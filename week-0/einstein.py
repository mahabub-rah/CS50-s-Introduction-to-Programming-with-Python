# Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def energy(mass):
    c = 300000000
    return mass *c*c

mass = int(input('Write your mass in Kg: '))

print(energy(mass))
