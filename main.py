import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
import os


# Finding Price
AMAZON_URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
            "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Men-US,en;q=0.9"
            }

response = requests.get(AMAZON_URL, headers= headers)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
current_price = soup.find(class_="a-offscreen").getText()
current_price = current_price.split("$")[1]
print(current_price)


# sending email
my_email = os.environ.get("my_email")
password = os.environ.get("password")


if float(current_price) <= 130:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="madasar54321@gmail.com",
                            msg= f"Subject: Low Price Alert\n\nPrice has gone down to {current_price}. You should seriously consdier buying it now bruv.\nits now or never."
                            )










