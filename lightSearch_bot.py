import telebot
import requests
import time

# initializing the bot
bot = telebot.TeleBot('Your Token')

# "/start" processing
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('📰', '🪙', '⛅', '🏦','🔄')
    
    bot.send_message(message.chat.id, f"🇷🇺 🇺🇦 🇧🇾 Приветствую тебя! 🇦🇿 🇰🇿 🇦🇲 \nЯ твой помощник в быстром поиске нужной информации!\nБот совершенствуется, поэтому перед каждой работой:\nпроверяйте обновления в боте командой - /start\nобязательно зайди в телеграмм канал с обновами - https://t.me/lightSearch_inf\nбольшое спасибо🙏\n \n🇬🇧 🇺🇸 Greetings to you! \nI am your assistant in a quick search for the right information!\nThe bot is improving, so before each job:\ncheck for updates in the bot with the command - /start\nfollow telegram channel with updates - https://t.me/lightSearch_inf\nbig bless🙏 \n \nversion 1.0.3", reply_markup=keyboard)

# "Weather" button
@bot.message_handler(func=lambda message: message.text == '⛅')
def weather_message(message):
        bot.send_message(message.chat.id, f'Write your city in chat & send location')
        bot.register_next_step_handler(message, get_weather)

def get_weather(message):
    city = message.text
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=Your Token=metric'
    response = requests.get(url).json()
    if response['cod'] == '404':
        bot.send_message(message.chat.id, f'City {city} not found❌')
    else:
        weather = response['weather'][0]['description']
        temp = response['main']['temp']
        bot.send_message(message.chat.id, f'⏳')
        time.sleep(1)
        bot.send_message(message.chat.id, f'Wait... 100%')
        bot.send_message(message.chat.id, f'OK✅')
        bot.send_message(message.chat.id, f'Weather in {city}\n \n 🌅{weather} \n🌡the temperature is: {temp}°C')

# "Сurrency rate" button
@bot.message_handler(func=lambda message: message.text == '🏦')
def currency_message(message):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    usd_rate = response['Valute']['USD']['Value']
    eur_rate = response['Valute']['EUR']['Value']
    cny_rate = response['Valute']['CNY']['Value']
    bot.send_message(message.chat.id, f'⏳')
    time.sleep(1)
    bot.send_message(message.chat.id, f'Wait... 100%')
    bot.send_message(message.chat.id, f'OK✅')
    bot.send_message(message.chat.id, f'💰Exchange rates at the Central Bank of Russia💰\n \n💵USD: {usd_rate}₽\n💶EUR: {eur_rate}₽\n💴CNY: {cny_rate}')

# "News" button
@bot.message_handler(func=lambda message: message.text == '📰')
def news_message(message):
    url_api = 'https://newsapi.org/v2/top-headlines?country=ru&category=technology&apiKey=Your Token'
    response = requests.get(url_api).json()
    articles = response['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        bot.send_message(message.chat.id, f'{url}', disable_notification = True)

# "Crypto" button
@bot.message_handler(func=lambda message: message.text == '🪙')
def crypto_message(message):
    url = 'https://api.coincap.io/v2/assets/bitcoin'
    response = requests.get(url).json()
    usd_price = response['data']['priceUsd']
    rub_price = round(float(usd_price) * get_usd_rate(), 2)
    bot.send_message(message.chat.id, f'⏳')
    time.sleep(1)
    bot.send_message(message.chat.id, f'Wait... 100%')
    bot.send_message(message.chat.id, f'OK✅')
    bot.send_message(message.chat.id, f'Bitcoin Rate\n \n🪙BTC in USD🇺🇸: {usd_price}$ \n🪙BTC in RUB🇷🇺: {rub_price}₽')
    
@bot.message_handler(func=lambda message: message.text == '🔄')
def refresh_message(message):
    bot.send_message(message.chat.id, f'Wait. 10%')
    time.sleep(3)
    bot.send_message(message.chat.id, f'Wait... 30%')
    time.sleep(3)
    bot.send_message(message.chat.id, f'Wait....... 65%')
    time.sleep(1)
    bot.send_message(message.chat.id, f'Wait......... 96%')
    time.sleep(4)
    bot.send_message(message.chat.id, f'Wait......... 97%')
    time.sleep(1)
    bot.send_message(message.chat.id, f'Wait.......... 99%')
    time.sleep(7)
    bot.send_message(message.chat.id, f'❌ERROR❌')
    time.sleep(1)
    bot.send_message(message.chat.id, f'sorry bout that... ')
    bot.send_message(message.chat.id, f'как быть с этой кнопкой подскажите?\n🥹')
# taking currency rate
def get_usd_rate():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    usd_rate = response['Valute']['USD']['Value']
    return usd_rate

# Starting bot
bot.polling()
