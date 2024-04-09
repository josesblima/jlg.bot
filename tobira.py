import random
import discord

week1 = [('1', 'one'), ('2', 'two')]
new_question = True

class Tobira:

    def __init__(self):
        self.question = week1[random.randint(0, len(week1) - 1)]
    if active_quiz = 'tobira':
        qnum = 0
        anum = 1

    def tobfunc(self, message):
        global new_question
        p_message = message.content.lower()
        if (p_message == 'tobira'):
            return 'Write the word in hiragana:\n' + self.question[qnum]
        elif (p_message == self.question[anum]):
            if (new_question == True):
                self.question = week1[random.randint(qnum, len(week1) - anum)]
            return self.question[qnum]
        return
