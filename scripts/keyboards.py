from telebot import types
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import KeyboardButton
from telebot.types import ReplyKeyboardMarkup


def ToMainMenuKeyboard():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('В главное меню',callback_data='to_mainmenu')
    markup.add(but1)
    return markup

def GetGeoKeyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    but1 = KeyboardButton('Поиск', request_location=True)
    but2 = KeyboardButton('В главное меню')
    markup.add(but1)
    markup.add(but2)
    return markup

def DostoprimPageKeybord(page:int):
    markup = InlineKeyboardMarkup()
    match page:
        case 1:
            markup.row(InlineKeyboardButton('[1] Брестская крепость', callback_data='dostoprim_obj1'),
                       InlineKeyboardButton('[2] Беловежская пуща', callback_data='dostoprim_obj2'))
            markup.row(InlineKeyboardButton('[3] Каменецкая башня', callback_data='dostoprim_obj3'),
                       InlineKeyboardButton('[4] Ружанский замок', callback_data='dostoprim_obj4'))
            markup.row(InlineKeyboardButton('[5] Коссовский дворец', callback_data='dostoprim_obj5'),
                       InlineKeyboardButton('[6] Свято-Афанасьевский монастырь', callback_data='dostoprim_obj6'))
            markup.row(InlineKeyboardButton('[7] Кобринский парк им.Суворова', callback_data='dostoprim_obj7'),
                       InlineKeyboardButton('[8] Музей железнодорожной техники', callback_data='dostoprim_obj8'))
            markup.row(InlineKeyboardButton('[9] Спасо-Преображенский монастырь', callback_data='dostoprim_obj9'),
                       InlineKeyboardButton('[10] Музей Белорусского Полесья', callback_data='dostoprim_obj10'))
            markup.row(InlineKeyboardButton('Дальше', callback_data='dostoprim_page2'))
            markup.row(InlineKeyboardButton('В главное меню',callback_data='to_mainmenu'))
        case 2:
            markup.row(InlineKeyboardButton('[11] Музей природы Беловежской пущи', callback_data='dostoprim_obj11'),
                       InlineKeyboardButton('[12] Холмские ворота', callback_data='dostoprim_obj12'))
            markup.row(InlineKeyboardButton('[13] Музей обороны Брестской крепости', callback_data='dostoprim_obj13'),
                       InlineKeyboardButton('[14] Усадьба Немцевичей', callback_data='dostoprim_obj14'))
            markup.row(InlineKeyboardButton('[15] Музей народного творчества "Бездежский фартушок"', callback_data='dostoprim_obj15'),
                       InlineKeyboardButton('[16] Барановичский Парк животных', callback_data='dostoprim_obj16'))
            markup.row(InlineKeyboardButton('[17] Пинская набережная и речной порт', callback_data='dostoprim_obj17'),
                       InlineKeyboardButton('[18] Костел Сердца Иисуса', callback_data='dostoprim_obj18'))
            markup.row(InlineKeyboardButton('[19] Хмелёвский Спасо-Преображенский монастырь', callback_data='dostoprim_obj19'),
                       InlineKeyboardButton('[20] Кобринская синагога', callback_data='dostoprim_obj20'))
            markup.row(InlineKeyboardButton('Назад', callback_data='dostoprim_page1'),InlineKeyboardButton('Дальше', callback_data='dostoprim_page3'))
            markup.row(InlineKeyboardButton('В главное меню',callback_data='to_mainmenu'))
        case 3:
            markup.row(InlineKeyboardButton('[21] Костёл Пресвятой Девы Марии', callback_data='dostoprim_obj21'),
                       InlineKeyboardButton('[22] Музей космонавтики', callback_data='dostoprim_obj22'))
            markup.row(InlineKeyboardButton('[23] Озеро Каташи', callback_data='dostoprim_obj23'),
                       InlineKeyboardButton('[24] Дом-музей Адама Мицкевича', callback_data='dostoprim_obj24'))
            markup.row(InlineKeyboardButton('[25] Музей-усадьба им. Т. Костюшко', callback_data='dostoprim_obj25'),
                       InlineKeyboardButton('[26] Усадьба Котлубаев', callback_data='dostoprim_obj26'))
            markup.row(InlineKeyboardButton('[27] Форт V Брестской крепости', callback_data='dostoprim_obj27'),
                       InlineKeyboardButton('[28] Усадьба Бохвицей', callback_data='dostoprim_obj28'))
            markup.row(InlineKeyboardButton('[29] Жировицкая икона Божией Матери', callback_data='dostoprim_obj29'),
                       InlineKeyboardButton('[30] Собор святых Петра и Павла', callback_data='dostoprim_obj30'))
            markup.row(InlineKeyboardButton('Назад', callback_data='dostoprim_page2'))
            markup.row(InlineKeyboardButton('В главное меню', callback_data='to_mainmenu'))
        case _:
            markup.row(InlineKeyboardButton('В главное меню',callback_data='to_mainmenu'))
            
    return markup

