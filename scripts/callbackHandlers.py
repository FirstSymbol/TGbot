import telebot
from telebot.types import Message

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
def start_test_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.TestingMessages(bot,message,1)