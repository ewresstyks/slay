# 1
# python.exe -m pip install --upgrade pip
# or
# pip install --upgrade pip

# 2
# python.exe -m pip install -r requirements.txt
# or
# pip install -r requirements.txt

import time
import requests
import random
import os
from dotenv import load_dotenv
load_dotenv()
bot_token = os.getenv("TOKEN")

url = f"https://api.telegram.org/bot{bot_token}/"  # don't forget to change the token!
bot_key = '8366770160:AAFosaiKzpT2O2i2-p8Bxr4SdV8Lg4xfrEY'

url = f"https://api.telegram.org/bot{bot_key}/"  # don't forget to change the token!


jokes = [
    "tung tung tung sahur",
    "balerinacapuchino'",
    "chimpanzini bananini" ]


def last_update(request):
    response = requests.get(request + 'getUpdates')
    # TODO: Uncomment just for local testing
    # print(response)
    response = response.json()
    # print(response)
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    try:
        update_id = last_update(url)['update_id']
        while True:
            time.sleep(3)
            update = last_update(url)
            if update_id == update['update_id']:


                message_text = get_message_text(update).lower()

                if message_text == 'hi' or message_text == 'hello' or message_text == 'hey':

                    send_message(get_chat_id(update), 'Greetings! Type "dice", "coin", "time" or "joke"!')

                elif message_text == 'qa24':
                    send_message(get_chat_id(update), 'Python')

                elif message_text == 'gin':
                    send_message(get_chat_id(update), 'Finish')
                    break

                elif message_text == 'python':
                    send_message(get_chat_id(update), 'version 3.10')

                elif message_text == 'dice':
                    _1 = random.randint(1, 6)
                    _2 = random.randint(1, 6)
                    send_message(get_chat_id(update),
                                 'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')

                elif message_text == 'coin':
                    result = random.choice(['Orel', 'Reshka'])
                    send_message(get_chat_id(update), 'Result: ' + result)

                elif message_text == 'time':
                    current_time = time.ctime()
                    send_message(get_chat_id(update), 'Time now: ' + current_time)

                elif message_text == 'joke':
                    joke = random.choice(jokes)
                    send_message(get_chat_id(update), joke)

                else:
                    send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')

                update_id += 1
    except KeyboardInterrupt:
        print('\nБот зупинено')


# print(__name__)
if __name__ == '__main__':
    main()