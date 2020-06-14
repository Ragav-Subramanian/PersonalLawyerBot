from chatterbot import ChatBot

chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. ',
            'maximum_similarity_threshold': .90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_law100 = open('training_data/f100.txt',encoding="utf-8").read().splitlines()
training_data_400 = open('training_data/400l.txt').read().splitlines()
training_data_500 = open('training_data/ipcc.txt').read().splitlines()
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_law100 + training_data_400 + training_data_500 + training_data_quesans + training_data_personal

trainer.train(training_data)

