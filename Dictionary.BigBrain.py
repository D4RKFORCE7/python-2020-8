ccp = {}

while True:
    print('1.set up vocab')
    print('2.print all information')
    print('3.translate english')
    print('4.translate chinese')
    print('5.Learning test')
    print('6.leaving system')
    sel = input('enter your options:')
    if sel == '1':
        en = input('Enter engrish:')
        chi = input('Enter chinese:')
        ccp[en]=chi
    elif sel == '2':
        for k,v in ccp.items():
            print(k,':',v)
    elif sel == '3':
        search = input('search engrish: ')
        print(ccp[search])
    elif sel == '4':
        for k,v in ccp.items():
            if search == v:
                print(k)
    elif sel == '5':
        score = 0
        for k,v in ccp.items():
            print(v,':')
            ans = input('enter your answer:')
            if ans == k:
                print('congrats!')
                score = score + 1
        print('your score:',score)
    elif sel == '6':
        break



