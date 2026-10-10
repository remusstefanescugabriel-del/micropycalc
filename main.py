import math

def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return n1 / n2
def power(n1, n2): return n1 ** n2
def sqrt(n1): return math.sqrt(n1)
def mod(n1, n2): return n1 % n2

"""LOGARITHMIC FUNCTIONS"""
def log_natural(n1): return math.log(n1)
def log_baza(n1, baza): return math.log(n1, baza) #baza arbitrara

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    'sqrt': sqrt,
    '%': mod,
    'log': log_baza
}

# rezultat = operations['*'](4, 8)

while True:
    print("\n--- CALCULATOR NOU ---")
    try:
        x = float(input("Introdu primul numar: "))
    except ValueError:
        print("introdu un numar!")
        continue
    print("'+'  '-'  '*'  '/'  '**'  'sqrt'  '%'  'log' sau 'reset'")


    while True:
        calc = input("alege operatia:\n")

        if calc.lower() == "reset":
            break

        if calc not in operations:
            continue

        if calc == "log":
            print("introdu log natural 'e' sau alta baza: ")
            baza_input = input("")
            if baza_input.lower() == "e":
                rezultat = log_natural(x)
            else:
                rezultat = log_baza(x, float(baza_input))

        elif calc == "sqrt":
            rezultat = sqrt(x)

        else:
            y = float(input("introdu un numar: "))
            rezultat = operations[calc](x, y)

        print(rezultat)
        x = rezultat

