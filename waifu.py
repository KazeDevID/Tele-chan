import telebot
from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv('TOKEN', '6859521411:AAETjm2VNCGBfIFWXrfa8IF6VKeHzSf4D88')

bot = telebot.TeleBot(token)

# Let's define stuff
def get_url():
    contents = requests.get('https://api.waifu.pics/sfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_nekourl():
    contents = requests.get('https://api.waifu.pics/sfw/neko').json()
    image_url = contents['url']
    return image_url


def get_shinobuurl():
    contents = requests.get('https://api.waifu.pics/sfw/shinobu').json()
    image_url = contents['url']
    return image_url

def get_meguminurl():
    contents = requests.get('https://api.waifu.pics/sfw/megumin').json()
    image_url = contents['url']
    return image_url

def get_kissurl():
    contents = requests.get('https://api.waifu.pics/nsfw/trap').json()
    image_url = contents['url']
    return image_url

def get_lickurl():
    contents = requests.get('https://api.waifu.pics/nsfw/blowjob').json()
    image_url = contents['url']
    return image_url

def get_nwaifuurl():
    contents = requests.get('https://api.waifu.pics/nsfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_lewdurl():
    contents = requests.get('https://nekos.life/api/v2/img/lewd').json()
    image_url = contents['url']
    return image_url



@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hey there, I'm Tele-chan 💖
     I can fetch hottest anime and hentai images & send them to you
     Send /help to check the commands out. '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['ping'])
def greet(message):
    msg = ''' I'm alive :3 '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['repo'])
def greet(message):
    msg = ''' Repository Link -> https://github.com/KazeDevID/Tele-chan/ '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['source'])
def greet(message):
    msg = ''' Source Code -> https://github.com/KazeDevID
              Author -> @KenalSayaaa '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['help'])
def help(message):
    msg = ''' Here are the commands :

    SFW Commands :
    /waifu
    /neko
    /shinobu
    /megumin

    NSFW Commands :
    /trap
    /blowjob
    /lewd

    Other Commands :
    /ping
    /repo
    /source
    '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['waifu'])
@bot.message_handler(regexp=r'waifu')
def waifu(message):
    url = get_url()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['neko'])
@bot.message_handler(regexp=r'neko')
def neko(message):
    url = get_nekourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['shinobu'])
@bot.message_handler(regexp=r'shinobu')
def shinobu(message):
    url = get_shinobuurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['megumin'])
@bot.message_handler(regexp=r'megumin')
def megumin(message):
    url = get_meguminurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['trap'])
@bot.message_handler(regexp=r'trap')
def kiss(message):
    url = get_kissurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['blowjob'])
@bot.message_handler(regexp=r'blowjob')
def lick(message):
    url = get_lickurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['lewd'])
@bot.message_handler(regexp=r'lewd')
def lewd(message):
    url = get_lewdurl()
    bot.send_photo(message.chat.id, url)




def main():
    bot.polling()

if __name__ == '__main__':
    main()
