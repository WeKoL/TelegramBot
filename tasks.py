import telebot, config
from telebot import types


bot = telebot.TeleBot(config.token)
def TasksPlanimetryMath():
    TasksPlanimetryMath_kbd = types.InlineKeyboardMarkup()
    i1 = types.InlineKeyboardButton("Задание 1.1", callback_data='TasksPlanimetryMath1.1')
    i2 = types.InlineKeyboardButton("Задание 1.2", callback_data='TasksPlanimetryMath1.2')
    i3 = types.InlineKeyboardButton("Задание 1.3", callback_data='TasksPlanimetryMath1.3')
    i4 = types.InlineKeyboardButton("Задание 1.4", callback_data='TasksPlanimetryMath1.4')
    i5 = types.InlineKeyboardButton("Задание 1.5", callback_data='TasksPlanimetryMath1.5')
    TasksPlanimetryMath_kbd.add(i1,i2,i3,i4,i5)
    return TasksPlanimetryMath_kbd
def TasksVectorsMath():
    TasksVectorsMath_kbd = types.InlineKeyboardMarkup()
    i1 = types.InlineKeyboardButton("Задание 2.1", callback_data='TasksVectorsMath2.1')
    i2 = types.InlineKeyboardButton("Задание 2.2", callback_data='TasksVectorsMath2.2')
    i3 = types.InlineKeyboardButton("Задание 2.3", callback_data='TasksVectorsMath2.3')
    i4 = types.InlineKeyboardButton("Задание 2.4", callback_data='TasksVectorsMath2.4')
    i5 = types.InlineKeyboardButton("Задание 2.5", callback_data='TasksVectorsMath2.5')
    TasksVectorsMath_kbd.add(i1,i2,i3,i4,i5)
    return TasksVectorsMath_kbd
def TasksStereometryMath():
    TasksStereometryMath_kbd = types.InlineKeyboardMarkup()
    i1 = types.InlineKeyboardButton("Задание 3.1", callback_data='TasksStereometryMath3.1')
    i2 = types.InlineKeyboardButton("Задание 3.2", callback_data='TasksStereometryMath3.2')
    i3 = types.InlineKeyboardButton("Задание 3.3", callback_data='TasksStereometryMath3.3')
    i4 = types.InlineKeyboardButton("Задание 3.4", callback_data='TasksStereometryMath3.4')
    i5 = types.InlineKeyboardButton("Задание 3.5", callback_data='TasksStereometryMath3.5')
    TasksStereometryMath_kbd.add(i1,i2,i3,i4,i5)
    return TasksStereometryMath_kbd
def TasksProbabilityTheoryMath():
    TasksProbabilityTheoryMath_kbd = types.InlineKeyboardMarkup()
    i1 = types.InlineKeyboardButton("Задание 4.1", callback_data='TasksProbabilityTheoryMath4.1')
    i2 = types.InlineKeyboardButton("Задание 4.2", callback_data='TasksProbabilityTheoryMath4.2')
    i3 = types.InlineKeyboardButton("Задание 4.3", callback_data='TasksProbabilityTheoryMath4.3')
    i4 = types.InlineKeyboardButton("Задание 4.4", callback_data='TasksProbabilityTheoryMath4.4')
    i5 = types.InlineKeyboardButton("Задание 4.5", callback_data='TasksProbabilityTheoryMath4.5')
    TasksProbabilityTheoryMath_kbd.add(i1,i2,i3,i4,i5)
    return TasksProbabilityTheoryMath_kbd