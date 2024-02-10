import os
import time
import smtplib
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Website URL
url = "https://www.airasia.com/flights/search/?origin=BKI&destination=KUL&departDate=21%2F02%2F2024&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&airlineProfile=all&type=paired&cabinClass=economy&upsellWidget=true&upsellPremiumFlatbedWidget=true&isOC=false&isDC=false&uce=false&ancillaryAbTest=false&providers=&taIDs="
# User Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

# Global variable to store the previous flight price
previous_flight_price = 388

# Function used to extract flight ticket information
def check_price():
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    try:
        # Wait for the element to be located
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='21/02/2024']/div[2]/div/div[2]"))
        )

        # Once the element is located, extract its text
        extracted_price = driver.find_element(By.XPATH, "//*[@id='21/02/2024']/div[2]/div/div[2]").text
        # Convert the price from string to integer
        converted_price = int(extracted_price)

    finally:
        # Close the WebDriver
        time.sleep(5)
        driver.quit()

    return converted_price 

# Function used to send email notification
def send_mail(email, recipient, pwd, subject, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, pwd)

    subject = subject
    body = f"The flight ticket price from Kota Kinabalu to Kuala Lumpur on February 21 {text}\n\nCheck the ticket prices through this link:\n{url}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        recipient,
        msg
    )
    print("Email Successfully Sent!")

    server.quit()

# Main function to execute the script
def main():
    global previous_flight_price

    email = os.environ.get('SENDER_EMAIL')
    recipient = os.environ.get('RECIPIENT_EMAIL')
    pwd = os.environ.get('SENDER_EMAIL_PASSWORD')

    flight_price = check_price()

    print(f"The current cheapest price is RM {flight_price}")

    if previous_flight_price is not None:  # Check if previous_flight_price has been initialized
        # Compare prices and pass relevant data as parameters to the send_mail function
        if (flight_price < previous_flight_price):
            send_mail(email, recipient, pwd, "The flight ticket price has fallen!", f"has gone from RM {previous_flight_price} to RM {flight_price}!")
        elif (flight_price > previous_flight_price):
            send_mail(email, recipient, pwd, "The flight ticket price has risen!", f"has gone from RM {previous_flight_price} to RM {flight_price}!")
        elif (flight_price == previous_flight_price):
            send_mail(email, recipient, pwd, "Flight Ticket Price Update", f"is currently still at RM {previous_flight_price}")

    # Update previous_flight_price with the latest flight_price
    previous_flight_price = flight_price

# Schedule task with schedule library        
if __name__ == "__main__":
    schedule.every().day.at("18:35").do(main)
    schedule.every().day.at("21:45").do(main)
    schedule.every().day.at("21:50").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1) 

