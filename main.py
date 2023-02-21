import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands= ['start'])
def main_menu(message):
    startBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Услуги')
    startBoard.add(menu)
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку', reply_markup=startBoard)



#@bot.message_handler(commands=['start'])
#def main_menu(message):
#    startKBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    student = types.KeyboardButton("Ученики")
#    tablet = types.KeyboardButton("Расписание")
#    notice = types.KeyboardButton("Уведомления")
#    startKBoard.add(student, tablet, notice)
#    bot.send_message(message.chat.id, "Добро пожаловать в расписание!", reply_markup=startKBoard)

bot.polling()