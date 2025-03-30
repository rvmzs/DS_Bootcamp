import sys

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
                raise Exception('The first raw must contain a two words separated by comma.')
            
            for line in lines[1:]:
                values = line.strip().split(',')
                if len(values) != 2 or not (values[0] == '0' or values[0] == '1') or not (values[1] == '0' or values[1] == '1'):
                    raise ValueError('Each data line must contain either 0 or 1, separated by a comma.')
        
    def file_reader(self):
        self.check_data()
        with open(self.args[1], 'r') as file:
            for line in file:
                print(line.strip())

if __name__ == '__main__':
    Research().file_reader()


