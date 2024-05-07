import sqlite3

class Database:
    def __init__(self):
        self.database = sqlite3.connect('userdata.db')
        self.cursor = self.database.cursor()

    # self.cursor.execute('''CREATE TABLE IF NOT EXISTS levels(user_id TEXT, xp INTEGER, level INTEGER, zeni INTEGER)''')
    # self.cursor.execute('INSERT INTO levels VALUES("qwe", 11, 111, 111)')
    # self.database.commit()


    def xpgold_update(self, user_name, xp, zeni):
        self.check_create_user(user_name)
        self.cursor.execute(f'UPDATE levels SET xp = xp + {xp} WHERE user_id = "{user_name}"')
        self.database.commit()
        self.cursor.execute(f'UPDATE levels SET zeni = zeni + {zeni} WHERE user_id = "{user_name}"')
        self.database.commit()
        self.cursor.execute(f'SELECT * FROM levels WHERE user_id = "{user_name}"')
        pdata = self.cursor.fetchone()
        return f'Genius! You have gained {xp} xp and {zeni} 銭(zeni).\n{pdata[0]} - {pdata[1]} xp - {pdata[-1]} 銭'


    def player_data(self, user_id):
        self.cursor.execute(f'SELECT * FROM levels WHERE user_id = "{user_id}"')
        pdata = self.cursor.fetchone()
        return '‎\n' + 'Player: ' + pdata[0] + '\nxp: ' + str(pdata[1]) + ' lvl: ' + str(pdata[2]) + ' 銭(zeni): ' + str(pdata[3])


      #Check if user is in db, if not, insert it
    def check_create_user(self, user_id):
        self.cursor.execute(f'SELECT (user_id) FROM levels WHERE user_id = "{user_id}"')
        user_ids = self.cursor.fetchall()
        user_exists = False
        for x in user_ids:
            if x[0] == user_id:
                print('it fookin worked m9')
                user_exists = True
                break

        if user_exists != True:
            self.cursor.execute(f'INSERT INTO levels Values("{user_id}", 0, 0, 0)')
            self.database.commit()



           




#cursor.execute('''CREATE TABLE IF NOT EXISTS levels(user_id TEXT, xp INTEGER, level INTEGER, last_level INTEGER)''')

#cursor.execute('INSERT INTO levels VALUES("qwe", 11, 111, 111)')
#database.commit()

#import nextcord
#from nextcord.ext import commands
# import vacefron
# import math
# import random
# import sqlite3

# database = sqlite3.connect('database.sqlite')
# cursor = database.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS levels(user_id TEXT, xp INTEGER, level INTEGER, last_level INTEGER)''')

# class Leveling(commands.Cog):
    
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.Cog.listener()
#     async def on_message(self, message):

#         if message.author.bot:
#             return
        
#         cursor.execute(f'SELECT user_id, xp, level, last_level FROM levels WHERE user_id = {message.author.id}')
#         result = cursor.fetchone()
#         if result is None:

#             cursor.execute(f'INSERT INTO levels(user_id, xp, level, last_level) VALUES({message.author.id})')
#             database.commit()

#         else:

#             xp = result[1]
#             lvl = result[2]
#             last_level = result[3]

#             xp_gained = random.randint(1,20)
#             xp += xp_gained
#             lvl = 0.1*(math.sqrt(xp))

#             cursor.execute(f'UPDATE levels SET xp = {xp}, level = {lvl} WHERE user_id = {message.author.id}')

#             if int(lvl) > last_level:
#                 await message. channel.send(f'{message.author.mention} has leveled up to level {int(lvl)}!')
#                 database.commit()



# def setup(bot):
#     bot.add_cog(Leveling(bot))
# import sqlite3
# class Datahandler():
#     def __init__(self):
#         conn = sqlite3.connect('userdata.db')

#         self.c = conn.cursor()

#         print("Successfully Connected to SQLite")

#         sqlite_insert_query = '''INSERT INTO userdata
#                             (id, xp)
#                             VALUES
#                             ('kafka4x', 0)'''

#         count = self.c.execute(sqlite_insert_query)
#         sqliteConnection.commit()
#         print("Record inserted successfully into SqliteDb_developers table ", self.c.rowcount)
#         conn.close()
#         user_data = []

#         #cur.execute(userdata(userid TEXT, XP INTEGER))
#         conn.commit()
#         conn.close()
#     #def xpgain():
