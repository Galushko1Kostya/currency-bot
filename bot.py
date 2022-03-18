import requests
import datetime
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, chat
TOKEN = '5155721257:AAHfnIfrQxaPiit3QnqR8QauW6Wa02eRGwc'
print("Bot is up")
updater = Updater(TOKEN)

def welcome(update, context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('USD')], [KeyboardButton('EUR')], [KeyboardButton('PLN')], [KeyboardButton('GEL')], [KeyboardButton('CAD')], [KeyboardButton('MXN')], [KeyboardButton('MDL')], [KeyboardButton('ILS')], [KeyboardButton('NOK')], [KeyboardButton('IDR')]]
    context.bot.send_message(chat_id=chat.id, text='Hello! I am your currency bot',
                             reply_markup=ReplyKeyboardMarkup(buttons))

def create_message_to_json(currency_code, date, rate):
    global data
    data = {"currency code" : currency_code, "date" : date, "rate" : rate}
    d = json.dumps(data)
    print(d)

def write_to_file(message):
    with open("new.json", "a") as f:
        f.append(json.dumps(data))

def currency_rate_22(update, context):
    chat = update.effective_chat
    currency_code = update.message.text
    date_21 = str(datetime.datetime.now() - datetime.timedelta(days=365))
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date='f'{date_21}&json').json()
        rate = currency_rate[0]['rate']
        global value_new
        value_new = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=value_new)

def currency_rate_21(update, context):
    chat = update.effective_chat
    currency_code = update.message.text
    date_22 = datetime.datetime.now()
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date='f'{date_22}&json').json()
        rate = currency_rate[0]['rate']
        global value_old
        value_old = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=value_old)

def sum(update, context):
    chat = update.effective_chat
    message_sum = value_new - value_old
    context.bot.send_message(chat_id=chat.id, text=message_sum)
    write_to_file(create_message_to_json())

def logging(a, b):
    memory.json
    [{
        'login':'',
        'password':'',
    }]
    pass

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(CommandHandler('currency_rate_new', currency_rate_22))
disp.add_handler(CommandHandler('currency_rate_old', currency_rate_21))
disp.add_handler(MessageHandler(Filters.all, sum))

updater.start_polling()
updater.idle()