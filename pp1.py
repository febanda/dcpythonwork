name = input('What is your name?')
print('Hello', name,'!')

her_name = input('WHAT IS YOUR NAME?')
print('HELLO,', her_name.upper(), '!')
print('YOUR NAME HAS', len(her_name), 'LETTERS IN IT! AWESOME!')

his_name = input('What is name?')
subject = input('What is subject?')
print(his_name + '\'s', 'favorite subject in school is', subject)


day = int(input('Day (0-6)?'))
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(week[day])        
        
        
day = int(input('Day (0-6)?'))
if day == 0 or day == 6:
    print('Sleep in')
else:
    print('Go to work')
    

temperature = float(input('Temperature in C?'))
print(temperature * 1.8 + 32, 'F')


total_bill = float(input('Total bill amount?'))
service_level = input('Level of service?')
good = float(.20 * total_bill)
fair = float(.15 * total_bill)
bad = float(.10 * total_bill)

if service_level == 'good':
    print('Tip amount: {:.2f}'.format(good))
    print('Total amount: {:.2f}'.format(total_bill + good))
elif service_level == 'fair':
    print('Tip amount: {:2f}'.format(fair))
    print('Total amount: {:.2f}'.format(total_bill + fair))
elif service_level == 'bad':
    print('Tip amount: {:2f}'.format(bad))
    print('Total amount: {:.2f}'.format(total_bill + bad))
        


total_bill = float(input('Total bill amount?'))
service_level = input('Level of service?')
splitting = int(input('Split how many ways?'))
good = float(.20 * total_bill)
fair = float(.15 * total_bill)
bad = float(.10 * total_bill)

if service_level == 'good':
    print('Tip amount: {:.2f}'.format(good))
    print('Total amount: {:.2f}'.format(total_bill + good))
    print('Total amount: {:.2f}'.format(total_bill + good / splitting))
elif service_level == 'fair':
    print('Tip amount: {:2f}'.format(fair))
    print('Total amount: {:.2f}'.format(total_bill + fair))
    print('Total amount: {:.2f}'.format(total_bill + fair / splitting))
elif service_level == 'bad':
    print('Tip amount: {:2f}'.format(bad))
    print('Total amount: {:.2f}'.format(total_bill + bad))
    print('Total amount: {:.2f}'.format(total_bill + bad / splitting))
    
    
    
    
for i in range(1, 10 +1):
    print (i)
        

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
        
        
        
        
