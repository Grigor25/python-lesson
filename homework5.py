#1.  Ունենք սենց dict
#			user = {
#				'name':'Jarviz',
#				'age' : '100',
#				'professions':['robot', 'dancer']
#				'test_result':[14,5,8,99,12,2,3,5,4]
#			}
#			
#	    1.1 Ինչպես կարող ենք տպել 'robot'-ը ու փոխել 'dancer'-ը:
#	    1.2 Սորտավորեք test_result-ը ըստ նվազման:
user = {
		'name':'Jarviz',
		'age' : '100',
		'professions':['robot', 'dancer'],
		'test_result':[14,5,8,99,12,2,3,5,4]
		}

print(user['professions'][0])
user['professions'][1] = 'not dancer'
user['test_result'].sort(reverse=True)	
#		
#	2. Ունենք սենց dict 
#			fruits = {
#				"banana": 4,
#				"apple": 2,
#				"orange": 1.5,
#				"pear": 3
#			}
#		2.1 Հաշվել բոլոր մրգերի գումարը
#		2.2 Ավելացրեք ձեր սիրած միրգը ու ինչքան եք իրան գնահատում
fruits = {
			"banana": 4,
			"apple": 2,
			"orange": 1.5,
			"pear": 3
		}	

sum(list(fruits.values()))

fruits['pinancle'] = 15	

#	3.  
#		[
#			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
#			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
#		]
#			
#		3.1 Լրացրեք բաց թողնված value-ները ( is_5g-ի արժեքը պետք է լինի bool type-ի )
#		3.2 Ավելացրեք նոր dict արդեն եղած user-երին, օրինակ ՝ {'car':{'model': '', 'type': '', 'max_speed': ''}}
#		3.3 Տպել is_5g-ին ամեն user-ի համար True է թե False.
#		3.4 x-ին վերագրեք հետեվյալ պայմանների արդյունքում ստացված արժեքը 
#			age մեծ է 18-ից և is_5g-ին հավասար է True կամ first_name-ի մեջ չկա bill և last_name-ի մեջ չկա gates:
#			Հետո տպեք print('chipavorvac e', x)
users = [
			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
		]

users[0] = dict(zip(users[0],['Grigor','Manukyan',28,dict(zip(users[0]['phone'],['Samsung',"+37494404442",False]))]))
users[1] = dict(zip(users[0],['Artavazd','Hakobyan',28,dict(zip(users[0]['phone'],['Iphone',"+37498452236",True]))]))
print(users)

users[0]['car'] = {'model': 'Hundayi','type': 'Elantra','max_speed': '280 km/h'}
users[0]['car'] = {'model': 'Opel','type': 'Vectra','max_speed': '220 km/h'}

print(users[0]['phone']['is_5g'],users[1]['phone']['is_5g'])

x = users[0]['age'] > 18 and users[0]['phone']['is_5g'] == True or 'bill' not in users[0]['first_name'] and 'gates' not in users[0]['last_name']
print('chipavorvats e',x)

#	4. zip()-ի և այլ անհրաժեշտ գործիքների միջոցով ստացեք dict որի key-րը կլինեն ձեր անվան առաջին տառերը իսկ
#	   value-ները հակառակ տառերը, օրինակ ՝ jarvis {'j':'s', 'a':'i', 'r':'v', 'v':'r', 'i':'a', 's':'j'}
name = 'Jarvis'
new_list = list(name)
new_list_copy = new_list.copy()
new_list.reverse()

result = dict(zip(new_list_copy,new_list))

print(result)


#Research
 # 1. setDefault()

 # set default funkcian veradarcnum e vorpes arachin parametr trvats arjin key-i arjeq@,erkord paramer @ndunum e default arjeq ev veradarcnum ayn key chunenalu depqum
  # 2. fromkeys()
  # functian veradarcnum e dictionari vori keyern en arachin parametr trvats arjeq@ karog elinel nayem iterable isk erkrod arjeqov stanum ayd keyeri valuner@.arjeqner@ chlinelu depqum arjeq@ darnum e None 
  # 3. Փորձեք կիրառել մեր անցած ֆունկցիաները dict-ի համար և գրեք արդյունքներիը
 # len(dict)  veradarcnum e dicti keyeri qnanak@
 # zip(dict)
 # typeof({})