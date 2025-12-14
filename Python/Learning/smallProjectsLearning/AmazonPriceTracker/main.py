from bs4 import BeautifulSoup
import requests
import smtplib
import smtplib
import  os
from dotenv import load_dotenv
load_dotenv()
def sendEmail(message="Subject: testing email from python\n\nHELLO FROM PYTHON",destination = os.environ.get("receiver_email")):
    email = os.environ.get("sender_email")
    app_password = os.environ.get("app_password") #
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password = app_password)
            connection.sendmail(from_addr=email,to_addrs=destination,msg=message)
            connection.close()


def priceAlert(link,targetPrice):
    response = requests.get(link)
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')
    price = soup.find(name="span", class_="a-price-whole").getText()
    price = float(price.replace(',', ''))
    productName = soup.find(id="productTitle").getText().strip()
    print(f"Price for Apple Ipad is : {price} EUR, it's type is {type(price)}")
    if price<=targetPrice:
        sendEmail(message=f"Subject: Price Drop Alert!\n\nThe price for {productName} is now {price} EUR. Hurry up!")

priceAlert(link="https://www.amazon.it/-/en/Optix-MEG381CQR-Curved-Gaming-Monitor/dp/B08ZSW4X6Y/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=CUCA3&content-id=amzn1.sym.e3f88a6b-72fb-4584-84ff-acf892c36061%3Aamzn1.symc.30e3dbb4-8dd8-4bad-b7a1-a45bcdbc49b8&pf_rd_p=e3f88a6b-72fb-4584-84ff-acf892c36061&pf_rd_r=3SVMW6B6BZE47RC28KQN&pd_rd_wg=heyip&pd_rd_r=893c2709-3292-4208-bece-84a6c1283152&pd_rd_i=B08ZSW4X6Y&th=1",targetPrice=2600 )