import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

clients_set = set(clients)
participants_set = set(participants)
recipients_set = set(recipients)

def call_center():
    return list(clients_set - recipients_set)

def potential_clients():
    return list(participants_set - clients_set)

def loyalty_program():
    return list(clients_set - participants_set)

def main(arg):
    if arg == "call_center":
        result = call_center()
    elif arg == "potential_clients":
        result = potential_clients()
    elif arg == "loyalty_program":
        result = loyalty_program()
    else:
        raise ValueError("Invalid task name. Please choose 'call_center', 'potential_clients', or 'loyalty_program'.")
    
    print(result)




if __name__ == "__main__":
    if len (sys.argv) == 2:
        main(sys.argv[1])