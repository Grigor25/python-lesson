#1. Ունենք 2 set	 x = {1,2,4,5,6}
#		         y = {5,6,7,8,9}	
#		1.1 Գտնել այն թվերը որոնք կան երկու set-ում

x = {1,2,4,5,6}
y = {5,6,7,8,9}

x.intersection(y)

#		1.2 Գտնել այն թվերը որոնք կան x-ում բայց չկան y-ում

x.difference(y)
	
#	2. x-ից ջնջեք x-ի և y-ի հատումը:

x = {1,2,4,5,6}
y = {5,6,7,8,9}	
removed_values = x.intersection(y)
x = x.difference(removed_values)
y = y.difference(removed_values)
print(x,y)
	
#	3. default ինչ պառամետր է ընդնում open() ֆունկցիան եթե իրան ոչինչ չփոխանցենք:

'r'
	
#	4. 
#	   4.1 Ստեղծել 2 file python-ի կոդի միջոցով: 
#	       Յուրաքանչյուր file-ի մեջ գրել file-ի անվան հետ կապված տեքստ
	
#	   4.2 Արդեն ստղծված ֆայլերում ավելացնել տեքստ առանց հին տեքստը ջնջելու:
file_path_python = 'python.txt'
file_path_js ='js.txt'
file_python = open(file_path_python,'a')
file_python.write('Python programming language')
file_js = open(file_path_js,'a')
file_js.write('Js programming language')
file_python.close()
file_js.close()
file_python = open(file_path_python,'r')
file_js = open(file_path_js,'r')
print(file_js.read(),file_python.read())
file_js.close()
file_python.close()
		    

file_python = open(file_path_python,'a')
file_python.write('Python')
file_js = open(file_path_js,'a')
file_js.write('Js')	  
file_js.close()
file_python.close() 
#	   4.3 Ունենանք input սենց հրավերքի տեսքով 'which file do you want to read?'
#	       file-ի անունը գրելուց հետո print արեք արդեն ստեղծված երկու file-ից համապատասխան file-ի տեքստը(file-ը բացել with-ի միջոցով):
#
selected_file = input('which file do you want to read')
with open(selected_file) as file:
    print(file.read())
 #       5.  Ունենք սենց list users = [
#				  	{
#					  'first_name': 'Jorj',
#					  'last_name' : 'Bush',
#					  'age':55
#					},

#					{
#					  'first_name': 'James',
#					  'last_name' : 'Bond',
#					  'age':100
#					}
#				]
#		ավելացրեք նոր ֆայլում user-ների տվյալնեը հետեվյալ ֆոռմատով
		
#		user 1: first_name = Jorj, last_name = Bush, age = 55
#		user 2: first_name = James, last_name = Bond, age = 100

dicts = { 'first_name': 'Jorj',                                                     
           'last_name' : 'Bush',                                                    
           'age':55                                                                 
         }                                                                          
dicts_2 = {	 'first_name': 'James',                                                 
			  'last_name' : 'Bond',                                                 
			  'age':100                                                             
	    }                                                                           
with open('user.txt','a') as file:                                                  
    file.write('user 1:' + str(dicts).strip("{}").replace(':',' ='))                
    file.write('user 2:' + str(dicts_2).strip("{}").replace(':',' ='))              
with open('users.txt','r') as file:                                                 
    print(file.read())                                                              
                                                                                    
                                                                                    
                                                                                    


#Research
#	1. isdisjoint() մեթոդը
#answer   erku seterum nuyn item@ chgtnelu depqum veradarcnum e True hakarak depqum veradarcnum em False
#	2. remove()-ի ու discard()-ի տարբերությունը

#discard & remov@ erkusnel jnjum en value set-um tarberutyun@ discard@ vorpes parametr trvats value chlinelu depqum error chi tali hamematabar removi