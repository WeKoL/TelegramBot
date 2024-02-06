import telebot, config
from buttons import (startMenu,mainMenu)
from Math import (MathMenu,
                  PlanimetryMathMenu,TheoryPlanimetryMath, #планиметрия
                  VectorsMathMenu,TheoryVectorsMath, #векторы
                  StereometryMathMenu,TheoryStereometryMath, #стереометрия
                  ProbabilityTheoryMathMenu, TheoryProbabilityTheoryMath  # Теория вероятностей
                  )
from tasks import (TasksPlanimetryMath, TasksVectorsMath, TasksStereometryMath,TasksProbabilityTheoryMath )
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я telegram bot, я помогу тебе с подготовкой к экзаменам".format(
                         message.from_user),
                     reply_markup=startMenu(),)


@bot.callback_query_handler(func=lambda call: True)
def call_Query(message):
    if message.message:
        if (message.data == 'startMenu'):
            bot.send_message(message.message.chat.id, "Выбери предмет по которому хочешь подготовиться", reply_markup=mainMenu())
        elif(message.data == 'TasksPlanimetryMath'):
            bot.send_message(message.message.chat.id, "Выбери задание:",
                             reply_markup=TasksPlanimetryMath())
        elif (message.data == 'TasksVectorsMath'):
            bot.send_message(message.message.chat.id, "Выбери задание:",
                             reply_markup=TasksVectorsMath())
        elif (message.data == 'TasksStereometryMath'):
            bot.send_message(message.message.chat.id, "Выбери задание:",
                             reply_markup=TasksStereometryMath())
        elif (message.data == 'TasksProbabilityTheoryMath'):
            bot.send_message(message.message.chat.id, "Выбери задание:",
                             reply_markup=TasksProbabilityTheoryMath())
        elif (message.data == 'TasksPlanimetryMath1.1'):
            bot.send_message(message.message.chat.id, "Задание 1.1 Напиши мне ответ в чат!",
                             reply_markup=TasksPlanimetryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/DFtuAHQ')
        elif (message.data == 'TasksPlanimetryMath1.2'):
            bot.send_message(message.message.chat.id, "Задание 1.2 Напиши мне ответ в чат!",
                             reply_markup=TasksPlanimetryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/Vu8wnzx')
        elif (message.data == 'TasksPlanimetryMath1.3'):
            bot.send_message(message.message.chat.id, "Задание 1.3 Напиши мне ответ в чат!",
                             reply_markup=TasksPlanimetryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/yuVgBta')
        elif (message.data == 'TasksPlanimetryMath1.4'):
            bot.send_message(message.message.chat.id, "Задание 1.4 Напиши мне ответ в чат!",
                             reply_markup=TasksPlanimetryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/4yuhf6U')
        elif (message.data == 'TasksPlanimetryMath1.5'):
            bot.send_message(message.message.chat.id, "Задание 1.5 Напиши мне ответ в чат!",
                             reply_markup=TasksPlanimetryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/w8Nz4OL')
        elif (message.data == 'TasksVectorsMath2.1'):
            bot.send_message(message.message.chat.id, "Задание 2.1 Напиши мне ответ в чат!",
                             reply_markup=TasksVectorsMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/JHWsut0')
        elif (message.data == 'TasksVectorsMath2.2'):
            bot.send_message(message.message.chat.id, "Задание 2.2 Напиши мне ответ в чат!",
                             reply_markup=TasksVectorsMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/jMKoZRC')
        elif (message.data == 'TasksVectorsMath2.3'):
            bot.send_message(message.message.chat.id, "Задание 2.3 Напиши мне ответ в чат!",
                             reply_markup=TasksVectorsMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/WDmqdXz')
        elif (message.data == 'TasksVectorsMath2.4'):
            bot.send_message(message.message.chat.id, "Задание 2.4 Напиши мне ответ в чат!",
                             reply_markup=TasksVectorsMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/nWfQDDz')
        elif (message.data == 'TasksVectorsMath2.5'):
            bot.send_message(message.message.chat.id, "Задание 2.5 Напиши мне ответ в чат!",
                             reply_markup=TasksVectorsMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/5dtUDrd')
        elif (message.data == 'TasksStereometryMath3.1'):
            bot.send_message(message.message.chat.id, "Задание 3.1 Напиши мне ответ в чат!",
                             reply_markup=TasksStereometryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/5a3gFQt')
        elif (message.data == 'TasksStereometryMath3.2'):
            bot.send_message(message.message.chat.id, "Задание 3.2 Напиши мне ответ в чат!",
                             reply_markup=TasksStereometryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/3H0N6uN')
        elif (message.data == 'TasksStereometryMath3.3'):
            bot.send_message(message.message.chat.id, "Задание 3.3 Напиши мне ответ в чат!",
                             reply_markup=TasksStereometryMath())
            bot.send_photo(message.message.chat.id, 'https://imgur.com/a/tJVUOKG')
        elif (message.data == 'TasksStereometryMath3.4'):
            bot.send_message(message.message.chat.id, "Задание 3.4 Напиши мне ответ в чат!",
                             reply_markup=TasksStereometryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/zb7thmSJ')
        elif (message.data == 'TasksStereometryMath3.5'):
            bot.send_message(message.message.chat.id, "Задание 3.5 Напиши мне ответ в чат!",
                             reply_markup=TasksStereometryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/14W75Q3B')
        elif (message.data == 'TasksProbabilityTheoryMath4.1'):
            bot.send_message(message.message.chat.id, "Задание 4.1 Напиши мне ответ в чат!",
                             reply_markup=TasksProbabilityTheoryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/kV9vv15D')
        elif (message.data == 'TasksProbabilityTheoryMath4.2'):
            bot.send_message(message.message.chat.id, "Задание 4.2 Напиши мне ответ в чат!",
                             reply_markup=TasksProbabilityTheoryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/yWWXjS7h')
        elif (message.data == 'TasksProbabilityTheoryMath4.3'):
            bot.send_message(message.message.chat.id, "Задание 4.3 Напиши мне ответ в чат!",
                             reply_markup=TasksProbabilityTheoryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/rKrGXX0K')
        elif (message.data == 'TasksProbabilityTheoryMath4.4'):
            bot.send_message(message.message.chat.id, "Задание 4.4 Напиши мне ответ в чат!",
                             reply_markup=TasksProbabilityTheoryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/kV9vv15D')
        elif (message.data == 'TasksProbabilityTheoryMath4.5'):
            bot.send_message(message.message.chat.id, "Задание 4.5 Напиши мне ответ в чат!",
                             reply_markup=TasksProbabilityTheoryMath())
            bot.send_photo(message.message.chat.id, 'https://postimg.cc/Y4bYftVy')
        bot.answer_callback_query(callback_query_id=message.id, show_alert=False)
        # удаление inline кнопок
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                      reply_markup=None)
        # Удаление предыдущего сообщения от бота
        bot.delete_message(message.message.chat.id, message.message.message_id)

@bot.message_handler(content_types=['text'])
def Math_message(message):
    if (message.text  == "Математика"):
        bot.send_message(message.chat.id, text="Выбери тему:", reply_markup=MathMenu())

    elif (message.text == "Планиметрия"):
        bot.send_message(message.chat.id, text="Выбери тип занятия:", reply_markup=PlanimetryMathMenu())
    elif (message.text == "Векторы"):
        bot.send_message(message.chat.id, text="Выбери тип занятия:", reply_markup=VectorsMathMenu())
    elif (message.text == "Стереометрия"):
        bot.send_message(message.chat.id, text="Выбери тип занятия:", reply_markup=StereometryMathMenu())
    elif (message.text == "Теория вероятностей"):
        bot.send_message(message.chat.id, text="Выбери тип занятия:", reply_markup=ProbabilityTheoryMathMenu())

    elif (message.text == "Теория по планеметрии"):
        bot.send_message(message.chat.id, text="Потверди отправку!", reply_markup=TheoryPlanimetryMath())
    elif (message.text == "Теория по векторам"):
        bot.send_message(message.chat.id, text="Потверди отправку!", reply_markup=TheoryVectorsMath())
    elif (message.text == "Теория по стереометрии"):
        bot.send_message(message.chat.id, text="Потверди отправку!", reply_markup=TheoryStereometryMath())
    elif (message.text == "Теория по теории вероятностей"):
        bot.send_message(message.chat.id, text="Потверди отправку!", reply_markup=TheoryProbabilityTheoryMath())

    elif (message.text == "Задания по планеметрии"):
        bot.send_message(message.chat.id, text="Выбери задание:", reply_markup=TasksPlanimetryMath())
    elif (message.text == "Задания по векторам"):
        bot.send_message(message.chat.id, text="Выбери задание:", reply_markup=TasksVectorsMath())
    elif (message.text == "Задания по стереометрии"):
        bot.send_message(message.chat.id, text="Выбери задание:", reply_markup=TasksStereometryMath())
    elif (message.text == "Задания по теории вероятностей"):
        bot.send_message(message.chat.id, text="Выбери задание:", reply_markup=TasksProbabilityTheoryMath())

    elif (message.text == "Вернуться в главное меню"):
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню!", reply_markup=mainMenu())
    elif (message.text == "Назад"):
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню!", reply_markup=mainMenu())

    elif (message.text == "Отправить теорию по планеметрии"):
        bot.send_message(message.chat.id, text="Отправляю...", reply_markup=PlanimetryMathMenu())
        bot.send_photo(message.chat.id, 'https://postimg.cc/4KdmGVLB')
        bot.send_photo(message.chat.id, 'https://postimg.cc/Dmsm726k')
        bot.send_photo(message.chat.id, 'https://postimg.cc/R3DqZh29')
        bot.send_photo(message.chat.id, 'https://postimg.cc/fSxbCKyT')
        bot.send_photo(message.chat.id, 'https://postimg.cc/R6Jh69zt')
        bot.send_photo(message.chat.id, 'https://postimg.cc/1fQXtL7g')
        bot.send_photo(message.chat.id, 'https://postimg.cc/rR6m5b8P')
        bot.send_photo(message.chat.id, 'https://postimg.cc/VJ7kK5fM')
        bot.send_photo(message.chat.id, 'https://postimg.cc/jDqj6ybt')
    elif (message.text == "Отправить теорию по векторам"):
        bot.send_message(message.chat.id, text="Отправляю...", reply_markup=VectorsMathMenu())
        bot.send_photo(message.chat.id, 'https://postimg.cc/q6k7mK3s')
    elif (message.text == "Отправить теорию по стереометрии"):
        bot.send_message(message.chat.id, text="Отправляю...", reply_markup=StereometryMathMenu())
        bot.send_photo(message.chat.id, 'https://postimg.cc/CzB331sk')
        bot.send_photo(message.chat.id, 'https://postimg.cc/qhvYjM7t')
        bot.send_photo(message.chat.id, 'https://postimg.cc/WD2f1bg9')
        bot.send_photo(message.chat.id, 'https://postimg.cc/3kQczZRQ')
        bot.send_photo(message.chat.id, 'https://postimg.cc/87d0GrJJ')
        bot.send_photo(message.chat.id, 'https://postimg.cc/hhww1nRj')
        bot.send_photo(message.chat.id, 'https://postimg.cc/4Ypr3SM3')
        bot.send_photo(message.chat.id, 'https://postimg.cc/nsZN91bG')
        bot.send_photo(message.chat.id, 'https://postimg.cc/sGBLC67s')
        bot.send_photo(message.chat.id, 'https://postimg.cc/zLj6CRqZ')
        bot.send_photo(message.chat.id, 'https://postimg.cc/G8gfNwBX')
        bot.send_photo(message.chat.id, 'https://postimg.cc/vDDknBjk')
        bot.send_photo(message.chat.id, 'https://postimg.cc/gnZ7M7GK')
    elif (message.text == "Отправить теорию по теории вероятностей"):
        bot.send_message(message.chat.id, text="Отправляю...", reply_markup=ProbabilityTheoryMathMenu())
        bot.send_photo(message.chat.id, 'https://imgur.com/a/ITPHk73')
        bot.send_photo(message.chat.id, 'https://imgur.com/a/Z4w91Wm')
        bot.send_photo(message.chat.id, 'https://imgur.com/a/aeYfwo3')
        bot.send_photo(message.chat.id, 'https://imgur.com/a/eyKQdJQ')
        bot.send_photo(message.chat.id, 'https://imgur.com/a/B0zxSCa')

    elif (message.text == "48"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "0,3"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "576"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "171"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "125"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "17,5"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "2"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "0,25"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "10"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "1"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "0"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    elif (message.text == "5"):
        bot.send_message(message.chat.id, text="{0.first_name}! Это правильный ответ!".format(message.from_user))
    else :
        bot.send_message(message.chat.id, text="Я тебя не понял, попробуй сначала", reply_markup=mainMenu())

bot.polling(none_stop=True)