

try:

    a = int(input('1.Enter number: '))
    b = int(input('2.Enter number: '))
    z = a / b
    print(a,'/',b,'=',a / b)
except ZeroDivisionError:
    print('GOTTYA NO ZERO MAN!')
except ValueError:
    print('strings are not allowed!')
except NameError:
    print('Look everything carefully!')
except:
    print('Tech Errors!')