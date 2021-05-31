def is_even(k):
    if k==0 :
        return True
    elif k==2:
        return False
    else:
        return is_even(k-4)


print(is_even(2))
print(is_even(20))
