# 1. In [73]: name = input('What is your name?')
# What is your name?Bob

# In [74]: print('Hello Bob!')
# Hello Bob!

# In [75]: print('Hello, Bob!')
# Hello, Bob!

# 2. In [76]: name = input('WHAT IS YOUR NAME?')
# WHAT IS YOUR NAME?Bob

# In [77]: print("""HELLO, BOB!
#     ...: YOUR NAME HAS 3  LETTERS IN IT! AWESOME!""")
# HELLO, BOB!
# YOUR NAME HAS 3  LETTERS IN IT! AWESOME!

# 3. In [78]: name = input('What is your name?')
# What is your name?Daniel

# In [79]: subject = input('What is your favorite subject?')
# What is your favorite subject?Science


# In [97]: print(name + 's' + ' favorite subject in school is ' + subject)
# Daniels favorite subject in school is Science

# 4. In [98]: day = int(input('Day (0-6)?'))









# Day (0-6)?4

# In [99]: print('Thursday')
# Thursday

# 5. In [108]: day = int(input('Day (0-6)?'))
# Day (0-6)?5

# In [109]: print('Go to work')
# Go to work

# 6. In [118]: user_response = int(input('Temperature in C?'))
# Temperature in C?23

# In [119]: print(user_response * 1.8 + 32)
# 73.4

# In [120]: print(user_response * 1.8 + 32, ' F')
# 73.4  F

# 9. In [123]: while count < 10:
#      ...:     count += 1
#      ...:     print('The count is', count)
#      ...: print('Done')
#      ...:     
# The count is 1
# The count is 2
# The count is 3
# The count is 4
# The count is 5
# The count is 6
# The count is 7
# The count is 8
# The count is 9
# The count is 10
# Done


num_coins = 0
print("You have {} coins.".format(num_coins))
while True:
    status = input("Do you want another? (yes/no) ")
    if status == 'yes':
        num_coins += 1
        print("You have {} coins.".format(num_coins))
    elif status == 'no':
        print("Bye")
        break
    else:
        print("Try again")
        
        
    
        
        