import telebot
import requests
# initializing the bot
bot = telebot.TeleBot('{Your API key in t.me/botfather}')

# "/start" processing
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('⛅Forecast⛅', '🏦Сurrency rate🏦')
    keyboard.row('📰News📰(beta)', '🪙Crypto🪙')
    bot.send_message(message.chat.id, f'🇷🇺 🇺🇦 🇰🇿 🇦🇿 🇦🇲 Приветсивую тебя!\n Я твой помощник в быстром поиске нужной информации!\n Бот совершенствуется, поэтому перед каждой работой:\n проверяйте обновления в боте командой - /start \n большое спасибо🙏\n \n 🇬🇧 🇺🇸 Greetings to you!\n I am your assistant in a quick search for the right information!\n The bot is improving, so before each job:\n check for updates in the bot with the command - /start \n big bless🙏', reply_markup=keyboard)

# "Weather" button
@bot.message_handler(func=lambda message: message.text == '⛅Forecast⛅')
def weather_message(message):
    city = 'New York City' # <--You can write ur town here
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Your API key}&units=metric'
    response = requests.get(url).json()
    weather = response['weather'][0]['description']
    temp = response['main']['temp']
    bot.send_message(message.chat.id, f'Weather in {city}: {weather}, the temperature is: {temp}°C')

# "Сurrency rate" button
@bot.message_handler(func=lambda message: message.text == '🏦Сurrency rate🏦')
def currency_message(message):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    usd_rate = response['Valute']['USD']['Value']
    eur_rate = response['Valute']['EUR']['Value']
    bot.send_message(message.chat.id, f'💵USD: {usd_rate}₽\n💶EUR: {eur_rate}₽')

# "News" button
@bot.message_handler(func=lambda message: message.text == '📰News📰(beta)')
def news_message(message):
    url = 'https://newsapi.org/v2/top-headlines?country=ru&category=technology&apiKey={Your API key}'
    response = requests.get(url).json()
    articles = response['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        bot.send_message(message.chat.id, f'{title}\n{description}')

# "Crypto" button
@bot.message_handler(func=lambda message: message.text == '🪙Crypto🪙')
def crypto_message(message):
    url = 'https://api.coincap.io/v2/assets/bitcoin'
    response = requests.get(url).json()
    usd_price = response['data']['priceUsd']
    rub_price = round(float(usd_price) * get_usd_rate(), 2)
    bot.send_message(message.chat.id, f'🪙BTC: {usd_price}$ ({rub_price}₽)')

# taking currency rate
def get_usd_rate():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    usd_rate = response['Valute']['USD']['Value']
    return usd_rate

# Starting bot
bot.polling()
