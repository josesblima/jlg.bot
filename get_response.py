import discord
from tobira import Tobira

active_quiz = ''
reply = None
question = None
instance = None
def  get_response(message):
    global instance
    global active_quiz
    p_message = message.content.lower()

    if (p_message == 'hi'):
        return 'Hello!'
    if (p_message == 'tobira'):
        active_quiz = 'tobira'
        instance = Tobira()
    if (active_quiz == 'tobira'):
        return instance.tobfunc(message), active_quiz



