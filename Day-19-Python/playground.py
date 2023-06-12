def add(*args):
    # MY CODE VERSION
    # print(sum(args))

    # THE SOLUTION
    sum=0
    for num in args:
        sum += num
    print(sum)
    
add(1,2,3,4,5,6)

def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculator(3, add = 3, multiply = 5)
