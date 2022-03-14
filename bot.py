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
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date=20220314&json').json()
        rate = currency_rate[0]['rate']
        global value_new
        value_new = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=value_new)

def currency_rate_21(update, context):
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL', 'CAD', 'MXN', 'MDL', 'ILS', 'NOK', 'IDR'):
        currency_rate = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date=20210314&json').json()
        rate = currency_rate[0]['rate']
        global value_old
        value_old = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=value_old)

def sum(update, context):
    chat = update.effective_chat
    message_sum = value_new - value_old
    context.bot.send_message(chat_id=chat.id, text=message_sum)

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(CommandHandler('courseone', currency_rate_22))
disp.add_handler(CommandHandler('coursetwo', currency_rate_21))
disp.add_handler(MessageHandler(Filters.all, sum))

updater.start_polling()
updater.idle()