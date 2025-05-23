from dotenv import load_dotenv
import os

load_dotenv()


bot_prefix = str(os.getenv('BOT_PREFIX'))
bot_token = str(os.getenv('BOT_TOKEN')) or 'your bot token'


# NODE INFO
host = str(os.getenv('NODE_HOST')) or 'localhost'
port = int(os.getenv('NODE_PORT')) or 2333
password = str(os.getenv('NODE_PASSWORD')) or 'youshallnotpass'
secure = str(os.getenv('NODE_SECURE')) or 'false'
if secure == 'true':
    print('Secure is true')
    secure = True
else:
    print('Secure is false')
    secure = False

# COGS

music = os.getenv('MUSIC')
moderation = os.getenv('MODERATION')
general = os.getenv('GENERAL')
giveaway = os.getenv('GIVEAWAY')
support = os.getenv('SUPPORT')

#add conditions for cogs
if music == 'true':
    music = True
else:
    music = False

if moderation == 'true':
    moderation = True
else:
    moderation = False

if general == 'true':
    general = True
else:
    general = False

if giveaway == 'true':
    giveaway = True
else:
    giveaway = False

if support == 'true':
    support = True
else:
    support = False
