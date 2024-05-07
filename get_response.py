from quiz import Quiz
from tobira import Tobira
from database import Database

class Responder:
    def __init__(self):
        self.quiz_active_bool = False
        self.quiz_instance = None
    async def get_response(self, message):
        p_message = message.content.lower()

        if (p_message == 'help'):
            return "Welcome to the JLG.BOT!\nYou can use the following commands:\nhelp - brings up this menu\ntobira - starts the tobira quiz\nskip - skips question\nstats - checks your stats\n"
        elif (p_message == 'stats'):
            db = Database()
            return db.player_data(message.author)
        elif (self.quiz_active_bool == True):
            print("get_response first if\n")
            return await self.quiz_instance.quiz_handler(message)

        elif (self.quiz_active_bool != True):
            if (p_message == 'tobira'):
                # Callfunction to start Quiz
                print("tobira did this print???\n")
                self.quiz_active_bool = True
                self.quiz_instance = Quiz()
                return self.quiz_instance.quiz_starter(message)
