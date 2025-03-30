class Must_read:
    with open ('data.csv', 'r') as file:
        for lines in file:
            print(lines.strip())

if __name__=='__main__':
    Must_read()

        
