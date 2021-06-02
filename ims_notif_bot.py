from time import sleep
import discord
import requests
import os
from bs4 import BeautifulSoup

client = discord.Client()

useless_notice_1 = "GO TO NSUTIMS LOGIN PAGE"
useless_notice_2 = "Daily Biometric Attendance"
notice = "Practical Examination date  sheet for BE 8th  Sem MPAE/ ME Even Sem 2021( DU- CBCS)"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client:
        return

    if message.content.startswith('$notice'):
        await message.channel.send("Started")
        # print(notice)
        while True:
            r = requests.get(
                'https://www.imsnsit.org/imsnsit/notifications.php')
            src = r.content
            soup = BeautifulSoup(src)
            links = soup.find_all("a")
            flag = False
            new_notice = ""
            global notice
            for link in links:
                print(link.text)
                if (link.text == useless_notice_2) or (link.text == useless_notice_1):
                    continue
                if (link.text != notice):
                    await message.channel.send(link.text)
                    await message.channel.send(link['href'])
                    if flag == False:
                        new_notice = link.text
                        flag = True
                else:
                    break
            if new_notice == "":
                await message.channel.send("No new notice")
            else:
                notice = new_notice
            sleep(10)

client.run('TOKEN')
