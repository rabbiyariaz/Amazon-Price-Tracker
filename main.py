import smtplib
import dotenv
import os
from bs4 import BeautifulSoup
import requests

price_of_interested = 0
dotenv.load_dotenv()
url = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    'Accept-Language': "en-PK,en-US;q=0.9,en-GB;q=0.8,en;q=0.7",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# Fetch the webpage content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.select_one("#submit.add-to-cart-button")
print(title)

# Extracting sizes
size_elements = soup.select("div.tooltip p.a-size-base")
size_list = [i.text.strip() for i in size_elements]
print(size_list)

# User's choice
user_choice_of_size = "6 Quarts"

# Checking if the user's choice exists in the list

if user_choice_of_size in size_list:
    print("hello")
    index_of_user_choice = size_list.index(user_choice_of_size)

    # Extracting prices
    price_elements = soup.select("span.aok-offscreen")[0]
    price_of_interested = price_elements.text.strip()
    price_of_interested = float(price_of_interested.split('$')[1])

    print(f"Price of {user_choice_of_size}: {price_of_interested}")
else:
    print(f"Size {user_choice_of_size} not found.")
if price_of_interested < 150:
    message = f"{title} is on sale for {price_of_interested}!"
    try:
        server = smtplib.SMTP(os.getenv("SMTP_ADDRESS"), 587)
        server.starttls()
        server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        server.sendmail(from_addr=os.getenv("EMAIL_ADDRESS"), to_addrs=os.getenv("TO_ADDRESS"),
                        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))
    except Exception as e:
        print(e)
        print(e)
        
