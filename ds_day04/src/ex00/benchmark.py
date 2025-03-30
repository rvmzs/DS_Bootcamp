import timeit


class MyClass:
    @staticmethod
    def loop(email_list):
        new_emails=[]
        for email in email_list:
            if email.endswith('@gmail.com'):
                new_emails.append(email)
        return new_emails
    
    @staticmethod
    def list_comprehension(email_list):
        return [email for email in email_list if email.endswith('@gmail.com')]

    def solving(self):
        email_list = [
            'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
            'anna@live.com', 'philipp@gmail.com'
        ] *5
    
        loop_duration = timeit.timeit(
            lambda: self.loop(email_list), number=90000000
        )

        comprehension_duration = timeit.timeit(
            lambda: self.list_comprehension(email_list), number=90000000
        )

        if comprehension_duration <= loop_duration:
            print(f"it is better to use a list comprehension\n{comprehension_duration:.6f} vs {loop_duration:.6f}")
        else:
            print(f"it is better to use a loop\n{loop_duration:.6f} vs {comprehension_duration:.6f}")



if __name__ == '__main__':
    MyClass().solving()


