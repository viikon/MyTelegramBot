import random
import time
import sys
import telebot
from telebot import types
from TOKEN import NEW_TOKEN

HELP = 'This is a rock-paper-scissors game. To play, choose one of the buttons: rock, paper, scissors, lizard, or spock.'
TOKEN = NEW_TOKEN


class RPSGame:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.score = 1

    def run(self):
        @self.bot.message_handler(commands=["help"])
        def help(message):
            self.bot.send_message(message.chat.id, HELP)

        @self.bot.message_handler(commands=["exit"])
        def exit(message):
            self.bot.send_message(message.chat.id, 'Пока, спасибо за игру!')
            sys.exit(0)

        @self.bot.message_handler(commands=['start'])
        def start(message: types.Message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('КАМЕНЬ')
            btn2 = types.KeyboardButton('НОЖНИЦЫ')
            btn3 = types.KeyboardButton('БУМАГА')
            btn4 = types.KeyboardButton('ЯЩЕРИЦА')
            btn5 = types.KeyboardButton('СПОК')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            self.bot.send_message(message.from_user.id, 'Выбери конпку с командой: / КАМЕНЬ / НОЖНИЦЫ / БУМАГА / ЯЩЕРИЦА / СПОК ', reply_markup=markup)

        @self.bot.message_handler(content_types=["text"])
        def game(message):
            if self.score > 0:
                if message.text == 'КАМЕНЬ':
                    self.bot.send_message(message.chat.id, 'КАМЕНЬ ПРОТИВ...')
                elif message.text == 'НОЖНИЦЫ':
                    self.bot.send_message(message.chat.id, 'НОЖНИЦЫ ПРОТИВ...')
                elif message.text == 'БУМАГА':
                    self.bot.send_message(message.chat.id, 'БУМАГА ПРОТИВ...')
                elif message.text == 'ЯЩЕРИЦА':
                    self.bot.send_message(message.chat.id, 'ЯЩЕРИЦА ПРОТИВ...')
                elif message.text == 'СПОК':
                    self.bot.send_message(message.chat.id, 'СПОК ПРОТИВ...')

                time.sleep(0.25)
                self.bot.send_message(message.chat.id, 'раз...')
                time.sleep(0.25)
                self.bot.send_message(message.chat.id, 'два...')
                time.sleep(0.5)
                self.bot.send_message(message.chat.id, 'три...')

                choice_list = ['КАМЕНЬ', 'НОЖНИЦЫ', 'БУМАГА', 'ЯЩЕРИЦА', 'СПОК']
                computer_move = random.choice(choice_list)
                self.bot.send_message(message.chat.id, computer_move)
                time.sleep(0.5)

                if message.text == computer_move:
                    self.bot.send_message(message.chat.id, 'Ничья...')
                    self.ties += 1
                elif (message.text == 'КАМЕНЬ' and computer_move == 'НОЖНИЦЫ') or \
                     (message.text == 'НОЖНИЦЫ' and computer_move == 'БУМАГА') or \
                     (message.text == 'БУМАГА' and computer_move == 'КАМЕНЬ') or \
                     (message.text == 'КАМЕНЬ' and computer_move == 'ЯЩЕРИЦА') or \
                     (message.text == 'ЯЩЕРИЦА' and computer_move == 'СПОК') or \
                     (message.text == 'СПОК' and computer_move == 'НОЖНИЦЫ') or \
                     (message.text == 'НОЖНИЦЫ' and computer_move == 'ЯЩЕРИЦА') or \
                     (message.text == 'ЯЩЕРИЦА' and computer_move == 'БУМАГА') or \
                     (message.text == 'БУМАГА' and computer_move == 'СПОК') or \
                     (message.text == 'СПОК' and computer_move == 'КАМЕНЬ'):
                    self.bot.send_message(message.chat.id, 'Вы выиграли!')
                    self.wins += 1
                    self.score += 1
                else:
                    self.bot.send_message(message.chat.id, 'Вы проиграли!')
                    self.losses += 1
                    self.score -= 1


                self.bot.send_message(message.chat.id, f'Осталось жизней: {self.score}')
                if self.score == 0:
                    self.bot.send_message(message.chat.id, 'Вы проиграли все жизни!')
                    self.bot.send_message(message.chat.id, 'Пока, спасибо за игру!')
                    #sys.exit(0)
                elif self.score >= 3:
                    self.bot.send_message(message.chat.id, 'Ты выиграл и стал почти бессмертным)))')
                    self.bot.send_message(message.chat.id, 'Пока, спасибо за игру!')
                    #sys.exit(0)

        self.bot.polling(none_stop=True)


game = RPSGame(TOKEN)
game.run()
