import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time

mail_host = 'smtp.163.com'
mail_user = 'zhanghao'
mail_pass = 'mima'
sender = 'zhanghao@163.com'
receivers = ['zhanghao@qq.com']

message = MIMEText('test content', 'plain', 'utf-8')
message['Subject'] = 'title'
message['From'] = sender
message['To'] = receivers[0]


def get_price(Url):
    float(868.17)
    res = requests.get(Url)
    soup = BeautifulSoup(res.text, "html.parser")
    tags = soup.find("span", attrs={
        "class": "cmc-details-panel-price__price"
    }).get_text()
    dat = float(tags.replace(',', '').replace('$', ''))
    # print(dat)
    return dat


def send_email():
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)


def get_rate():
    pbtc = get_price(
        "https://coinmarketcap.com/zh/currencies/bitcoin/markets/")
    peth = get_price(
        "https://coinmarketcap.com/zh/currencies/ethereum/markets/")
    btc_to_eth = pbtc / peth
    # print(btc_to_eth)
    return btc_to_eth


if __name__ == '__main__':
    cnt = 0
    old_rates = {}
    while 1:
        rate = get_rate()
        old_rates[cnt] = rate
        print('current rate (btc to eth) is: ', old_rates[cnt])
        # print(old_rates)
        if cnt >= 3600:
            diff = abs((rate - old_rates[cnt - 3600])) / old_rates[cnt - 3600]
            old_rates.pop((cnt - 3600))
            if diff >= 0.05:
                send_email()  # send alert to someone
        time.sleep(20)  # show current exchange rate every 20 seconds
        cnt += 20
