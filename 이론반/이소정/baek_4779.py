import sys
def can(n) :
    if n == 1 :
        return "-"
    cantor_unit = can(n//3)
    cantor_res = cantor_unit + " " * (n//3) + cantor_unit
    return cantor_res

while True :
    try :
        N = int(sys.stdin.readline())
        print(can(3**N))
    except :
        break