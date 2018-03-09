  
  
# def Hello(name):
#     print('Hello {} !'.format(name))
    
# Hello(input('What is your name?'))

# import matplotlib
# matplotlib.use("Agg")

# from matplotlib import pyplot

# def f(x):
#     return x + 1
    
# xs = list(range(-3, 4))
# ys = []
# for x in xs:
#     ys.append(f(x))
    
# pyplot.plot(xs, ys)
# pyplot.savefig('Number1.png')
# pyplot.close()


# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# def square(x):
#     return x * x
    
# xs = list(range(-100, 101))
# ys = []
# for x in xs:
#     ys.append(square(x))
    
# pyplot.plot(xs, ys)
# pyplot.savefig('Number2.png')
# pyplot.close()


# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# def f(x):
#     if x%2 == 0:
#         return -1
#     else:
#         return 1
    
# xs = list(range(-5, 6))
# ys = []
# for x in xs:
#     ys.append(f(x))
    
# pyplot.bar(xs, ys)
# pyplot.savefig('Number3.png')
# pyplot.close()



# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# from math import sin

# def f(x):
#     return sin(x)
    
# xs = list(range(-5, 6))
# ys = []
# for x in xs:
#     ys.append(f(x))
    
# pyplot.plot(xs, ys)
# pyplot.savefig('Number4.png')
# pyplot.close()




# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# from math import sin
# from numpy import arange

# def f(x):
#     return sin(x)
    
# xs = arange(-5, 6, 0.1)
# ys = []
# for x in xs:
#     ys.append(f(x))
    
# pyplot.plot(xs, ys)
# pyplot.savefig('Number5.png')
# pyplot.close()



# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# from math import sin
# from numpy import arange
# import numpy


# def celcius2fahrenheit(temp):
#     return (temp * 1.8 + 32)
    
# xs = list(range(0, 100))
# ys = []

# for x in xs:
#     y = celcius2fahrenheit(x)
#     ys.append(y)
    
# pyplot.plot(xs, ys)
# pyplot.savefig('Number6.png')
# pyplot.close()




# def f():
#     play_again = input('Do you want to play again (Y or N)?')
#     if play_again == 'Y':
#      return ('True')
#     else:
#      return('False')
     
     
# print (f())



def g():
    
    while True:
        play_again = input('Do you want to play again (Y or N)?')
        if play_again == 'Y':
         return ('True')
         
        elif play_again == 'N':
         return ('False')
         
        else:
            print('Invalid input.')
            
print(g())














    










    



