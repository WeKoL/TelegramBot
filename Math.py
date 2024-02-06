from telebot import types

def MathMenu():
    Math_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Планиметрия", callback_data='PlanimetryMathMenu')
    i2 = types.InlineKeyboardButton("Векторы", callback_data='VectorsMathMenu')
    i3 = types.InlineKeyboardButton("Стереометрия", callback_data='StereometryMathMenu')
    i4 = types.InlineKeyboardButton("Теория вероятностей", callback_data='ProbabilityTheoryMathMenu')
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='mainMenu')
    Math_kbd.add(i1, i2)
    Math_kbd.add(i3, i4)
    Math_kbd.add(back)
    return Math_kbd

def PlanimetryMathMenu(): # Планиметрия
    PlanimetryMath_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Теория по планеметрии", callback_data='TheoryPlanimetryMath')
    i2 = types.InlineKeyboardButton("Задания по планеметрии", callback_data='TasksPlanimetryMath')
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='MathMenu')
    PlanimetryMath_kbd.add(i1, i2)
    PlanimetryMath_kbd.add(back)
    return PlanimetryMath_kbd
def TheoryPlanimetryMath():
    TheoryPlanimetryMath_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Отправить теорию по планеметрии")
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='PlanimetryMath')
    TheoryPlanimetryMath_kbd.add(i1)
    TheoryPlanimetryMath_kbd.add(back)
    return TheoryPlanimetryMath_kbd


def VectorsMathMenu(): # Векторы
    VectorsMathMenu_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Теория по векторам", callback_data='TheoryVectorsMath')
    i2 = types.InlineKeyboardButton("Задания по векторам", callback_data='TasksVectorsMath')
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='MathMenu')
    VectorsMathMenu_kbd.add(i1, i2)
    VectorsMathMenu_kbd.add(back)
    return VectorsMathMenu_kbd
def TheoryVectorsMath():
    TheoryVectorsMath_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Отправить теорию по векторам")
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='VectorsMath')
    TheoryVectorsMath_kbd.add(i1)
    TheoryVectorsMath_kbd.add(back)
    return TheoryVectorsMath_kbd

def StereometryMathMenu(): # Стереометрия
    StereometryMathMenu_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Теория по стереометрии", callback_data='TheoryStereometryMath')
    i2 = types.InlineKeyboardButton("Задания по стереометрии", callback_data='TasksStereometryMath')
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='MathMenu')
    StereometryMathMenu_kbd.add(i1, i2)
    StereometryMathMenu_kbd.add(back)
    return StereometryMathMenu_kbd
def TheoryStereometryMath():
    TheoryStereometryMath_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Отправить теорию по стереометрии")
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='StereometryMathMenu')
    TheoryStereometryMath_kbd.add(i1)
    TheoryStereometryMath_kbd.add(back)
    return TheoryStereometryMath_kbd


def ProbabilityTheoryMathMenu(): # Теория вероятностей
    ProbabilityTheoryMathMenu_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Теория по теории вероятностей", callback_data='TheoryProbabilityTheoryMath')
    i2 = types.InlineKeyboardButton("Задания по теории вероятностей", callback_data='TasksProbabilityTheoryMath')
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='MathMenu')
    ProbabilityTheoryMathMenu_kbd.add(i1, i2)
    ProbabilityTheoryMathMenu_kbd.add(back)
    return ProbabilityTheoryMathMenu_kbd
def TheoryProbabilityTheoryMath():
    TheoryProbabilityTheoryMath_kbd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.InlineKeyboardButton("Отправить теорию по теории вероятностей")
    back = types.InlineKeyboardButton("Вернуться в главное меню", callback_data='ProbabilityTheoryMathMenu')
    TheoryProbabilityTheoryMath_kbd.add(i1)
    TheoryProbabilityTheoryMath_kbd.add(back)
    return TheoryProbabilityTheoryMath_kbd
