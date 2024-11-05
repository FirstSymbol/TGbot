import telebot.types
import telebot


class TestQuestion:
    id = 0
    text = 'Sample test text'
    correctAnswer:int = 1
    def __init__(self,id:int):
        self.id = id

class TestStartPage:
    text = str()
    keyboard:telebot.types.InlineKeyboardMarkup
    def __init__(self,text:str):
        self.text = text

class Test:
    name = str('Default Test')
    startPage:TestStartPage
    answers: list[int] = list()

    id:int
    questions:list[TestQuestion] = []

    def __init__(self,testID:int,questionCount:int,startPage:TestStartPage):
        self.id = testID
        for i in range(questionCount):
            self.questions.append(TestQuestion(i))
        self.startPosition = 0
        self.startPage = startPage
        self.CreateStartPageKeyboard()

    def CreateStartPageKeyboard(self):
        self.startPage.keyboard = telebot.types.InlineKeyboardMarkup()
        but1 = telebot.types.InlineKeyboardButton('В главное меню',callback_data='to_mainmenu')
        but2 = telebot.types.InlineKeyboardButton('Начать тест',callback_data=f'start_test_{self.id}_{0}')
        self.startPage.keyboard.row(but1,but2)

    def CreateQuestionKeyboard(self,questionID:int):
        questionKeyboard = telebot.types.InlineKeyboardMarkup()
        but1 = telebot.types.InlineKeyboardButton('а', callback_data=f'answer_test_{self.id}_{questionID}_{1}_{self.questions[questionID].correctAnswer}')
        but2 = telebot.types.InlineKeyboardButton('б', callback_data=f'answer_test_{self.id}_{questionID}_{2}_{self.questions[questionID].correctAnswer}')
        but3 = telebot.types.InlineKeyboardButton('в', callback_data=f'answer_test_{self.id}_{questionID}_{3}_{self.questions[questionID].correctAnswer}')
        but4 = telebot.types.InlineKeyboardButton('г', callback_data=f'answer_test_{self.id}_{questionID}_{4}_{self.questions[questionID].correctAnswer}')
        questionKeyboard.row(but1,but2,but3,but4)
        return questionKeyboard

    def LoadTest(self,bot:telebot.TeleBot,message:telebot.types.Message):
        bot.edit_message_text(text=self.startPage.text,
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=self.startPage.keyboard)
        print(f'Тест №{self.id} загружен')



    def LoadQuestion(self,bot:telebot.TeleBot,message:telebot.types.Message,questionID:int):
        bot.edit_message_text(text=self.questions[questionID].text,
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=self.CreateQuestionKeyboard(questionID))

    def GetAnswerInfo(self):
        result = 0
        for answer in self.answers:
            result += answer
        return result




    def print(self):
        for quest in range(len(self.questions)):
            print(self.questions[quest].id)
