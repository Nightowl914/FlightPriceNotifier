# FlightPriceNotifier


## Introduction
This Python script is designed to track flight ticket prices for a specific route and date using a deisred airline website. It utilizes Selenium for web scraping to extract the ticket price information and sends email notifications to users when there are changes in the ticket prices. The script is scheduled to run at specific times each day to check for updates in ticket prices and send notifications accordingly.

## Instructions
1. #### Clone the Repository:
```
git clone https://github.com/Nightowl914/FlightPriceNotifier.git
```

2. #### Environment Setup:
- ##### Ensure you have Python installed on your system.
- ##### Install the required Python packages using pip:
  ```
  pip install selenium schedule python-dotenv
  ```
- ##### Make sure you have a compatible version of Chrome installed on your system.

3. #### Configure Environment Variables:
- ##### Add the following environment variables to the .env file:
  ```
  SENDER_EMAIL=your_email@gmail.com
  RECIPIENT_EMAIL=recipient_email@example.com
  SENDER_EMAIL_PASSWORD=your_email_password
  ```
- ##### Replace your_email@gmail.com with your Gmail address, recipient_email@example.com with the recipient's email address, and your_email_password with your Gmail account password.
  
4. #### Run the script:
-##### Execute the Python script by running the following command in your terminal or command prompt:
 ```
 python main.py
 ```

5. #### Scheduled Execution:
-##### The script will run at the specified times each day to check for updates in ticket prices.
-##### You can modify the schedule by adjusting the 'schedule.every().day.at()' calls in the script to your preferred times.

6. #### Receive Email Notifications:
-##### If there are changes in ticket prices, you will receive email notifications at the specified email address (RECIPIENT_EMAIL).

Feel free to customize the script, update the 'url' and use different selector with selenium if you want to track flight prices for a different route or date using your desired airline website.
