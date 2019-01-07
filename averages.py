# Tristan, tkw6eh
# PA09: averages
# status: completed

def mean(a,b,c):
    return (a+b+c)/3

def median(a,b,c):
    if (a <= b and a >= c) or (a >= b and a <= c):
        return a
    elif (b <= a and b >= c) or (b >= a and b <= c):
        return b
    else:
        return c


def rms(a, b, c):
    sum_abc = (mean(a, b, c,))*3
    n1 = sum_abc - b - c
    n2 = sum_abc - a - c
    n3 = sum_abc - a - b
    return ((n1**2 + n2**2 + n3**2)/3)**(1/2)

def middle_average(a, b, c):
    average = mean(a, b, c)
    root_mean_square = rms(a, b, c)
    med = median(a, b, c)
    return median(average, root_mean_square, med)




