try:
    def multiply(a, b):
        print(a*b)
        
    def divide(c, d):
        print(c/d)
        
    def add(e, f):
        print(e+f)
        
    def subtract(g, h):
        print(g-h)
        
    def square(i):
        print(i**2)
        
    def cube(j):
        print(j**3)
        
    def sqrt(k):
        print(k**(1/2))
        
    def cbrt(l):
        print(l**(1/3))
        
    def modulo(m, n):
        print(m % n)

    def percentage(o, p):
        print(o*(p/100))

    def exp(q, r):
        print(q**(r))
        
    def pythagorean(height, base):
        return ((height**2)+(base**2))**(1/2)

    def triangle_area(height, base):
        return (height*base)/2

except ZeroDivisionError:
    print('Undefined')

except ValueError:
    print('Invalid Input')
    
except TypeError:
    print('Invalid Input')
    
except NameError:
    print('Invalid Input')
