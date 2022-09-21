import os
import logging
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import random
from dalle2 import Dalle2


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

API_KEY = os.environ['API_KEY']
DALLE_TOKEN = os.environ['DALLE_TOKEN']
dalle = Dalle2(DALLE_TOKEN);

def no_entendi(update, context):
  #update.message.reply_text("Qué decis walter? No se entiende.")
  # Send photo
  update.message.reply_photo("https://pbs.twimg.com/media/D697a1EW0AAoGFy.jpg")

def dolar(update, context):
  res = requests.get('https://criptoya.com/api/dolar')
  data = res.json()
  response = f"Precio del Dolar {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n*Dolar Oficial*: ${data['oficial']}\n*Dolar Solidario*: ${data['solidario']}\n*Dolar Blue*: ${data['blue']}\n*Dolar MEP*: ${data['mep']}\n*Dolar CCL*: ${data['ccl']}"
  update.message.reply_text(response, parse_mode='Markdown')

def peso(update, context):
  update.message.reply_photo("https://imgs.search.brave.com/sBgon1V77usyhio-5ulkjFxQCxDvmwSLh-BL-DhKDFg/rs:fit:400:400:1/g:ce/aHR0cHM6Ly9wYnMu/dHdpbWcuY29tL3By/b2ZpbGVfaW1hZ2Vz/LzEzNzA1MjAyODUx/MzMzNDg4NjgvTWdu/SWhSb3cuanBn")

def albondiga_magica(update, context):
  rnd = random.randint(0, 100)
  if rnd < 30:
    update.message.reply_text("Si")
  elif rnd < 50:
    update.message.reply_text("No")
  elif rnd < 60:
    update.message.reply_text("Tal vez")
  elif rnd < 70:
    update.message.reply_text("Mirá flaco, con esa pregunta yo mejor te recomiendo que te replantees la existencia")
  elif rnd < 80:
    update.message.reply_text("JAJJAJAJAJJAJAJ")
  elif rnd < 90:
    update.message.reply_text("No se, yo solo se que Alee es Crack")
  else:
    update.message.reply_text("Andá a cagar :)")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def massa(update, context):
  base_prompt = "Massa: Hola! Yo soy Sergio Massa, actual Super Ministro de Economía de la República Argentina.\n"
  base_prompt += "Vengo en reemplazo de Silvina Batakis, una mujer medio rara que asumió después del pelado Guzmán.\n"
  base_prompt += "El presidente actualmente es Alberto Fernandez y la Vicepresidente es Cristina Kirchner.\n"
  base_prompt += "Yo soy una persona que se identifica con la centro-izquierda pero a veces puedo responder como una persona de derecha.\n"
  base_prompt += "Hazme una pregunta...\n"
  base_prompt += "Yo: " + update.message.text.split('/massa')[-1] + "\n"
  base_prompt += "Massa: "
  print(update.message.text.split('/massa')[-1])

  res = requests.post('https://api.usegrand.com/generate', headers = {
    'x-auth-key': os.environ['USEGRAND_AUTH_KEY'],
    'x-auth-secret': os.environ['USEGRAND_AUTH_SECRET']
  }, json = {
    "text": base_prompt.rstrip(),
    "model_id": "Ukg1ClHdlG03aG7cAu8J",
    "creativity": 30,
    "stop": "<newline>",
    "max": 100,
    "only_response": True
  })
  print(res.text)
  data = res.json()
  print(data)
  if(data['ok']):
    response = data['data']['text']
    update.message.reply_text(response)
    return
  update.message.reply_text("Perdón loco, no puedo responder eso, me llamó Macri y ahora soy de JxC")

