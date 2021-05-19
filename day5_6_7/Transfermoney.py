
print('online shipping from AliEx')
print('way to pay for airpods')
way = (input('PAYMENT: ')).lower()
balance = 6000 #balance
acer = 3500  # costs

if way ==  'mastercard':
    print('sorry... MS  is not maintainig!')
elif way == 'elcard':
    print('sorry...Ed is not maintaing!')

elif way == 'visa' or way == 'paypal':
    print('')
    print('Download....')
    card_no = input('Card no.: ')
    if len(card_no) > 6 or len(card_no) < 6:
        print('Card no. is incorrect...')
        quit()
        
    

    summ = int(input('Amount of money???: '))
    
    if acer > summ:

        print('U cant pay less then the costs of the good!    ')

    else:
        print('download...')
        print('')
        a = 'With check'
        b = 'Not'
        input('with check or not?:' )
        if a == a or b == b:
            print('')
            print('Download...')
        else :
            print('Error!     ')
        
        print('')
        
        s = float(summ - acer)
        print('u have', s ,'on ur card')
        
     
        print('Successfully paid!    Thnks for using our goods!  ')
    
    




    







