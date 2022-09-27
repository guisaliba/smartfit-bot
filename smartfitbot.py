import tweepy
import time
import datetime

client = tweepy.Client(consumer_key='INSERT-YOUR-CONSUMER-KEY',
                       consumer_secret='INSERT-YOUR-CONSUMER-SECRET',
                       access_token='INSERT-YOUR-ACESS-TOKEN',
                       access_token_secret='INSERT-YOUR-ACESS-TOKEN-SECRET')

def tweet():
    firstdate = '25/05/2022'
    resultdate = (datetime.datetime.now() - datetime.timedelta(hours=3)) - datetime.datetime.strptime(firstdate, '%d/%m/%Y')
    hours = (resultdate.seconds / 60) / 60
    hoursStr = str(hours)

    if hours >= 1 and hours < 2:
        suffix = f"e {hoursStr[:1]} hora"
    elif hours > 1 and hours < 10:
        suffix = f"e {hoursStr[:1]} horas"
    elif hours > 10:
        suffix = f"e {hoursStr[:2]} horas"
    else:
        suffix = ""

    return f"Esse armário está ocupado há {resultdate.days} dias {suffix}"


def write():
  client.create_tweet(text = tweet())    

while True:
  try:
    write()
    time.sleep(60)
  except:
    print("Estou em cooldown...")
    time.sleep(60)
