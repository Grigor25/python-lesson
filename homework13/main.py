import auth
user_type = input("Please write what you want to do?")
if user_type == 'signin':
    auth.signin()
elif user_type == 'signup':
    auth.signup()

#1. Ինչ կլինի եթե մեր գրած ծրագրում ստանանք exception ու չփորցենք handle անել:

#asnwer error kstananq


#	2. Նշեք ինչ արհեստական եղանակներ գիտեք exception առաջացնելու:

#answer raise Exeprion()   assert

#Research
#	1.      Ինչպես կարող ենք raise-ի միջոցով փոխանցել message exception-ին:
#answer
try:
    raise SyntaxError
except SyntaxError as error:
    print(str(error))
#	2.	Ուսումնասիրեք math package-ը և դուրս գրեք 3 ձեզ դուր եկած և ձեր կարծիքով ամենաօգտակար method-ները:
#math.pow()
#math.sqrt()
#math.ceil()