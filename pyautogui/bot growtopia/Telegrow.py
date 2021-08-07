from constans import API_KEY
from responses import respons
from telegram.ext import *

def handle_message(update, context):
    respons(update)

updater = Updater(API_KEY)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.all, handle_message, pass_chat_data=True))

updater.start_polling()
updater.idle()