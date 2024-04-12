import random

def generator_email():
    login = ''
    for _ in range(3):
        login += random.choice('qwertyuioplkjhgfdsazxcvbnm1234567890')
    domain = random.choice(['ya.ru', 'gmail.com', 'mail.ru'])
    email = f'{login}@{domain}'
    return email

def generator_password():
    characters = 'asddfghjklzxcvbnmqwertyuiopASDFGHJKLQWERTYUIOPZXCVBNM1234567890'
    length = random.randint(6, 10)
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password