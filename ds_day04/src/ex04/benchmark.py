import timeit, random
from collections import Counter

class MyClass:

    @staticmethod
    def my_func(numbers):
        counts = {}
        for num in numbers:
            counts[num] = counts.get(num, 0) + 1
        return counts

    @staticmethod
    def counter_function(numbers):
        return dict(Counter(numbers))
    
    @staticmethod
    def top_10_my_function(numbers):
        counts = MyClass.my_func(numbers)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_counts[:10]
    
    @staticmethod
    def top_10_counter(numbers):
        counter = Counter(numbers)
        return counter.most_common(10)
    

    def solving(self):
        numbers = [random.randint(0, 100) for _ in range(1000000)]

        time_my_function = timeit.timeit(
            lambda: self.my_func(numbers), number=1
        )
        time_my_function_top = timeit.timeit(
            lambda: self.top_10_my_function(numbers), number=1
        )

        time_counter = timeit.timeit(
            lambda: self.counter_function(numbers), number=1
        )
        time_counter_top = timeit.timeit(
            lambda: self.top_10_counter(numbers), number=1
        )
        
        print(f"my function: {time_my_function:.7f}")
        print(f"Counter: {time_counter:.7f}")
        print(f"my top: {time_my_function_top:.7f}")
        print(f"Counter's top: {time_counter_top:.7f}")

if __name__ == '__main__':
    MyClass().solving()
