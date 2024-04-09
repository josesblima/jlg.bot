import random
import discord

week1 = [('1', 'one'), ('2', 'two')]
new_question = True

class Tobira:

    def __init__(self):
        self.question = week1[random.randint(0, len(week1) - 1)]

    def tobfunc(self, message):
        global new_question
        p_message = message.content.lower()
        print('p_message = ' + p_message)
        print('self.question = ' + self.question[0])
        if (p_message == 'tobira'):
            return 'Write the word in hiragana:\n' + self.question[0]
        elif (p_message == self.question[1]):
            print('heyo')
            if (new_question == True):
                self.question = week1[random.randint(0, len(week1) - 1)]
            return self.question[0]
        return
