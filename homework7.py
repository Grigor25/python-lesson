#1.	Ունենք  list users = [ [] ]
#		if users:
#			print('users exist')
#		else:
#			print('users not found')
			
#		Ինչ կտպի հետեվյալ արահայտությունը և ինչու:

# answer ktpi users exist   vorovhetev users list@ datark chi mech@ 0 indexum ka list
		
#	2.	Ունենք list pythonists = ["Bush", "Jarvis", "Oxxi", "Buffon", "Vardan"]
		
#		2.1 Ստուգեք ձեր անունը կա list-ում թե ոչ, եթե կա print արեք , եթե ոչ ավլեացրեք ձեր անունը և print արեք:

pythonists = ["Bush", "Jarvis", "Oxxi", "Buffon", "Vardan"]

if 'Grigor' in pythonists:
    print('Grigor' in pythonists)
else:
    pythonists.append("Grigor")
    print(pythonists)
		
#		2.2 Ստուգեք եթե pythonists-ների քանակը քիչ է 7-ից եվ մեծ է 5-ից print արեք նրանց քանակը,
#			եթե փոքր է 5-ից print արեք "appended new user" և ավլեացրեք նոր user-ի
#			իսկ եթե 7-ից մեծ է print արեք "user removed"  և ջնջեք ինչ որ user-ի

if 5 < len(pythonists) < 7:
    print(len(pythonists))
elif len(pythonists) < 5:
    print("append new user")
    pythonists.append('Artak')
elif len(pythonists) > 7:
    print('user removed')
    pythonists.pop()


print(pythonists)
			
# len(pythonists) < 7 and len(pythonists) > 5 Hov pastoren ste senc chenq kara grenq ha



#	3.  while-ի միջոցով print արեք 0-21(աճման կարգով) թվերի միջեվ գտնվող զույգ թվերը:
#		Օրինակ  2
#			4
#			6
#			8
#			...
	
x = 0

while x <= 21:
    if x % 2 == 0:
        print(x)
        x = x + 1
    else:
        x = x + 1
            
#	4.	while-ի միջոցով print արեք 20-1(նվազման կարգով) թվերը և դիմացը քառակուսին:
		
#		countinue-ի միջոցով բաց թողեք 17 թիվը:
		
#		Օրինակ  20-400
#			19-361
#			18-324
#			...
	
x = 20

while x >= 0:
    if x == 17:
        x = x - 1
        continue
    else:
        print(x,x**2)
        x = x - 1



#	5.	while-ի միջոցով print արեք 1-50-ի միջեվ ընկած 3-ի բաժանվող առաջին 10 թվերը և դուրս եկեք while-ից:

x = 1
y = 0

while x < 50 and y < 10:
    if x % 3 == 0:
        print(x)
        y = y + 1
        x = x + 1
    else:
        x = x + 1

#Research
#	1. Ինչպես է աշխատում else-ը while-ի հետ