def draw_rec(m, n):
    m = int(input('Enter the length of your rectangle: '))
    n = int(input('Enter the width of your rectangle: '))
    if n > m:
        print('ERROR!!! The width is longer than the length.')
    else:
        for i in range(n):
            print('*'*m)


draw_rec(m='', n='')
