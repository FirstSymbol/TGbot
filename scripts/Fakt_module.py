import telebot
from telebot import TeleBot
from telebot.types import Message

import keyboards


class Fakt:
    text:str = 'Default text'
    id:int = 0
    def LoadFakt(self, bot:TeleBot,message:Message):
        if message.photo:
            chatID:int = message.chat.id
            bot.delete_message(chat_id=chatID,
                               message_id=message.message_id)
            bot.send_message(text=self.text,
                             chat_id=message.chat.id,
                             reply_markup=keyboards.GetFaktsKeybord(self.id))
        else:
            bot.edit_message_text(text=self.text,
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.GetFaktsKeybord(self.id))
    #
