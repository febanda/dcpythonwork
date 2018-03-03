total_bill = float(input('Total bill amount?'))
level_service = input('Level of Service?')
good = float(.20 * total_bill)
fair = float(.15 * total_bill)
bad = float(.10 * total_bill)
if level_service == "good":
    print('Tip amount: {:.2f}'.format(good))
    print('Total amount: {:.2f}'.format(total_bill + good))
elif level_service == "fair":
    print('Tip amount: {:.2f}'.format(fair))
    print('Total amount: {:.2f}'.format(total_bill + fair))
elif level_service == "bad":
    print('Tip amount: {:.2f}'.format(bad))
    print('Total amount: {:.2f}'.format(total_bill + bad))