numbers = [-1, -7, -5, 3, 5, 10, 2, 1]

print (sum(numbers))

print (max(numbers))

print (min(numbers))


for number in numbers:
    if number%2 == 0:
        print (number)
        
for number in numbers:
    if number > 0:
        print (number) 
        
positive_numbers = []
for number in numbers:
    if number >= 0:
        positive_numbers.append(number)
        
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





    



    




    


    
    






