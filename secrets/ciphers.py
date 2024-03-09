'''
    Generates a random cipher
    for the application
'''
# pylint:  disable=W1514, C0209
import random

letters = ['a', ' b', ' c', ' d', ' e', ' f', 
           ' g', ' h', ' i', ' j', ' k', ' l', 
           ' m', ' n', ' o', ' p', ' q', ' r', 
           ' s', ' t', ' u', ' v', ' w', ' x', 
           ' y', ' z']

def generate_cipher():
    '''
        Creates a psuedo-random
        cipher for secret
    '''
    cipher = ''
    for _x in range(0, 100):
        rand_num = str(random.randrange(-100, 5000))
        some_letter = random.choice(letters)
        some_other_letter = random.choice(letters)
        cipher += '{}{}{}'.format(some_other_letter.upper(),rand_num,some_letter)
    f_cipher = cipher.replace(' ', '')
    return f_cipher
