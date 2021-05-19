c_pin = 1203 #true pin DemirBank

#дать возможным только 4 кода
balance = 9956 #balance текущий


pin = int(input('PIN:')) # enter our true pin



#if our pin is correct we get next operation or u are at the beginnig
if c_pin == pin:
    print('1. Balance:  ')
    print('2. Cash Out. ')
    print('3. Change Pin.')
    operation = int(input('Choose operation:')) #operation we want
    if operation == 1: # at no 1 we have balance
        print('Ur balance:', balance)
        
    elif operation == 2: #here we have cash out
        
        a = int(input('Cash:')) #here we enter any amount of cash we want none bigger that our balance (error if its bigger)
        if a > balance:
            print('Insufficient Funds!')
            quit()
        print('')
        print('Download......')
        print('')
        print('ZZZZZZZZZZZZZZZZZ    ') #here we are aleady getting cash

        print('Ur current balance :' , balance - a ) 
    elif operation == 3: #we wanna change our pin
        asdd = int(input('New PIN:'))
        asddd = int(input('Enter new PIN one more time!: '))
        if asdd == asddd: #if we enter our new pin correctly 2 times we'll get:

            print('PIN successfully changed!   ')
            print(' Ur new pin:' , asdd)
       
        if asdd != asddd: # if our first or second pins are not the same we will have:
            print('PIN does not match!   ')
        else: #here we are entering again with new pin
            c_pin = asdd
            print('PIN was changed:') 
            adddd = int(input('Enter changed PIN:')) #here we oughtta enter our new pin
            if adddd != c_pin: #checking pin
                print('Error PIN')
            else:
                print('True PIN!')
    
    
    
else:
    print('Incorrect PIN')


