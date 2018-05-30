from chatterbot import ChatBot

bot = ChatBot('My Chat')
from chatterbot.trainers import ListTrainer

bot.set_trainer(ListTrainer)
F = open(r'D:\Training\log\chatlog.txt')
conv = F.readlines()
F.close()
bot.train(conv)

while True:
    try:
        s = input('you:')
        r = bot.get_response(s)
        print('response =', r)
    except:
        break
