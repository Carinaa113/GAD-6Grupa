#suma tuturor nr de la 0 la n

def get_sum(n):
    if n==0:
        return 0
    return n + get_sum(n-1)

print(get_sum(9))

#suma numerelor pare de la 0 la n

def get_sum_evennumbers(n):
    if not n%2==0:
        return n
    else:
        return n+get_sum_evennumbers(n-1)

print(get_sum_evennumbers(12))

#suma numere impare de la 0 la n dat

def sum_odd(n):
    if not n%2 !=0:
        return n
    else:
        return n+get_sum_evennumbers(n-1)

print(sum_odd(30))
