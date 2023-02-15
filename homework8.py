 #1.	Ունենք list-եր 
		
#		last_names = ['Adams','Allen','Brooks','Davidson','Sargsyan','Jenkins']
#		armenian_last_names = []
		
#		Օգտվելով while cycle-ից գտեք և ավելացրեք հայկական ազգանունները ըստ yan վերջավորության armenian_last_names list-ում:
		
last_names = ['Adams','Allen','Brooks','Davidson','Sargsyan','Jenkins']
armenian_last_names = []
x = len(last_names)
while x:
    x -= 1
    if last_names[x][-3::] == 'yan':
        armenian_last_names.append(last_names[x])
    else:
        print('No')
print(armenian_last_names)
		
	
#	2.	Ունենք string long_word = 'arevachachapaylatakum':
		
#		Օգտվելով for cycle-ից գտնել թե քանի հատ a կա մեր string-ի մեջ:

long_word = 'arevachachapaylatakum'
a_count = 0
for item in long_word:
    if item == 'a':
        a_count += 1

print(a_count)

	
#	3.  alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		
#		Համարակարել այբուբենի տառերը ըստ կենտ թվերի ձեր իմացած ամենակարճ ճանապարհով և ստացեք dict 
		
#		Օրինակ ՝ {'a': 1, 'b': 3, 'c' : 5, .....}

alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
odd_numbers = []
x = 1
result = dict()

while len(odd_numbers) < len(alpabet):
    if x % 2 != 0:
        odd_numbers.append(x)
        x += 1
    else:
        x += 1
else:
   result = dict(zip(alpabet,odd_numbers))
print(result)

		
#	4.	Գտնել 10 թվի ֆակտորիալը օգտվելով կամ while-ից կամ for-ից

x = 10
result = 1
for item in range(1,11):
    result *= item
print(result)
	
	
#	5.	alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#		Առանց օգտվելու մեթոդներից և ֆունկցիաներից reverse արեք alpabet list-ը cycle-ի և slice-ի միջոցով

alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpabet_length = len(alpabet)
x = 0
while x < alpabet_length / 2:
    alpabet[x],alpabet[alpabet_length - x - 1] = alpabet[alpabet_length - x - 1],alpabet[x]
    print(alpabet[x],alpabet[alpabet_length - 1])
    x += 1
print(alpabet)

#Research
#enumerate() functian stextsum e enumarate tipi object tuplic kam ayl colectic,vori keyer@ tver en sksats 0-ic,erkrord paramtrov karogh enq tal skzbnakan index@