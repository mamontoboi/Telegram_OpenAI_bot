import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_TOKEN')


def interaction(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50
    )

    return response
