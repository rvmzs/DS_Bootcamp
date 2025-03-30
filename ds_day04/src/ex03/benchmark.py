from functools import reduce
import timeit
import sys

class MyClass:

    def __init__(self, args=sys.argv):
        if len(args) != 4:
            print('Invalid number of arguments!')
            sys.exit(1) 
        self.method = args[1]
        self.iter = int(args[2])
        self.number = int(args[3])

    @staticmethod
    def loop(number):
        res = 0
        for i in range(1, number + 1):
            res += i * i  
        return res
    
    @staticmethod
    def reduce_method(number):  
        return reduce(lambda y, x: y + x * x, range(1, number + 1), 0)
    
    def solving(self):
        time = None
        if self.method == 'loop':
            time = timeit.timeit(
                lambda: self.loop(self.number), number=self.iter  
            )
       
        elif self.method == 'reduce': 
            time = timeit.timeit(
                lambda: self.reduce_method(self.number), number=self.iter 
            )

        if time is None:
            raise Exception('Try another method!')  

        print(f'{time:.7f}')  

if __name__ == '__main__':
    MyClass().solving()