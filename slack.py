import requests
import json
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()
my_wb = os.getenv("SECRET_WEBHOOK")

web_hook_url = 'https://hooks.slack.com/services/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'

slack_mg = {
   'text': 'El grafico de google trends fue actualizado con éxito!'
}

requests.post(web_hook_url, data=json.dumps(slack_mg))
