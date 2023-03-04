def fib(num):
    li = [1,2,3]
    if num < 0:
        return 'please write int number'
    if num in li:
        return num
    else:
        while len(li) < num:
            li.append(li[-1] + li[-2])
    return li[-1]
print(fib(14))
