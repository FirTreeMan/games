a = 'okay'
b = 'ok fricker'
c = 'deres nothing here...'
d = 'its locked...'
e = 'u dont have da reqired materials'
f = 'cant do that'
secretlore1 = "you can just barely see the words '1: mustard'"
secretlore2 = ""
secretlore3 = ""
secretlore4 = "you can barely make out the words '4: turnips'"
secretlore5 = ""
stuck = '''
this is the help screen

type 'use ____' to use an item in ur inventory
type 'interact ____' to interact with something
type 'merge ____ w/ ____' to merge 2 items together
'''
inputvars = 'kay, hay, bay, lay, day'
inventoryee = "you don't have anything right now"
while True:
    choice1 = '''
You awake in a small room. Wat u wanna do
1. walk out the room
2. S T R I D E out da room LIKE A BOSS
3. inventory
4. yellow

u can also type skipcodes here
'''
    print(choice1)
    test = input('wat u gonna do\n')
    if test == '1':
        print('u walk out da room')
        print('u advanced to LEVEL 2')
    if test == '2':
        print('u S T R I D E out da room awsomely')
        print('u advanced to LEVEL 2')
    if test == '3':
        print(inventoryee)
        continue
    if test == '2':
        break
    if test == '1':
        break
    if test == 'hotham':
        break
    if test == 'mayochill69':
        break
    if test == 'kookyburro':
        break
    if test == 'stuck':
        print(stuck)
        continue
    else:
        print(a)
        print('')
        continue
while True:
    if test == 'hotham':
        break
    if test == 'mayochill69':
        break
    if test == 'kookyburro':
        break
    choice2 = '''ur now in a room with a lock on the door in front of u. deres also a noice rug.
    1. go to the door
    2. go to teh rug
    3. flip da rug
    4. inventory
    5. yellow
    '''
    print(choice2)
    test2 = input("wat choo gonna doo\n")
    if test2 == '1':
        kay = input('u wanna do sumtin\n')
        if inventoryee == "u don't have anything right now":
            print('its locked duh')
        if kay == 'ok boomer':
            print(b)
        if inventoryee == 'u hav a NOOB KEEY':
            if kay == 'use NOOB KEEY':
                print('da lock opened noice job')
                print('u are on LEVEL 3')
                print("u can skip to LEVEL 3 w/ SKIPCODE 'hotham'")
                break
            else:
                print(a)
            if kay == 'ok boomer':
                print(b)
    if test2 == '2':
        print('its a noice rug')
    if test2 == '3':
        if inventoryee == 'u hav a NOOB KEEY':
            print(c)
        if inventoryee == "you don't have anything right now":
            print('itz a NOOB KEEY')
            inventoryee = 'u hav a NOOB KEEY'
            print("remember 2 type 'use ____' on something to use dat item")
    if test2 == '4':
        print(inventoryee)
    if test2 == 'stuck':
        print(stuck)
        continue
    else:
        print(a)
inventoryee = 'nothing here...'
inventoryee2 = 'nothing here...'
while True:
    if test == 'mayochill69':
        break
    if test == 'kookyburro':
        break
    choice3 = '''
ur in aroom
1. go to rug
2. go to trapdoor
3. go to door
4. inventory
5. yellow
remember to type 'merge ___ w/ ___' to combine 2 items and
type 'interact ____' to interact with sumting
'''
    print(choice3)
    test3 = input('wat u will do\n')
    if test3 == '1':
        bay = input('wat u wanna do\n')
        if bay == 'ok boomer':
            print(b)
            continue
        if bay == 'interact rug':
            if inventoryee == 'u have a KEY HANDLE':
                print(c)
                continue
            if inventoryee == 'u have a SMOL KEY':
                print(c)
                continue
            if inventoryee == 'nothing here...':
                inventoryee = 'u have a KEY HANDLE'
                print('u found a KEY HANDLE')
                continue
        else:
            print(a)
            continue
    if test3 == '2':
        hay = input('wat u wanna do\n')
        if hay == 'ok boomer':
            print(b)
            continue
        if hay == 'inspect trapdoor':
            print(secretlore4)
            continue
        if hay == 'interact trapdoor':
            if inventoryee2 == 'u have a KEY HEAD':
                print(c)
                continue
            if inventoryee2 == ' ':
                print(c)
                continue
            if inventoryee2 == 'nothing here...':
                print('u got a KEY HEAD')
                inventoryee2 = 'u have a KEY HEAD'
                continue
        else:
            print(a)
            continue
    if test3 == '3':
        lay = input('wat u want do hmm\n')
        if inventoryee == 'u hav a SMOL KEY':
            if lay == 'use SMOL KEY':
                print('u got out noice')
                print('you advanced to LEVEL 4')
                print("SKIPCODE to LEVEL 4 is 'mayochill69'")
                break
        else:
            print(d)
            continue
    if test3 == '4':
        print(inventoryee)
        print(inventoryee2)
        continue
    if test3 == '5':
        continue
    if test3 == 'stuck':
        print(stuck)
        continue
    if test3 == 'merge KEY HANDLE w/ KEY HEAD':
        if inventoryee == 'u have a KEY HANDLE':
            if inventoryee2 == 'u have a KEY HEAD':
                print('u made a SMOL KEY')
                inventoryee = 'u hav a SMOL KEY'
                inventoryee2 = ' '
                continue
        else:
            print(e)
    if test3 == 'merge KEY HEAD w/ KEY HANDLE':
        if inventoryee == 'u have a KEY HANDLE':
            if inventoryee2 == 'u have a KEY HEAD':
                print('u made a SMOL KEY!!!111')
                inventoryee = 'u hav a SMOL KEY'
                inventoryee2 = ' '
                continue
        else:
            print(e)
    if test3 == 'merge KEY HEAD w/ NOOB KEEY':
        print(e)
        print('')
        continue
    if test3 == 'merge NOOB KEEY w/ KEY HEAD':
        print(e)
        print('')
        continue
    if test3 == 'merge KEY HANDLE w/ NOOB KEEY':
        print(e)
        print('')
        continue
    if test3 == 'merge NOOB KEEY w/ KEY HANDLE':
        print(e)
        print('')
        continue
    else:
        print(a)
