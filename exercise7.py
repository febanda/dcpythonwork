numbers = [-1, -7, -5, 3, 5, 10, 2, 1]

print sum(numbers)

print max(numbers)

print min(numbers)


for i in numbers:
    if i%2 == 0:
        print i 
        
for i in numbers:
    if i > 0:
        print i 
        
positive_numbers = []
for i in numbers:
    if i >= 0:
        positive_numbers.append(i)
        
print (positive_numbers)


my_list = [1, 2, 3, 4, 5]
my_new_list = [i * 5 for i in my_list]
print(my_new_list)


list_one = [3, 6, 9]
list_two = [2, 4, 8]

list_three = [list_one[0] * list_two[0], list_one[1] * list_two[1], list_one[2] * list_two[2]]
print (list_three)


matrix1 = [[1, 3], [2, 4]]
matrix2 = [[5, 2], [1, 0]]
matrix3 = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        
print (matrix3)

matrix4 = [[2, 4], [1, 5], [6, 8], [0, 3]]
matrix5 = [[1, 2], [3, 4], [5, 6], [7, 8]]
matrix6 = [[0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(len(matrix4)):
    for j in range(len(matrix4[0])):
        matrix6[i][j] = matrix4[i][j] + matrix5[i][j]
print (matrix6)
        
        


matrix7 = [[5, 3], [2, 4]]
matrix8 = [[1, 2], [6, 0]]
matrix9 = [[0, 0], [0,0]]
for i in range(len(matrix7)):
    for j in range(len(matrix7[0])):
        matrix9[i][j] = matrix7[i][j] * matrix8[i][j]
        
print (matrix9)



names = ['Frankie', 'Robin', 'Sara', 'Sara']
names = set(names)
names = list(names)
print(names)


first_name = "Francisco"
print first_name.upper()


last_name = "banda"
print last_name.capitalize()


food = "desserts"
print food[::-1]


import string

the_text = "Hello my name is Francisco, it is nice to meet you! I live in friendswood, and work in the heights. I have lived in texas all my life. I love to travel, I plan to go to europe in 2019."
new_text = ""

for i in range(len(the_text)):
    if the_text[i] == 'a':
        new_text+='4'
        continue
    if the_text[i] == 'e':
        new_text+='3'
        continue
    if the_text[i] == 'g':
        new_text+='6'
        continue
    if the_text[i] == 'i':
        new_text+='1'
        continue
    if the_text[i] == 'o':
        new_text+='0'
        continue
    if the_text[i] == 's':
        new_text+='5'
        continue
    if the_text[i] == 't':
        new_text+='7'
        continue
    
    new_text+=the_text[i]
    
the_text=new_text
print new_text



my_word = "cheese"
my_word = my_word.replace('ee', 'eeeee')
print my_word

word = "groove"
word = word.replace('oo', 'ooooo')
print word



cipher_text = "Ibh zhfg hayrnea jung Ibh unir yrnearq"

    



    




    


    
    






