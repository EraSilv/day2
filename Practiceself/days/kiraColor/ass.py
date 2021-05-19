import termcolor
termcolor.cprint(
    'hello world', 
    'cyan', 
    attrs=['bold'])


text = '{0} + {1} = {2}'.format(10,10,10+10)

termcolor.cprint(text,'cyan',attrs = ['bold'])