inventoryee = 'nothing here...'
inventoryee2 = ' '
while True:
    if test == 'kookyburro':
        break
    choice4 = '''
alright here we go again
    1. go to the door
    2. go to wall
    3. go to key pedestal
    4. inventory
    5. yellow
    remember that u can type 'inspect _____' to closely look at sumting
    remember to type 'stuck' for help on how to do stuff
    
'''
    print(choice4)
    test4 = input('so wat will u do\n')
    if test4 == '1':
        print('its a standard-issue 2-lock door')
        bay = input('wat u will do\n')
        if bay == 'use KEY UNO':
            if inventoryee == 'u have KEY UNO':
                day = input('now wat')
                if day == 'use KEY DOS':
                    if inventoryee2 == 'u have KEY DOS':
                        print('u advanced to LEVEL 5')
                        print("btw SKIPCODE to LEVEL 5 is 'kookyburro'")
                        break
        if bay == 'use KEY DOS':
            if inventoryee2 == 'u have KEY DOS':
                day = input('now wat\n')
                if day == 'use KEY UNO':
                    if inventoryee == 'u have KEY UNO':
                        print('u advanced to LEVEL 5')
                        print("btw SKIPCODE to LEVEL 5 is 'kookyburro'")
                        break
    if test4 == '2':
        print('there is faint writing')
        hay = input('wat will u do\n')
        if hay == 'inspect wall':
            print(secretlore1)
            continue
    if test4 == '3':
        lay = input('wat u do\n')
        if lay == 'inspect key pedestal':
            if inventoryee == 'nothing here...':
                print('u cant look behind the key pedestal unless you take its key')
                continue
            if inventoryee == 'u have KEY UNO':
                if inventoryee2 == ' ':
                    print('u found another key!!!!111')
                    inventoryee2 = 'u have KEY DOS'
                    continue
                if inventoryee2 == 'u have KEY DOS':
                    print(c)
                    continue
        if lay == 'interact key pedestal':
            if inventoryee == 'u have KEY UNO':
                print(c)
                continue
            if inventoryee == 'nothing here...':
                print('U fount a key!!!1')
                inventoryee = 'u have KEY UNO'
                continue
    if test4 == '4':
        print(inventoryee)
        print(inventoryee2)
        continue
    if test4 == '5':
        continue
    if test4 == 'merge KEY UNO w/ KEY DOS':
        if inventoryee == 'nothing here...':
            print(e)
            continue
        if inventoryee == 'u have KEY UNO':
            if inventoryee2 == 'nothing here...':
                print(e)
                continue
            if inventoryee2 == 'u have KEY DOS':
                print(f)
                continue
    if test4 == 'merge KEY DOS w/ KEY UNO':
        if inventoryee == 'nothing here...':
            print(e)
            continue
        if inventoryee == 'u have KEY UNO':
            if inventoryee2 == 'nothing here...':
                print(e)
                continue
            if inventoryee2 == 'u have KEY DOS':
                print(f)
                continue
    if test4 == 'stuck':
        print(stuck)
        continue
    else:
        print(a)
        continue
inventoryee = 'nothing is here...'
inventoryee2 = 'nothing is here...'
while True:
    choice5 = '''
    
    '''
    print(choice5)
    test5 = input('what action will you pertain to committing\n')
