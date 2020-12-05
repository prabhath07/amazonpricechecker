import smtplib
import requests
from bs4 import BeautifulSoup

headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
URL ='https://www.amazon.in/dp/B08L5WHFT9/ref=gwdb_bmc_1_CP_BudgetQC_h?pf_rd_s=merchandised-search-14&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=WNJ6QECN16D8APCZVJKY&pf_rd_p=0d3fbf21-d551-4603-a78b-2fc1a6bd56f0'



def checkprice():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content , 'html.parser')
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    cprice = float(price[1:4])
    print(cprice)
    if (cprice < 100 ):
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.google.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('prabhath2002sai@gmail.com', 'rsgusgplzmofjdfe')
    subject = 'price came to your standards'
    body = 'checking the price '
    msg = f"subject:{subject}\n\n{body}"
    server.sendmail('prabhath2002sai@gmail.com','prabhath2002sai@gmail.com', msg)
    print("email is sent")

checkprice()


