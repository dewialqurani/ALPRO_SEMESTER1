def anyfunction(number):
    if number==0 or number==1:
        return number+1
    else:
        return anyfunction(number-1)+number