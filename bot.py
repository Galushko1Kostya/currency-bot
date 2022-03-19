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

def currency_sum(update, context):
    chat = update.effective_chat
    currency_code = update.message.text
    global date_22
    global date_21
    date_22 = datetime.datetime.now()
    date_21 = str(datetime.datetime.now() - datetime.timedelta(days=365))
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate1 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='f'{currency_code}&date='f'{date_21}&json').json()
        currency_rate2 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='f'{currency_code}&date='f'{date_22}&json').json()                              
        rate1 = currency_rate1[0]['rate']
        rate2 = currency_rate2[0]['rate']
        value_new = f'{currency_code} rate: {rate1} UAH'
        value_old = f'{currency_code} rate: {rate2} UAH'
    message_sum = value_new - value_old
    context.bot.send_message(chat_id=chat.id, text=message_sum)

def create_message_to_json(currency_code, rate, message_sum):
    data = {"currency code" : currency_code, "rate" : rate, "result" : message_sum}
    with open("neww.json", "a") as f:
        f.append(json.dumps(data))

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(CommandHandler('json', create_message_to_json))
disp.add_handler(MessageHandler(Filters.all, currency_sum))
updater.start_polling()
updater.idle()