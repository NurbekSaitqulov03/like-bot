import telegram
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

TOKEN=os.environ['TOKEN']

def main(update, context):
    bot = context.bot

    chat_id = update.message.chat.id
    text = update.message.text
    button1 = InlineKeyboardButton(text='👍', callback_data="like_emoji")
    button2 = InlineKeyboardButton(text='👎', callback_data="dislike_emoji")
    keyboard = InlineKeyboardMarkup([[button1, button2]])

    bot.sendMessage(chat_id=chat_id, text=text, reply_markup=keyboard)

def count(update, context):
    query = update.callback_query
    print(query.data)
    
updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, main))
dp.add_handler(CallbackQueryHandler(count))

updater.start_polling()
updater.idle()