def power(base,exponent):
    if exponent ==0:
        return 1
    return base*( base,exponent-1)
print(power(2,0))
print( power(2,2))
print(power(2,4))