class Research:
    def file_read(self, file):
        with open (file, 'r') as f:
            return f.readlines()
        
if __name__=='__main__':
    research = Research()
    content = research.file_read('../ex00/data.csv')
    for line in content:
        print(line.strip())


