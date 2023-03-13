import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands= ['start']) #/start - то вызов приветственного экрана который ты сейчас читаешь
def start_main_menu(message):
    bot.send_message(message.chat.id, "<b>Привет!</b>"
                                      "\nЭто бот помощник и он же моё портфолио. Давай я тебе расскажу что он может."
                                      "\n<b>Меню:</b>"
                                      "\n/start - вызов приветственного экрана" "<code>(ты сейчас его читаешь)</code>"
                                      "\n/help - подсказка с командами"
                                      "\n/about_me - тут я расскажу о себе"
                                      "\n/weather - узнаём погоду"
                                      "\n/currency_rate - курс валют"
                                      "\n/to_do_list - напоминания"
                                      "\n/to_do_list - напоминания"
                                      "\n/calculator - простой калькулятор" , parse_mode='html', reply_markup=types.ReplyKeyboardRemove())



@bot.message_handler(commands= ['weather']) #/weather - узнаём погоду
def weather_def (message):
    bot.send_message(message.chat.id, 'Это BOT который позволит узнать какая сейчас температура за окном. \nBOT запрашивает информацию через API с сайта openweathermap.org \nЕсли хотите Оценить как работает бот переходите по ссылке \nhttps://t.me/mkostarev_weather_bot', reply_markup=types.ReplyKeyboardRemove())



@bot.message_handler(commands= ['currency_rate']) #/currency_rate - курс валют currency_rate
def currency_rate_def(message):
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку, раздел Курс валют', reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands= ['help']) #/help - подсказка с командами
def help_def (message):
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку, задел Help', reply_markup=types.ReplyKeyboardRemove())






@bot.message_handler(commands= ['about_me']) #/about_me - вызов приветственного экрана который ты сейчас читаешь
def about_me_main_menu(message):
   #about_me_board = types.ReplyKeyboardMarkup(resize_keyboard=True)
   #biography = types.KeyboardButton('Биография')
   #portfolio = types.KeyboardButton('Портфолио')
   #contacts = types.KeyboardButton('Контакты')
   #about_me_board.add(biography, portfolio, contacts)
    about_me_board_inline = types.InlineKeyboardMarkup()
    biography_inline = types.InlineKeyboardButton(text="Биография", callback_data="biography_clicked")
    about_me_board_inline.add(biography_inline)
    bot.send_message(message.chat.id, "Это раздел ""<b>Обо мне</b>\nТут я немного расскужу о себе, своём опыте, своих целях.", parse_mode='html', reply_markup=about_me_board_inline)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):

    #chat_id = call.message.chat.id
    #message_id = call.message.message_id
    if call.data == "biography_clicked":
        biography_def(call.message)
        #bot.send_message(call.message.chat.id,"<b>1. Высшее образование:</b>"
        #                                               "\nОкончил СПбГЭТУ «ЛЭТИ» в 2015 году."
        #                                               "\nФакультет: Автоматизация технологических процессов."
        #                                               "\n\n<b>2. Среднее профессиональное образование:</b>"
        #                                               "\nОкончил БПОУ УР «ГТК» в 2010"
        #                                               "\nФакультет: Автоматизация и электрификация.", parse_mode='html')



#@bot.message_handler(content_types=['text'])
#def handler_about_me_main_menu (message)
#    if message.text == "Биография":
#        biography_def (message)
#    elif message.text == "Портфолио":
#        bot.send_message(message.chat.id,'Портфолио')
#    elif message.text == "Контакты":
#        bot.send_message(message.chat.id,'Контакты')




bot.message_handler(message=['text'])
def biography_def(message):
    bot.send_message(message.chat.id, "<b>1. Высшее образование:</b>"
                                      "\nОкончил СПбГЭТУ «ЛЭТИ» в 2015 году."
                                      "\nФакультет: Автоматизация технологических процессов."
                                      "\n\n<b>2. Среднее профессиональное образование:</b>"
                                      "\nОкончил БПОУ УР «ГТК» в 2010"
                                      "\nФакультет: Автоматизация и электрификация.", parse_mode='html')



#@bot.message_handler(commands= ['help']) #/help - подсказка с командами
#def help_def (message):
#    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку, задел Help', reply_markup=types.ReplyKeyboardRemove())




@bot.message_handler(commands= ['to_do_list']) #/to_do_list - подсказка с командами
def to_do_list_def(message):
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку, раздел Напоминания', reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands= ['calculator']) #/calculator - подсказка с командами
def calculator_def(message):
    bot.send_message(message.chat.id, 'Добропожаловать в бот визитку, раздел Простой калькулятор', reply_markup=types.ReplyKeyboardRemove())



bot.polling()