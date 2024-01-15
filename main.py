import discord
from discord import *
from discord.ext import tasks, commands
import requests
from colorama import *
import asyncio
from pystyle import *
from time import *

client = discord.Client()
bot = commands.Bot(command_prefix="!", self_bot=True)

statuslist = ['11gn is cool', 'status changer https://github.com/11gn/discord-status-changer-py', 'new tools out soon', 'V1 OUT NOW!!!', "fork it if you would like", "give it a like to support "] #change this to wtv u like


async def change_status():
    while True:
        for status in statuslist:
            await client.change_presence(activity=discord.Game(name=status, url="https://github.com/11gn/discord-status-changer-py"))
            await asyncio.sleep(1)  

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(change_status())

startlogo = (f"""
             
             
             
       ______    __                  __                                 ______   __                                                         
 /      \  /  |                /  |                               /      \ /  |                                                        
/$$$$$$  |_$$ |_     ______   _$$ |_    __    __   _______       /$$$$$$  |$$ |____    ______   _______    ______    ______    ______  
$$ \__$$// $$   |   /      \ / $$   |  /  |  /  | /       |      $$ |  $$/ $$      \  /      \ /       \  /      \  /      \  /      \ 
$$      \$$$$$$/    $$$$$$  |$$$$$$/   $$ |  $$ |/$$$$$$$/       $$ |      $$$$$$$  | $$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |
 $$$$$$  | $$ | __  /    $$ |  $$ | __ $$ |  $$ |$$      \       $$ |   __ $$ |  $$ | /    $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
/  \__$$ | $$ |/  |/$$$$$$$ |  $$ |/  |$$ \__$$ | $$$$$$  |      $$ \__/  |$$ |  $$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ |$$$$$$$$/ $$ |      
$$    $$/  $$  $$/ $$    $$ |  $$  $$/ $$    $$/ /     $$/       $$    $$/ $$ |  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$       |$$ |      
 $$$$$$/    $$$$/   $$$$$$$/    $$$$/   $$$$$$/  $$$$$$$/         $$$$$$/  $$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$ | $$$$$$$/ $$/       
                                                                                                         /  \__$$ |                    
                                                                                                         $$    $$/                     
                                                                                                          $$$$$$/                              
  {"мα∂є ву 11gη"}
             
    This Is v1 So Uh If There Is Bugs Lmk       
             
             
             
             
             
             
    """)

# code/message here can be changed to watever you would like.

print(Colorate.Horizontal(Colors.blue_to_purple, startlogo))


client.run('TOKEN HERE', bot=False)

