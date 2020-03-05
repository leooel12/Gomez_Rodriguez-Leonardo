d='********'
n=input(print('HI, what is your name'))
print(d)
s=input(print('Tell me your sex M/F'))
print(d)
print('Hola :{}'.format (n))
if s=='F':
    r=input(print('Would you like to go to a restaurant with me? Y/N'))
    if r=='Y':
        print('Awesome see you tomorrow')
    else:
        r=input(print('Then what about a picnic?Y/N'))
        if r=='Y':
            print('Sorry i hate picnics bye')
        else:
            print('It´s ok i have girlfriend')
else:
        r=input(print('Do you have a sister?Y/N'))
        if r=='N':
            print('Well thank you for talking with me, Bye')
        else:
            r=input(print('Can you give me her number?Y/N'))
            if r=='Y':
                print('Thanks i´ll call her tomorrow')
            else:
                print('Ok sorry for asking')
