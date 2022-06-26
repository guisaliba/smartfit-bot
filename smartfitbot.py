import tweepy
import time
import datetime

client = tweepy.Client(consumer_key='JI5kIiurU2b4cNkZiwZZJXaou',
                       consumer_secret='JwRMT3D5aCqbAYWVobQZCuHw659FA2CcZYkImgcIHi3t6MHJzC',
                       access_token='1524542526279016451-ZtHfTK7s1XggPacyL0RnSzVAF12ZUJ',
                       access_token_secret='4v2D6Yo33F7z48U6bYhImkptSwa7BZOOWnVfSQbpZzh2W')

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

    return f"O armário 53 da SmartFit está ocupado há {resultdate.days} dias {suffix}"


def write():
  client.create_tweet(text = tweet())    

while True:
  try:
    write()
    time.sleep(60)
  except:
    print("Estou em cooldown...")
    time.sleep(60)
