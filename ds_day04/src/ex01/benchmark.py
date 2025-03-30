import timeit

class MyClass:

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
    
    def solving(self):
        emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
                  'anna@live.com', 'philipp@gmail.com'] * 5

        loop_time = timeit.timeit(lambda: self.loop(emails), number=90000000)

        comprehension_time = timeit.timeit(lambda: self.list_comprehension(emails), number=900000000)

        map_time = timeit.timeit(lambda: self.map_method(emails), number=90000000)

        if map_time <= comprehension_time and map_time <= loop_time:
            print("it is better to use a map")
        elif comprehension_time <= loop_time:
            print("it is better to use a list comprehension")
        else:
            print("it is better to use a loop")

        times = sorted([loop_time, comprehension_time, map_time])
        print(" vs ".join([f"{round(time, 6)}" for time in times]))

if __name__ == '__main__':
    MyClass().solving()
