#	1.	
#		1.1	Ունենք db.txt file որի առաջին տողից պետք է ստանալ dict-ի key-եր իսկ մնացաց տողերից վերցնել
#			key-երին համապատասխան value-ները, ստացված dict-երը ավելացնել list-ին և հետո ձեր տվյալները
#			նույնպես ավելացնել list-ին:
#			Ստանալ  նմանատիպ list 
#			users = [	
#					{'first_name':'Smbat', 'last_name':'Paloyan', 'age':'23' ...},
#					{'first_name':'Hovhannes', 'last_name':'Stepanyan', 'age':'25 ...},
#					{'first_name':'my name', 'last_name':'my last name', 'age':'my age' ...}		
#				]
#		1.2	Գրեք function որը ընդունում է 2 parameter 1.1-ում ստացված users-ը և **kwargs:
##		

with open('db.txt') as f:
    users = []
    users_list = []
    for index,str in enumerate(f):
        users.append(str.split(','))
        print(str)
    discr = users.pop(0)
    for elem in users:
        users_list.append(dict(zip(discr,elem)))
    print(users_list)


def 
##		
#	2.	Ունենք list numbers = [[[[[10]]]]]
numb = [[[[[10]]]]]
def items_sum(li):
    for item in li:
        if type(item) == int:
            print(item)
            return item
        else:
             items_sum(item[0])
    return item
items_sum(numb)

##		
		
#	3.	Ունենք list numbers  = [1, 2, [3, 4], [5, 6, [10, 19]]]
#		Recursion function-ի միջոցով ստանալ բոլոր item-ների գումարը:
numbers = [1, 2, [3, 4], [5, 6, [10, 19]]]
result = 0
def items_sum(li):
    global result
    for item in li:
        if type(item) == int:
            result += item
        else:
             items_sum(item)
    return result

print(items_sum(numbers))

#Research
#	1.	lambda functions

#answer lambda funcian @ndunum e cankacats qanaki argument bayc unenum e miayn mek artahaytutyun vori arjeq@ veradarcnum e