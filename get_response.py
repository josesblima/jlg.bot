from quiz import Quiz
from questions import Questions
from database import Database
from jisho import Jisho

class Responder:
    def __init__(self):
        self.quiz_active_bool = False
        self.quiz_instance = None
        self.dictionary = Jisho()
    async def get_response(self, message):
        p_message = message.content.lower()

        if (p_message[:2] == '??'):
            print('if statement - p_message[:2] == ??\n')
            return self.dictionary.jisho(message)

        if (p_message == 'help'):
            return "Welcome to the JLG.BOT!\nYou can use the following commands:\nhelp - brings up this menu\nn5 - starts the n5 quiz (works for all other jlpt levels)\nskip - skips question\nendquiz - ends quiz\n??辞書 - searches the word after the ?? on jisho.org\nstats - checks your stats\n"
        elif (p_message == 'stats'):
            db = Database()
            return db.player_data(message.author)
        
        elif (self.quiz_active_bool == True): 
            if(p_message == 'endquiz'):
                print('get_response endquiz\n')
                self.quiz_active_bool = False
                self.quiz_instance.end_quiz()
                self.quiz_instance = None
                return "The quiz was successfully terminated"
        
            print("quiz handler being called from get_response\n")
            return await self.quiz_instance.quiz_handler(message)

        elif (self.quiz_active_bool != True):
            if (p_message == 'n5' or p_message == 'n4' or p_message =='n3' or p_message == 'n2' or p_message == 'n1'):
                # Callfunction to start Quiz
                print("It's starting one  of the nquizzes\n")
                self.quiz_active_bool = True
                self.quiz_instance = Quiz()
                return self.quiz_instance.quiz_starter(message)
