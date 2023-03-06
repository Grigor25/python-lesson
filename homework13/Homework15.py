#Homework №14
#	1.	Ինչ տարբերություններ կան list comprehension-ի և generator-ի մեջ:

#answer list comprehensin@ stextsum e list isk generator@ generator tipi object	
#	2.	Ինչպես կարող ենք իմանալ function-ը generator է թե ոչ:
#answer returni poxaren gravats e yield
#	3.	Գրեք generator function որը ամեն անգամ next()-ին փոխանցելիս կվերադարցնի fibonacci-ի հաջորդ թիվը:
#		Ստացած function-ի միջոցով տպել fibonacci-ի 25-րդ թիվը:

def fib(num=0):
    fib_num_list = [1,2,3]
    for x in fib_num_list:
        fib_num_list.append(fib_num_list[-1] + fib_num_list[-2])
        yield x
x = fib()
for i in range(25):
    next(x)
    if i == 24:
        print(next(x))

		
#	4.	Գրեք generator որը կփոխարինի range()-ին ( range չօգտագործեք :) ):

def range_copy(*args):
    if len(args) > 2:
        raise TypeError('range can take only two agrs')
    elif len(args) == 2:
        (start,end) = args
    else:
        (start,end) = (0,*args)
    range_list = []
    while start < end:
        range_list.append(start)
        start += 1
    for step in range_list:
        yield step

h = range_copy(15,25)
for i in h:
    print(i)

	
#	5.	Գտեք string-ը համահունչ է թե ոչ
#		Օրինակ 'abcba', '12321' 
def is_symetric(str):
    str_length = len(str)
    step = 0
    while step < str_length // 2:
        if str[step] == str[str_length - 1 - step]:
            step += 1
            continue
        else:
            return False
    return True
		
#	6.	>>> def is_symmetric(arg):
#		...		.....
#		...		.....
#		...		.....
#		>>>	
#		>>> x = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
#		>>> y = {...} # dict comprehension
#		
#		Լրացրեք բաց թողնված կոդը, is_symmetric function-ը պետք է օգտագործեք y-ը ստանալու ժամանակ։


print(is_symetric('asddsa'))


x = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
y = {item: is_symetric(item) for item in x}
print(y)

#Research
#	1.	__iter__ method:
#answer  __iter__ method@ veradarcnum e iterator objectneric voronc vra hnaravor e linum next method@ kanchel
#	2.	Գրեք մեր անցած iterable data type-երը:
#answer    dict,set,tuple,string,list
#	3.	Գրեք մեր անցած sequence data type-երը:
#answer      list,tuple,string,range
#	4.	Գրեք sequence-ի և iterable-ի տարբերությունները:
#answer   bolor sequence datat typer@ voroshaki indexavorum unem isk iterablner@ voch bolor@