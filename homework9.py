#1.	Գրեք function, որը ընդունում է 3 parameters name, last_name, age(integer)
#		ու format-ի միջոցով կտպի
			
#		Օրինակ 'hello my name is Vazgen, my last name is Adunc, I am 10 years old:
def person(name, last_name, age):
    print(""" my name is {0}, my last name is {1}, I am {2} years old""".format(name, last_name, age))

person('Grigor','Manukyan',28)
		
#	2.	Գրեք function, որը ընդունում է 3 parameters text, old_character, new_chararcter
#		և կփոխարինի բոլոր old_character-ը new_chararcter-ով (old_character-ը և new_chararcter-ը պետք է լինեն 1 տառ)
#		առանց օգտվելու default function-ից և method-ից:
		
def char_change(str,old_character,new_character):
    result = ''
    for elem in str:
        if elem == old_character:
            result += new_character
        else:
            result += elem
    return result            
# Hov upper caseri pah@ chem naye


#	3.	Գրեք function, որը ընդունում է 2 parameters file_name, list_of_texts  
#		function-ը file_name-ով file պետք է սարքի և file-ում գրի list_of_texts-ում եղած արժեքները
#		file_name parameter-ի default արժեքը պետք է լինի 'text.txt':

def wr(list_of_text,file_name='text.txt'):
    with open(file_name,'w') as written_file:
        with open(list_of_text) as reading_file:
            written_file.write(reading_file.read())
		
#	4.	Գրեք function, որը ընդունում է int type-ի parameter և print է անում թիվը պարզ է թե ոչ:

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True

#Hov es internetic em ogtve
	
#Research
#	1. Ինչպես գրել function-ի documentation և կանչել help function-ով:



#anwser  """  """   erek skobkeqi mech anyem mi qani toxi hamar  kanchel help(func)