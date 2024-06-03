import random
import string

small = ''.join(random.choices(string.ascii_lowercase, k=2))
symbol = ''.join(random.choices(string.punctuation, k=2))
numbers = ''.join(random.choices(string.digits, k=2))
capital = ''.join(random.choices(string.ascii_uppercase, k=2))

password_chars = small + symbol + numbers + capital
password_chars_list = list(password_chars)
random.shuffle(password_chars_list)

password = ''.join(password_chars_list)

print(password)