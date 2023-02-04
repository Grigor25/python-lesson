#1. Ունենք օրինակ users_list = ['Vardan', 'Vazgen', 'Jarviz']
#	1. print արեք list-ի բոլոր անդամները:
#	2. Ինչպես կարող ենք փոխել 'Vazgen'-ը մեկ այլ անունով:
users_list = ['Vardan', 'Vazgen', 'Jarviz']

print(users_list)

users_list[0] = 'Grigor'
 
 #2. Ունենք 2 list 
  #  	x = [1,2,3,4,5,6]
	#z = [7,8,9,10,11]
	#Ինչպես կարող ենք իմանանալ դրանց ըդհանուր երկարությունը:
x = [1,2,3,4,5,6]
z = [7,8,9,10,11]
print(len(x) + len(z))
 
 #3. Նշեք ինչ ընդանուր ֆունկցիաներ գիտեք հաջորդականությունների համար ու ինչ են իրանք վերադարցնում:

 #len() -> veradarcnume e erkarutyun@
 #list() -> stextsum e nor hajordakanutyun
 # copy() -> copi e anum hajordakanutyun@
 # remove() ->jnjum e hajordakanutyuniic element
 #append() -> avelacnum e element
 #reverse() -> shrjum e hajordakanutyun@
 #sorted() -> sortavorum e
 
 
 #4. Ստեղծել երկու input():
#	Առաջինը պետքա ունենա սենց հրավերքի տեքստ - how many words do you want to type?
#	Իսկ երկրորդը պետքա ունենա սենց հրավերքի տեքստ - write a word
#	Արդյունքում պետքա print անենք մեր երկրորդ input-ից ստացած բառը բազմապատկած առաջին input-ից ստացած քանակությամբ:

quantity = input('how many words do you want to type?')
word = input('write a word')
print(word*int(quantity))
 
 #5. Ունենք users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
#	Հարկավոր է input()-ի միջոցով ավելացնել նոր user-ի, որից հետո պետք է տպել հին(исходный) users_list-ը և նոր users_list-ը:
	

users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
new_user = input('type new user')
new_users_list = users_list.copy()
new_users_list.append(new_user)
print(new_users_list)



users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
new_users_list = users_list.copy()
new_users_list.append(input('add new user'))
print(new_users_list)
 #6. Ունենք users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
#	Ստեղծել input(), որը կունենա սենց հրավերքի տեքստ 
#		'Your users ["Vazgen", "Chris Tacker", "Nikola Tesla"]'
#		'who do you want to remove ?'
#	Հետո գրեք են user-ի անունը որին ուզում եք հեռացնել:
#	Արդյունքում ստանանք սենց տեքստ
#		'User NIKOLA TESLA(մեծատառ) is removed'
 #       'Your users ["Vazgen", "Chris Tacker"]'


users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
removing_user = input(
		"""Your users ["Vazgen", "Chris Tacker", "Nikola Tesla"]'
		'who do you want to remove ?""")
users_list.remove(removing_user)
		
print(f"""User {removing_user.upper()} is removed'
       'Your users {users_list}""")	
 
 #7. Ունենք numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  #  Գտնել զույգ թվերի գումարը:

  
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers_list[1::2]))





#Research
 #1. list-ի որ մեթոդով կարող ենք գտնել տրված արժեքի index-ը:

list.index()

 #2. Ինչ է անում del արտահատությունը ու ինչով է տարբերվում remove()-ից:

#del hraman@ method chi removi nman
#remove-ov karog enq jnjel listi mek element isk del-ov mi qani kam bolor@
#remove@ @ndunum eparametr listgi arjeq@ isk del@ elementi index@