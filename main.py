import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands= ['start']) #/start - то вызов приветственного экрана который ты сейчас читаешь
def start_main_menu(message):
    bot.send_message(message.chat.id, """Привет! 
Это бот помощник и он же моё портфолио. 

Давай я тебе расскажу что он может.

"Меню":
/start - то вызов приветственного экрана который ты сейчас читаешь
/help - подсказка с командами
/about_me - тут я расскажу о себе, своих достижениях, своих целях
/weather - узнаём погоду
/currency_rate - курс валют
/to_do_list - напоминания
/calculator - простой калькулятор
/.........
""")


@bot.message_handler(commands= ['about_me']) #/start - то вызов приветственного экрана который ты сейчас читаешь
def about_me_main_menu(message):
    about_me_board = types.ReplyKeyboardMarkup(resize_keyboard=True)
    biography = types.KeyboardButton('Биография')
    portfolio = types.KeyboardButton('Портфолио')
    contacts = types.KeyboardButton('Контакты')
    about_me_board.add(biography, portfolio, contacts)
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку', reply_markup=about_me_board)

@bot.message_handler(commands= ['help']) #/help - подсказка с командами
def main_menu(message):
    #startBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #menu = types.KeyboardButton('Услуги')
    #startBoard.add(menu)
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку, задел Help')



#/help - подсказка с командами
#
#/about_me - тут я расскажу о себе, своих достижениях, своих целях
#
#/weather - узнаём погоду
#
#/currency_rate - курс валют
#
#/to_do_list - напоминания
#
#/calculator - простой калькулятор

#@bot.message_handler(commands=['start'])
#def main_menu(message):
#    startKBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    student = types.KeyboardButton("Ученики")
#    tablet = types.KeyboardButton("Расписание")
#    notice = types.KeyboardButton("Уведомления")
#    startKBoard.add(student, tablet, notice)
#    bot.send_message(message.chat.id, "Добро пожаловать в расписание!", reply_markup=startKBoard)

bot.polling()