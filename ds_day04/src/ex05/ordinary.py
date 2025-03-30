import sys
import time
import resource

class MyClass:

    def __init__(self, args=sys.argv):
        if len(args) != 2:
            raise 'Invalid number of arguments'
        self.file_path = args[1]
    
    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except:
            raise 'Try another file!'

    def solving(self):
        start_time = time.process_time()
        data = self.read_file(self.file_path)
        for line in data:
            pass
        end_time = time.process_time()

        peak_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 ** 2)

        print(f"Peak Memory Usage = {peak_memory:.3f} GB")
        print(f"User Mode Time + System Mode Time = {end_time - start_time:.2f}s")

if __name__ == '__main__':
    MyClass().solving()

