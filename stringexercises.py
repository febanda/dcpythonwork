
first = "Francisco"
first.upper()


last = "banda"
last.capitalize()


food = "desserts"
food[::-1]


paragraph = input('The paragraph: ').upper()
paragraph = paragraph.replace('A', '4')
paragraph = paragraph.replace('E', '3')
paragraph = paragraph.replace('G', '6')
paragraph = paragraph.replace('I', '1')
paragraph = paragraph.replace('O', '0')
paragraph = paragraph.replace('S', '5')
paragraph = paragraph.replace('T', '7')

print(paragraph)


my_word = "cheese"
my_word = my_word.replace('ee', 'eeeee')
my_word = my_word.replace('oo', 'ooooo')

print (my_word)

word = "groove"
word = word.replace('oo', 'ooooo')
word = word.replace('ee', 'eeeee')

print (word)


secret = 'Lbh zhfg hayrnea jung lbh unir yrnearq'
offset = 13
result = ''

for char in secret:
    code = ord(char.lower())
    if code >= 97 and code <= 122:
        code += offset
        if code > 122:
            code = code - 26
            
    result += chr(code)
    
print(result)


