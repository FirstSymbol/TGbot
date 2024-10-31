import telebot
import defaultmessages
import keyboards
from telebot import types
from telebot.types import Message
from telebot.types import CallbackQuery

def mainMenu_button1_click(bot:telebot.TeleBot,message:Message):
    dostoprim_page1_click(bot,message)
    
def mainMenu_button2_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('Нажата кнопка 2',message.chat.id,message.message_id, reply_markup=keyboards.ToMainMenuKeyboard())

def mainMenu_button3_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('Нажата кнопка 3',message.chat.id,message.message_id, reply_markup=keyboards.ToMainMenuKeyboard())

def mainMenu_button4_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('Нажата кнопка 4',message.chat.id,message.message_id, reply_markup=keyboards.ToMainMenuKeyboard())

def dostoprim_page1_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('🏛| Достопримечательности Бресткой области [1 / 4]',message.chat.id,message.message_id, reply_markup=keyboards.DostoprimPageKeybord(1))

def dostoprim_page2_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('🏛| Достопримечательности Бресткой области [2 / 4]',message.chat.id,message.message_id, reply_markup=keyboards.DostoprimPageKeybord(2))
    
def dostoprim_page3_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('🏛| Достопримечательности Бресткой области [3 / 4]',message.chat.id,message.message_id, reply_markup=keyboards.DostoprimPageKeybord(3))
    
def dostoprim_page4_click(bot:telebot.TeleBot,message:Message):
    bot.edit_message_text('🏛| Достопримечательности Бресткой области [4 / 4]',message.chat.id,message.message_id, reply_markup=keyboards.DostoprimPageKeybord(4))
    
def dostoprim_obj_click(bot:telebot.TeleBot,message:Message,obj_id:int):
    defaultmessages.EditDostoprimObj(bot,message,obj_id)
    
def toMainMenu_click(bot:telebot.TeleBot,message:Message):
    defaultmessages.EditMainMenu(bot,message)