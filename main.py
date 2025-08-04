import requests
import datetime
import jdatetime
import time
import telegram
from bs4 import BeautifulSoup

BOT_TOKEN = '8495684260:AAGpOxlVDeNxVbz8aiFFN0WHqJENTR4Wz5s'
CHANNEL_ID = '@amirgoldprice'
bot = telegram.Bot(token=BOT_TOKEN)

def format_price(price):
    if price:
        return f"{int(price):,}".replace(",", "٫")
    return "نامشخص"

def get_prices():
    url = "https://www.tgju.org"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    def extract(id_):
        tag = soup.find("td", {"id": id_})
        return tag.text.strip().replace(",", "") if tag else None

    prices = {
        "ons": extract("l-me"),
        "mesghal": extract("ls-mesghal"),
        "gold18": extract("ls-geram18"),
        "gold24": extract("ls-geram24"),
        "coin_imami": extract("ls-sekee"),
        "coin_bahar": extract("ls-bahartala"),
        "half": extract("ls-nim"),
        "quarter": extract("ls-rob"),
        "grami": extract("ls-gerami")
    }

    return prices

def build_message(prices):
    now = datetime.datetime.now()
    jalali_now = jdatetime.datetime.fromgregorian(datetime=now)
    time_str = jalali_now.strftime("🗓️ %d %B %Y - %H:%M:%S")

    msg = f"""📞 09194900317 | ☎️ 02133338705

{time_str}

🔹اونس طلا: $ {prices['ons']}
🔹مثقال طلا: {format_price(prices['mesghal'])}
🔹طلا ۱۸ عیار: {format_price(prices['gold18'])}
🔹طلای ۲۴ عیار: {format_price(prices['gold24'])}
🔹سکه امامی: {format_price(prices['coin_imami'])}
🔹سکه بهار آزادی: {format_price(prices['coin_bahar'])}
🔹نیم سکه: {format_price(prices['half'])}
🔹ربع سکه: {format_price(prices['quarter'])}
🔹سکه گرمی: {format_price(prices['grami'])}

@gold21ir
"""
    return msg

def main():
    while True:
        try:
            prices = get_prices()
            message = build_message(prices)
            bot.send_message(chat_id=CHANNEL_ID, text=message)
        except Exception as e:
            print("خطا:", e)
        time.sleep(60)

if __name__ == '__main__':
    main()
  
