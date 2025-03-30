import timeit, sys

class MyClass:
    def __init__(self, args = sys.argv):
        if len(args)!=3:
            print('Invalid number of arguments')
        self.method = args[1]
        self.number = int(args[2])

    @staticmethod
    def loop(emails):
        res = []
        for email in emails:
            if email.endswith('@gmail.com'):
                res.append(email)
        return res

    @staticmethod
    def list_comprehension(emails):
        return [email for email in emails if email.endswith('@gmail.com')]

    @staticmethod
    def map_method(emails):
        return map(lambda email: email if email.endswith('@gmail.com') else '', emails)
    
    @staticmethod
    def filter_method(emails):
        return filter(lambda email: email.endswith('@gmail.com'), emails)

    def solving(self):
        emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
                  'anna@live.com', 'philipp@gmail.com'] * 5
        time = None

        if self.method == 'loop':
            time = timeit.timeit(
                lambda: self.loop(emails), number=self.number
            )

        if self.method == 'list_comprehension':
            time = timeit.timeit(
                lambda: self.list_comprehension(emails), number=self.number
            )

        if self.method == 'map':
            time = timeit.timeit(
                lambda: list(self.map_method(emails)), number=self.number
            )
        
        if self.method == 'filter':
            time = timeit.timeit(
                lambda: list(self.filter_method(emails)), number=self.number
            )

        if time is None:
            raise 'Try another method!'
        
        print(f'{time:.7f}')

if __name__ == '__main__':
    MyClass().solving()




