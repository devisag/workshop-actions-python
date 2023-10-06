import requests
import json
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()
my_wb = os.getenv("SECRET_WEBHOOK")

web_hook_url = f'https://hooks.slack.com/services/{my_wb}'

slack_mg = {
   'text': 'El grafico de google trends fue actualizado con éxito!'
}

requests.post(web_hook_url, data=json.dumps(slack_mg))