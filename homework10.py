#1.      >>> my_name = 'name'
#		>>>	
#		>>> def f1():
#		>>>		....
#		>>>	
#		>>> f1()
#		>>> print(my_name)
#		My real name
		
#		f1() function-ում լրացրեք կետերը այնպես որ my_name-ի արժեքը փոխվի:

my_name = 'name'
def f1():
    global my_name
    my_name = 'Grigor'
    
f1()
print(my_name)

		
#	2.	users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza", "Janna", "Armen", "Lilit"]
#		long_word = 'dzaynaskavarakavacharanoc' # google եմ արել :)
#		last_names = ("Watson", "Richards", "Richardson", "Saunders", "Watson", "Young", "Saunders")
		
#		Գրեք function որ ընդունում է 1 parametr sequence_object(ցանկացաց հաջորդականություն) և
#		գտնում է բոլոր կրկնվող անդամները և վերադարցնում դրանց list-ը.(Գտնելու համար մեթոդներից չօգտվել):
#		Ստուգեք եթե sequence_object-ի արժեքը int փոխանցվի վերադացրեք 'please send sequence object':

def f(obj):
    if type(obj) == 'int':
        return 'please send sequence object'
    result = set()
    di = {}
    for elem in obj:
        if elem in di:
            result.add(elem)
            di[elem] += 1
        else:
            di[elem] = 1
    return result
				
#	3.	Գրեք function որ ընդունում է թիվ ցանկացաց թվանշանների քանակով և վերադարցնում թվանշանների գումարը և տպեք:
#		(default method-ներից չօգտվել)

check = 15646515
def char_sum(arg):
    num = str(arg)
    sum = 0
    for item in num:
        sum += int(item)
    return sum
print(char_sum(check))


	
#	4.	Գտնել 1-100 թվերի մեջ եղած բոլոր պարզ թվերը, ավելացնել list-ում և վերադացնել:

def is_prime(n):
    if n < 2:
        return False
    li = []
    for j in range(2,n):
        for i in range(2, int(j ** 0.5 + 1)):
            if j % i == 0:
                break
        else:
            li.append(j)
    return li
print(is_prime(100))
#	
#	5.	1 2 3 5 8 13 21 ... (Fibonacci number)
#		Գրեք function որը ընդունում է n parametr և վերադարցնում է Fibonacci-ի հաջորդականության n-րդ թիվը


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

	
#Research
#	1.	Python Function Annotations

# answer functioayi argumentneri masin informacia e avelacnum
#	2.	Function-ի parametrs *args, **kwargs
#answer args u kwarg@ tuyl en talis grel ansman qanaki argumentneric functiayi hamar
#*args grvum e sovorakan argumentneric ev default argumentneric heto ev veradarcum e avel argumentr@ tupli tesqov 
#**kwargs@ grvum e verchum ev veradarcnum dictionalri drvats argumetnerov
# orinak    def f(15,'str - sovorakan argumentner,name='grigor' default arjeqov argumentner, 15,26,8 *args,x=8,y=485 **kwargs)