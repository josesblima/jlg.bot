import discord
from key import KEY
import os
from get_response import get_response
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)
tobira_timer = False
winners = set() #hash set
winners_print = ''
final_winners = {} # dictionary
final_winners_print = ''
new_question = True
winner = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global tobira_timer, winners, new_question, winners_print, score_dic, final_winners, winner
    if message.author == client.user:
        return
    response, quiz = get_response(message)
    print(quiz)
    if (quiz == 'tobira' and message.content != 'tobira'):
        if (tobira_timer == False):
            winners = set()
            tobira_timer = True
            winners.add(message.author.name)
            if final_winners[message.author.name] >= 3:
                winner = True
            else:
                final_winners[message.author.name] = 1
            await asyncio.sleep(1)
            tobira_timer = False
            new_question = True
            if (response != None):
                winn:winners_printers_print = ''
                for x in winners:
                    winners_print += '\n' + x
                if winner == True:
                    final_winners_print = ''
                    for x in reversed(final_winners.items()):
                        final_winners_print += '\n' + x[0] + ' - ' + x[1] + 'points'
                    await message.channel.send('GAME OVER\n' + final_winners_print + 'congrats!')
                    winner = False
                    final_winners = {}
                    winners = set()
                    winners_print = ''
                else:
                    await message.channel.send('Correct!' + winners_print + '\ngot it right!\n' + response)
        elif (tobira_timer == True):
            print('tobira timer = true')
            winners.add(message.author.name)
            return
    #if response is discord.Embed or isinstance(response, discord.Embed):
    #    await message.channel.send(embed = response)
    else:
        await message.channel.send(response)
client.run(KEY)
