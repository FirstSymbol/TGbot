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
    if (values[2] == values[3]):
        print('Верный ответ')
        tests[int(values[0])].answers.append(1)
    else:
        tests[int(values[0])].answers.append(0)
        print('Не верный ответ')
    if (int(values[1]) < len(tests[int(values[0])].questions) - 1):
        tests[int(values[0])].LoadQuestion(bot,message, int(values[1]) + 1)
    else:
        defaultmessages.FinishTest(bot,message, values, tests)
# ----------------------------------
def zapovedniki_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.Zapovedniki(bot,message)

def zapovednik_click(bot:telebot.TeleBot,message:Message,num:id):
    defaultmessages.LoadZapovednik(bot,message,num)
# ----------------------------------
def prazdniki_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.LoadPrazdniki(bot, message)