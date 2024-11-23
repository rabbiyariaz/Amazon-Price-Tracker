# Amazon-Price-Tracker
This project is a Price Tracker Tool for Amazon products that:

Monitors the price of a specific product.
Compares the current price against a user-defined threshold.
Sends an email alert when the product price drops below the threshold.

## Features
Scrapes product details (e.g., price, sizes) using BeautifulSoup.
Sends price drop alerts via email using the smtplib library.
Uses dotenv for secure storage of sensitive credentials (email login, SMTP server details).
Customizable product size and price threshold.

## Installation and Setup
### Set Up Environment Variables
Create a .env file in the root directory and add the following details:
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_password_for_email
TO_ADDRESS=recipient_email@example.com
SMTP_ADDRESS=smtp.example.com

