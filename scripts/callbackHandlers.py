import sqlite3

import telebot
from telebot.types import Message

import Test_module
import defaultmessages


def mainMenu_button1_click(bot:telebot.TeleBot,message:Message):
    dostoprim_page1_click(bot,message)
    
def mainMenu_button2_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.GetGeo(bot,message)
    #bot.edit_message_text('Нажата кнопка 2',message.chat.id,message.message_id, reply_markup=keyboards.ToMainMenuKeyboard())

def mainMenu_button3_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditTestsMenu(bot,message)

def mainMenu_button4_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditGeneralInformation(bot,message)

def mainMenu_button5_click(bot:telebot.TeleBot,message:Message):
    pass

def mainMenu_button6_click(bot:telebot.TeleBot,message:Message):
    pass

def mainMenu_button7_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditGeneralInformation(bot,message)

# ----------------------------------

def dostoprim_page1_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditDostoprimPage1(bot, message)

def dostoprim_page2_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditDostoprimPage2(bot, message)
    
def dostoprim_page3_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditDostoprimPage3(bot, message)

# ----------------------------------

def dostoprim_obj_click(bot:telebot.TeleBot,message:Message,obj_id:int):
    defaultmessages.EditDostoprimObj(bot,message,obj_id)
    
def toMainMenu_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditMainMenu(bot,message)
def toMainMenu_geo_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.SendMainMenuRemoveKeyboard(bot,message)

# ----------------------------------
def answer_test_click(bot:telebot.TeleBot,message:Message,values:list[str],tests:list[Test_module.Test]):
    db = sqlite3.connect('../database/database.db')
    c = db.cursor()
    c.execute(f"""SELECT marks FROM test{values[0]} WHERE user_id = {message.chat.id}""")
    usertestdata = c.fetchone()
    usermarks = list(usertestdata[0])


    if (values[2] == values[3]):
        usermarks[int(values[1])] = '1'
        print('Верный ответ')

    else:
        usermarks[int(values[1])] = '0'
        print('Не верный ответ')

    resylt = ''.join(usermarks)
    c.execute(f"""UPDATE test{values[0]} SET marks = '{resylt}' WHERE user_id = {message.chat.id}""")
    db.commit()

    if (int(values[1]) < len(tests[int(values[0])].questions) - 1):
        tests[int(values[0])].LoadQuestion(bot,message, int(values[1]) + 1)
    else:
        defaultmessages.FinishTest(bot,message, values, tests)

    c.execute(f"""SELECT * FROM test{values[0]}""")
    db.close()

# ----------------------------------
def zapovedniki_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.Zapovedniki(bot,message)

def zapovednik_click(bot:telebot.TeleBot,message:Message,num:id):
    defaultmessages.LoadZapovednik(bot,message,num)
# ----------------------------------
def prazdniki_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.LoadPrazdniki(bot, message)

def prazdnik_globals_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.LoadPradnikGlobal(bot,message)
def prazdnik_days_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.LoadPrazdnikDays(bot, message)
def prazdnik_pamyat_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.LoadPrazdnikPamyat(bot, message)