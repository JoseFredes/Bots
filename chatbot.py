from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.response_selection import get_most_frequent_response

miBot = ChatBot(name = 'Botsito', read_only = True,
                preprocessors=['chatterbot.preprocessors.clean_whitespace'],
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                'chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter'
                ]
                )

trainer = ChatterBotCorpusTrainer(miBot)


trainer.train(
    "chatterbot.corpus.spanish.conversations",
    "chatterbot.corpus.spanish.dinero",
    "chatterbot.corpus.spanish.emociones",
    "chatterbot.corpus.spanish.greetings",
    "chatterbot.corpus.spanish.IA",
    "chatterbot.corpus.spanish.perfilbot",
    "chatterbot.corpus.spanish.psicologia"
)

#Entrenamiento = ListTrainer(miBot)
# for item in ( Problema1, Probelma2):
#           Entrenamiento.train(item)
          
        
print(" Hola, soy Botsito")
while True:
    try:
        bot_imput = miBot.get_response(input())
        print(bot_imput)

    except(KeyboardInterrupt,EOFError,SystemExit):
        break