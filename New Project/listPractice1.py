# Hello World program in Python

b = []

while True:
    try:
        a = int(input("enter a random integer: "))
        break
    except ValueError: 
        print ("not an integer!")
        

x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for numb in (x):
    if numb < a:
        b = b + [numb]
print (b)

