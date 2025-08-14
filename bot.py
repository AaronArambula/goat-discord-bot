import discord
import requests
import json
import random
import requests

TENOR_KEY = ""

def get_lebron_gif():
    search_term = "LeBron James"
    limit = 10  # request more results for variety
    r = requests.get(
        f"https://tenor.googleapis.com/v2/search?q={search_term}&key={}&limit={limit}&media_filter=gif"
    )
    data = r.json()
    gifs = [result['media_formats']['gif']['url'] for result in data.get('results', [])]
    if gifs:
        return random.choice(gifs)
    return None
def get_diddy_lebron():
    return "https://c.tenor.com/fFkrubLxwwYAAAAC/tenor.gif"



def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
    if message.content.startswith('$lebron'):
      await message.channel.send(get_lebron_gif())
    if message.content.startswith('$goat'):
      await message.channel.send(get_lebron_gif())
    if message.content.startswith('$diddy'):
      await message.channel.send(get_diddy_lebron())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')
