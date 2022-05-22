import discord
import random


TOKEN = "OTUzMDE5NDEyODU0NzQzMDUw.GiUJfc.w6shx101VsLoiAr_D2UiaYWMHlh6mD1QRH9-4I"

client = discord.Client()

@client.event
async def on_ready():
    print("Ingelogd als {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_msg} ({channel})')

    if message.author ==client.user:
        return
    
    if message.channel.name == 'discord-bot':
        if user_msg.lower().split(" ")[0] == '!calculate':
            first_number = user_msg.split(" ")[1]
            second_number = user_msg.split(" ")[2]
            first_number_int = int(first_number)
            second_number_int = int(second_number)
            calculation = ((second_number_int - first_number_int) / first_number_int) * 100
            third_number = user_msg.split(" ")[3]
            third_number_int = int(third_number)
            profit_loss = (third_number_int * calculation) / 100
            if calculation > 0:
                await message.channel.send(f"Winst in procent = {round(calculation, 2)}% / winst in € = €{round(profit_loss, 2)}")
            elif calculation < 0:
                await message.channel.send(f"Verlies in procent: {round(calculation, 2)}% / verlies in € = €{round(profit_loss, 2)}")
            elif calculation == 0:
                await message.channel.send(f"Geen winst of verlies")
            return


client.run(TOKEN)
