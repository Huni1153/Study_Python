comment = '''while True:
    stuff = input("String to capitalize [type q to quit] : ")
    if stuff == "q":
        break
    print(stuff.capitalize())'''
word = 'thud'
for letter in word:
    print(letter)
print("---------------------------")
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")
