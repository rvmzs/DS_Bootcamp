import sys
from random import randint

class Research:
    def __init__(self, args=sys.argv):
        self.args = args

    def check_data(self):
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
        self.check_data()
        with open(self.args[1], 'r') as file:
            lines = file.readlines()
            if has_header:
                lines = lines[1:]
            return [list(map(int, line.strip().split(','))) for line in lines]

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            summary = heads + tails
            head_per = (heads / summary) * 100
            tail_per = (tails / summary) * 100
            return head_per, tail_per

class Analytics(Research.Calculations):
    def predict_random(self, num_predictions):
        predictions = []
        for _ in range(num_predictions):
            head = randint(0, 1)
            tail = 1 - head
            predictions.append([head, tail])
        return predictions

    def predict_last(self):
        return self.data[-1]

    def save_file(self, data, filename, extension):
        with open(f"{filename}.{extension}", 'w') as file:
            file.write(data)
