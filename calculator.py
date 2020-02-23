while True:
    gel = '''
    welcome 2 calculator
    '+' is add
    '-' is subtract
    '*' is multiply
    '/' is divide
    '^' is exponent
    '%' is remainder
    '&' is square (type 0 as the second number)
    '&&' is square root (type 0 as the second number) [warning - not implemented]
    '@' is cube (type 0 as the second number)
    '@@' is cube root (type 0 as the second number) [warning - not implemented]
    '''
    print(gel)
    a = input("type first number here\n")
    b = int(a)
    aa = input('type operator here\n')
    a2 = input('type second number here\n')
    b2 = int(a2)
    if aa == '+':
        print(b + b2)
    if aa == '-':
        print(b - b2)
    if aa == '*':
        print(b * b2)
    if aa == '/':
        print(b / b2)
    if aa == '^':
        print(b ** b2)
    if aa == '&':
        print(b ** 2)
    if aa == '@':
        print(b ** 3)
    gello = input('another calculation?\n')
    print(gello)
    if gello == 'no':
        break
    if gello == 'N':
        break