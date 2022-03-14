import requests
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

def currency_rate_22(update, context):
    global message
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate1 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date=20220314&json').json()
        rate = currency_rate1[0]['rate']
        message = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=message)

def currency_rate_21(update, context):
    global message
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate2 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date=20210314&json').json()
        rate = currency_rate2[0]['rate']
        message = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=message)
 
    currency_rate_sum = currency_rate_22 - currency_rate_21
    message1 = f'{currency_rate_sum}'
    context.bot.send_message(chat_id=chat.id, text=message1)

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(MessageHandler(Filters.all, currency_rate_21))

updater.start_polling()
updater.idle()