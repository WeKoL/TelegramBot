from telebot import types

def startMenu():
    startMenu_kbd = types.InlineKeyboardMarkup()
    i1 = types.InlineKeyboardButton("Приступить!", callback_data='startMenu')
    startMenu_kbd.add(i1)
    return startMenu_kbd


def mainMenu():
    mainMenu_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Математика", callback_data='MainMenu')
    mainMenu_kbd.add(i1)
    return mainMenu_kbd