def DostoprimObjKeybord(obj:int):
    global page
    markup = InlineKeyboardMarkup()
    back = str(obj-1)
    next = str(obj+1)
    
    if 10 >= obj > 0:page='1'
    elif 20 >= obj > 10:page='2'
    elif 30 >= obj > 20:page='3'

    if obj >= 30:
        markup.row(InlineKeyboardButton('Назад', callback_data=('dostoprim_obj'+back)))
        markup.row(InlineKeyboardButton('К списку', callback_data=('dostoprim_page' + page)),
                    InlineKeyboardButton('В главное меню', callback_data='to_mainmenu'))
    elif obj <= 1:
        markup.row(InlineKeyboardButton('Дальше', callback_data=('dostoprim_obj'+next)))
        markup.row(InlineKeyboardButton('К списку', callback_data=('dostoprim_page' + page)),
                    InlineKeyboardButton('В главное меню', callback_data='to_mainmenu'))
    elif obj > 1 & obj < 30:
        markup.row(InlineKeyboardButton('Назад', callback_data=('dostoprim_obj'+back)),
                    InlineKeyboardButton('Дальше', callback_data=('dostoprim_obj'+next)))
        markup.row(InlineKeyboardButton('К списку', callback_data=('dostoprim_page' + page)),
                    InlineKeyboardButton('В главное меню', callback_data='to_mainmenu'))
    
    return markup

def GetFaktsKeybord(fakt:int):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('В главное меню', callback_data='to_mainmenu')
    but2 = InlineKeyboardButton('Следующий факт', callback_data=f'load_fakt_{fakt+1}')
    but3 = InlineKeyboardButton('Случайный факт', callback_data=f'load_fakt_random')
    markup.row(but3,but2)
    markup.add(but1)
    return markup

def GetTestsKeybord():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Города достопримечательностей',callback_data='load_test_0')
    but2 = InlineKeyboardButton('Памятные даты и праздники',callback_data='load_test_1')
    but3 = InlineKeyboardButton('В главное меню', callback_data='to_mainmenu')
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    return markup

def GetZapovednikiKeyboard():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Березинский биосферный заповедник',callback_data='load_zapov_1')
    but2 = InlineKeyboardButton('Полесский государственный радиационно-экологический заповедник',callback_data='load_zapov_2')
    but3 = InlineKeyboardButton('Национальный парк «Беловежская пуща»',callback_data='load_zapov_3')
    but4 = InlineKeyboardButton('Нарочанский национальный парк',callback_data='load_zapov_4')
    but5 = InlineKeyboardButton('Национальный парк «Браславские озёра»',callback_data='load_zapov_5')
    but6 = InlineKeyboardButton('Припятский национальный парк',callback_data='load_zapov_6')
    markup.row(but1,but2)
    markup.row(but3,but4)
    markup.row(but5,but6)
    markup.add(InlineKeyboardButton('В главное меню',callback_data='to_mainmenu'))
    return markup
def GetZapovednikKeboard():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('В главное меню', callback_data='to_mainmenu')
    but2 = InlineKeyboardButton('К списку',callback_data='load_zapovedniki')
    markup.row(but1,but2)
    return markup

def GetPrazdnikiKeyboard():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('В главное меню', callback_data='to_mainmenu')
    but2 = InlineKeyboardButton('Государственные праздники', callback_data='load_prazdnik_globals')
    but3 = InlineKeyboardButton('Праздничные дни', callback_data='load_prazdnik_days')
    but4 = InlineKeyboardButton('Памятные дни', callback_data='load_prazdnik_pamyat')
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but1)
    return markup

def GetPrazdnikPageKeyboard():
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('В главное меню', callback_data='to_mainmenu')
    but2 = InlineKeyboardButton('К списку', callback_data='load_prazdniki')
    markup.row(but1,but2)
    return markup



mainMenuKeyboard = types.InlineKeyboardMarkup()
mainMenuKeyboard.add(types.InlineKeyboardButton('🏛 Достопримечательности',callback_data='main_button1'))
mainMenuKeyboard.add(types.InlineKeyboardButton('🗺 Ближайшая достопримечательность',callback_data='main_button2'))
mainMenuKeyboard.add(types.InlineKeyboardButton('📝 Тесты',callback_data='main_button3'))
mainMenuKeyboard.add(types.InlineKeyboardButton('❓ Факты',callback_data='load_fakt_0'))
mainMenuKeyboard.add(types.InlineKeyboardButton('🏞 Заповедники и нац. парки',callback_data='load_zapovedniki'))
mainMenuKeyboard.add(types.InlineKeyboardButton('🎆 Памятные даты и праздники',callback_data='load_prazdniki'))
mainMenuKeyboard.add(types.InlineKeyboardButton('📔 Общая информация',callback_data='main_button4'))