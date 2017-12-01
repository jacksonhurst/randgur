import discord
import asyncio
import imguralbum
import os
import random
import shutil

client = discord.Client()


@client.event
async def on_ready():
    print("Bot online") 

@client.event
async def on_message(message):
    if message.content.startswith('!randgur'):
        if not os.path.exists('test'):
            os.makedirs('test')
        while os.listdir('test') == []:
            try:
                keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                key = ''
                j = 0
                while j == 0:
                    try:
                        for i in range(0,5):
                            k = random.randrange(0,61)
                            key += keys[k]
                        newurl = 'https://imgur.com/gallery/' + key
                        downloader = imguralbum.ImgurAlbumDownloader(newurl)
                        j = 1
                    except:
                        key = ''
                        continue

                cwd = os.getcwd()
                downloader.save_images()

            except:
                continue
        
        i = random.choice(os.listdir('test'))
        await client.send_file(message.channel, "test\\" + i)
        shutil.rmtree('test')
    if message.content.startswith('!rhelp'):
        await client.send_message(message.channel, 'Created by Jackson Hurst\n\nTo generate a random image from imgur, simply type !randgur, wait a few seconds, and an image should send!')
client.run('ENTER TOKEN HERE')
