for number in range(1, 10 + 1):
    print (number)


start_number = int(input('Start from:'))
end_number = int(input('End on:'))
for number in range(start_number, end_number + 1):
    print (number)
    
    
    
for number in range(1, 10 + 1):
    if number%2 != 0:
        print (number)
        

import sys


size = int(5)
for i in range(size):
    print ('*' * size)
    
    
size = int(input('How big is the square?'))
for i in range(size):
    print ('*' * size)
    
 
#print multiplication_table
n=int(input('Please enter a positive integer between 1 and 10: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, "\t",end = "")      
    print() 
    
    
a = input('Text?')
b = len(a) + 2
print('*' * b)
print('*'+ a + '*')
print('*' * b)


for number in range (1,100):
    a = number*(number+1)/2
    print (a)
    
    