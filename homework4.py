
 #1. Նշեք copy-ի ու deepcopy-ի տարբերությունը:

#answer copy-n mi level e copy anum  isk deep_copin qani level irar mech ka

 #2. Ունենք սենց list x = [1,2,5, [8,9,10]]
 #   Վերագրեք y-ին x այնպես, որ x-ի յուրաքանչյուր index-ը փոխելուց y-ը չփոխվի (առանց օգտագործելու deep_copy):
x = [1,2,5, [8,9,10]]
y = x[3]
z = y.copy()
j = x.copy()
j[3] = z
print(j,x)

 
 
 #3. Ունենք սենց մի հատ tuple - ('Erk','Ereq','Choreq','Hing','Urb',['Shb'])
  #  Ինչպես կարանք ավելացնենք 'kiraki'-ին ['Shb']-ի հետ նույն լիստում և բացատրեք թե ինչու error չենք ստանում: 
  
tuple[5].append('kiraki')

# error chi tali vorovhetev menq tupli arjeq chenq poxum nuyn listna mnum uxaki liti mech enq popoxutyun anum id-i popoxutyun chi tenum
	
 #4. Ունենք փոփոխականներ
#	name = 'My name'
#	last_name = 'My last name'
#	patronymic = 'My father name'
	
#	3 վերագրումները գրեք մեկ տողով:

name,last_name,patronymic = ('My name','My last name','My father name')

	
 
 #5. Ունենք սենց users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
#	Ինչպես կարող ենք փոխել users_tuple-ի ինչ որ value:
	
#answer tupli arjeq chenq kara poxenq    

 #6. Նախ արեք resaearch-ի հատվածը որպեսզի կարողանաք անել տնայինը
	
#	Ունենք users_list = [
#			"Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
#			[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
#		]
#	Օգտագործել zip() function-ը այնպես որ ստանանք 
#		[('Lilit', 1, 8, 15),
#		 ('Aren', 2, 9, 16),
#		 ('Janna', 3, 10, 17),
#		 ('Samvel (Sam)', 4, 11, 18),
#		 ('Gohar', 5, 12, 19),
#		 ('Armen', 6, 12, 20),
#		 ('Luiza', 7, 14, 21)]		


users_list = [
			"Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
			[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
		]

new_users = zip(users_list[0:7],users_list[7][0],users_list[7][1],users_list[7][2])

print(list(new_users))


#Research
 # 1. zip() function

 #answer zip funkcian feradarcnum e zip object or@ kazmvats e tuplneric,vorpes parametr trvum en itarablner,hertakanutyamb stextsum e tapler voronc arjeqner@ trvats iteratorn eri hertakan indexov arjeqnern en,erkarutyun @ndunvum e amenakarchh erkarutyun unecov iterator@
#orinak amenakrch@ v tuplne aysinq mer zip objecti erkarutyun@ 2 e 
a = ("John", "Charles", "Mike","Vicky")
b = ("Jenny", "Christy", "Monica", )
v = ("Jenny", "Christy" )

x = zip(a, b, v)

#use the tuple() function to display a readable version of the result:

print(tuple(x))

(('John', 'Jenny', 'Jenny'), ('Charles', 'Christy', 'Christy'))
