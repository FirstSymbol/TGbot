import telebot
import keyboards
from telebot import types
from telebot.types import Message
from telebot import TeleBot
from telebot.types import CallbackQuery

def SendMainMenu(bot:TeleBot,message:Message):
    bot.send_message(message.chat.id,'📋| Главное меню:', reply_markup=keyboards.mainMenuKeyboard)

def MessageNotFounded(bot:TeleBot,message:Message):
    bot.send_message(text='❌| Данная команда не найдена. Обратитесь к меню.', chat_id=message.chat.id, reply_markup=keyboards.ToMainMenuKeyboard())

def EditMainMenu(bot:TeleBot,message:Message):
    bot.edit_message_text('📋| Главное меню:',message.chat.id,message.message_id,reply_markup=keyboards.mainMenuKeyboard)
    
def EditDostoprimObj(bot:TeleBot,message:Message,obj_id:int):
    match obj_id:
        case 1:
            bot.edit_message_text(text='Объект 1',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 2:
            bot.edit_message_text(text='Объект 2',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 3:
            bot.edit_message_text(text='Объект 3',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 4:
            bot.edit_message_text(text='Объект 4',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 5:
            bot.edit_message_text(text='Объект 5',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 6:
            bot.edit_message_text(text='Объект 6',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 7:
            bot.edit_message_text(text='Объект 7',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 8:
            bot.edit_message_text(text='Объект 8',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 9:
            bot.edit_message_text(text='Объект 9',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case 10:
            bot.edit_message_text(text='Объект 10',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.DostoprimObjKeybord(obj_id))
        case _:
            pass