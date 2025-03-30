import sys
import logging
from random import randint
import requests
from config import telegram_bot_token, telegram_chat_id

logging.basicConfig(filename='analytics.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

class Research:
    def __init__(self, args=sys.argv):
        self.args = args
        logging.debug('Research instance created')

    def check_data(self):
        logging.debug('Checking data')
        if len(self.args) != 2:
            raise ValueError('Incorrect number of arguments')

        try:
            open(self.args[1], 'r')
        except FileNotFoundError:
            raise FileNotFoundError('No such file')

        with open(self.args[1], 'r') as f:
            lines = f.readlines()

            if len(lines) < 2:
                raise Exception('The file must contain a header and at least one line of data.')

            head = lines[0].strip().split(',')
            if len(head) != 2:
                raise Exception('The first row must contain two words separated by a comma.')

            for line in lines[1:]:
                values = line.strip().split(',')
                if len(values) != 2 or not (values[0] == '0' or values[0] == '1') or not (values[1] == '0' or values[1] == '1'):
                    raise ValueError('Each data line must contain either 0 or 1, separated by a comma.')

    def file_reader(self, has_header=True):
        logging.debug('Reading file')
        self.check_data()
        with open(self.args[1], 'r') as file:
            lines = file.readlines()
            if has_header:
                lines = lines[1:]
            return [list(map(int, line.strip().split(','))) for line in lines]

    def send_telegram_message(self, message):
        logging.debug('Sending Telegram message')
        url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
        payload = {
            'chat_id': telegram_chat_id,
            'text': message
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            raise Exception(f'Failed to send message: {response.text}')

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.debug('Calculations instance created')

        def counts(self):
            logging.debug('Calculating counts of heads and tails')
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            logging.debug('Calculating fractions of heads and tails')
            summary = heads + tails
            head_per = (heads / summary) * 100
            tail_per = (tails / summary) * 100
            return head_per, tail_per

class Analytics(Research.Calculations):
    def predict_random(self, num_predictions):
        logging.debug('Predicting random observations')
        predictions = []
        for _ in range(num_predictions):
            head = randint(0, 1)
            tail = 1 - head
            predictions.append([head, tail])
        return predictions

    def predict_last(self):
        logging.debug('Predicting last observation')
        return self.data[-1]

    def save_file(self, data, filename, extension):
        logging.debug(f'Saving file {filename}.{extension}')
        with open(f"{filename}.{extension}", 'w') as file:
            file.write(data)