def massa_yankee(update, context):

  base_prompt = "Massa: Hi!. I'm Sergio Massa. Current Minister of Economy of Argentina.\n"
  base_prompt += "Ask me a question...\n"
  base_prompt += "Me: " + update.message.text.split('/massa_yankee')[-1] + "\n"
  base_prompt += "Massa: "

  res = requests.post('https://api.usegrand.com/generate', headers = {
    'x-auth-key': os.environ['USEGRAND_AUTH_KEY'],
    'x-auth-secret': os.environ['USEGRAND_AUTH_SECRET']
  }, json = {
    "text": base_prompt.rstrip(),
    "model_id": "Ukg1ClHdlG03aG7cAu8J",
    "creativity": 30,
    "stop": "<newline>",
    "max": 100,
    "only_response": True
  })
  print(res.text)
  data = res.json()
  print(data)
  if(data['ok']):
    response = data['data']['text']
    update.message.reply_text(response)
    return
  update.message.reply_text("Perdón loco, no puedo responder eso, me llamó Macri y ahora soy de JxC")
    
def pokemon(update, context):
  pokemon_search = update.message.text.split('/pokemon')[-1].strip()
  res = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + pokemon_search)
  if res.status_code != 200:
    update.message.reply_photo("https://imgs.search.brave.com/zJhPICzAl9QUjS7VgNtbmYXhxfUiCoq31neMht6_I7Q/rs:fit:955:791:1/g:ce/aHR0cHM6Ly9wbGFu/dGlsbGFzZGVtZW1l/cy5jb20vaW1nL3Bs/YW50aWxsYXMvcGlr/YWNodS1jb25mdW5k/aWRvLXNvcnByZW5k/aWRvLXNvbnJpZW5k/bzYucG5n")
    return
  data = res.json()
  pokemon_name = data['name']
  pokemon_id = data['id']
  color = data['color']['name']
  habitat = data['habitat']['name']
  is_legendary = "Si" if data['is_legendary'] else "No"
  flavor_text_entries = data['flavor_text_entries']
  flavor = ""
  for entry in flavor_text_entries:
    if entry['language']['name'] == 'es':
      flavor += f"{entry['flavor_text']}\n"

  evolution_chain_endpoint = data['evolution_chain']['url']
  res = requests.get(evolution_chain_endpoint)
  evolution_chain_response = res.json()
  evolution_chain = evolution_chain_response['chain']
  chain = ""
  while True:
    if not evolution_chain['evolves_to']:
      break
    chain += evolution_chain['species']['name'] + " -> "
    evolution_chain = evolution_chain['evolves_to'][0]

  chain += evolution_chain['species']['name']

  description = "Desconocido"
  characteristic_response = requests.get(f'https://pokeapi.co/api/v2/characteristic/{pokemon_id}')
  if characteristic_response.status_code == 200:
    data = characteristic_response.json()
    for desc in data['descriptions']:
      if desc['language']['name'] == 'es':
        description = desc['description']
        break

  pokemon_info_endpoint = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
  data = pokemon_info_endpoint.json()
  image = data['sprites']['other']['official-artwork']['front_default']
  
  bulbapedia_link = f'https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}'
  response = f"\n*{pokemon_name.capitalize()}*\n• *ID*: {pokemon_id}\n• *Color*: {color}\n• *Habitat*: {habitat}\n• *Evoluciones*: `{chain}`\n• *Descripción*: {description}\n• *Legendario*: {is_legendary}\n• *Bulbapedia*: [Ir a la bulbapedia]({bulbapedia_link})"

  update.message.reply_photo(image, caption=response, parse_mode='Markdown')


def imaginate(update, context):
  prompt = update.message.text.split('/imaginate')[-1].strip()
  file_paths = dalle.generate_and_download(prompt)
  print(file_paths);
  for path in file_paths:
    with open(path, 'rb') as f:
      update.message.reply_photo(f)
    


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("dolar", dolar))
    dp.add_handler(CommandHandler("albondiga_magica", albondiga_magica))
    dp.add_handler(CommandHandler("peso", peso))
    dp.add_handler(CommandHandler("massa", massa))
    dp.add_handler(CommandHandler("massa_yankee", massa_yankee))
    dp.add_handler(CommandHandler("pokemon", pokemon))
    dp.add_handler(CommandHandler("imaginate", imaginate))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, no_entendi))


    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()