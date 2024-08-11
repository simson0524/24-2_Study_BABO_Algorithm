def cantor(n):
    if n == 0:
        return '-'
    else:
        string = cantor(n-1)
        string += ' '*(3**(n-1))
        string += cantor(n-1)
        return string

# 여러줄..어이없삼;;
while True:
    try:
        n = int( input() )
        string = cantor(n)
        print( string )
    except:
        break
