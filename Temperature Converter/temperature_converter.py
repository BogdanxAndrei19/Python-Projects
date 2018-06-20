## C = Celsius
## K = Kelvin
## F = Fahrenheit

## unit switches

C_to_F = 0
C_to_K = 0

F_to_C = 0
F_to_K = 0

K_to_C = 0
K_to_F = 0

print ("Enter your value:")
value = input()

try:
    if '.' in value:
        value = float(value)
    else: value = int(value)
except ValueError:
    print("Your input should be just a number")


if C_to_F == 1:
    converted_value = value*1.8 + 32
    
if C_to_K == 1:
    converted_value = value + 273.15
    
if F_to_C == 1:
    converted_value = (value - 32)/1.8
    
if F_to_K == 1:
    converted_value = (value - 32)/1.8 + 273.15
    
if K_to_C == 1:
    converted_value = value - 273.15
    
if K_to_F == 1:
    converted_value = (value - 273.15)*1.8 + 32

## in order to avoid results which end in .0
if converted_value - int(converted_value) == 0: 
    converted_value = int(converted_value)

if C_to_F == 1:
    print ('{} C'.format(value) + " converted is " + '{} F'.format(converted_value))
if C_to_K == 1:
    print ('{} C'.format(value) + " converted is " + '{} K'.format(converted_value))

if F_to_C == 1:
    print ('{} F'.format(value) + " converted is " + '{} C'.format(converted_value))

if F_to_K == 1:
    print ('{} F'.format(value) + " converted is " + '{} K'.format(converted_value))

if K_to_C == 1:
    print ('{} K'.format(value) + " converted is " + '{} C'.format(converted_value))

if K_to_F == 1:
    print ('{} K'.format(value) + " converted is " + '{} F'.format(converted_value))



