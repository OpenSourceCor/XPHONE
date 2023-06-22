import random
import os, sys, time
from phonenumbers import carrier
import phonenumbers
import argparse
from pystyle import Colors, Colorate, Center
from threading import Thread
from tqdm import tqdm

print(Colorate.Vertical(Colors.black_to_red, """
                                    ██╗  ██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
                                    ╚██╗██╔╝██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
                                     ╚███╔╝ ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  
                                     ██╔██╗ ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  
                                    ██╔╝ ██╗██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗
                                    ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   
                                    +--------------------------------------------------+
                                    |  [+] - Générateur de numéros de téléphone FR     |
                                      Github : https://github.com/OpenSourceCor/XPHONE
                                                    By N0x, Hawkishx & Zqx           
                                                   """, 1))

for i in tqdm(range(100), desc=Colors.yellow + "Loading" + Colors.white, ascii=False, ncols=75):
    time.sleep(0.01)

def generate_phone_number():
    phone_number = random.choice(["+336", "+337"])
    phone_number += str(random.randint(0, 9))
    phone_number += ''.join(random.choice("123456789") for _ in range(7))
    parse = phonenumbers.parse(phone_number)
    operator = carrier.name_for_number(parse, 'fr')
    
    return phone_number, operator

def cccv(num):
    phone_numbers = [generate_phone_number() for _ in range(num)]

    operator_numbers = {}
    print(f"Try to generate {len(phone_numbers)}", Colors.orange)
    for phone_number, operator in phone_numbers:
        if operator not in operator_numbers:
            operator_numbers[operator] = []
        operator_numbers[operator].append(phone_number)

    for operator, numbers in operator_numbers.items():
        try:
            directory = "check phone"
            if not os.path.exists(directory):
                os.makedirs(directory)
            file_path = os.path.join(directory, f'{operator.lower()}.txt')

            if os.path.exists(file_path):
                mode = 'a'  
            else:
                mode = 'w'  

            with open(file_path, mode) as file:
                for number in numbers:
                    file.write(number + "\n")
            print(f"[+] - {len(numbers)} numéros générés pour l'opérateur {operator}", Colors.green)
        except Exception as e:
            pass

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, help='Nombre de numéros à générer')
args = parser.parse_args()

if args.n is not None:
    num_numbers = args.n
else:
    num_numbers = 5000
    
cccv(num_numbers)
