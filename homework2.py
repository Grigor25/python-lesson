
# 1 Ինչ type կվերադարցնի հետեվյալ արտահայտությունը ու ինչ պատճառով
#  1 + 2.0 +3
6.0
# answer kveradzrcni float tiv 6.0  vorovhetev tveric mek@ float tiva

# 2 Ունենք հետեվյալ արտահայտությունը
# 	2 * 3 + 4
#  Ինչպես կարանք փոխենք արտահայտությունը այնպես որ առաջինը գումարի հետո նոր բազմապատկի

# answer   vercnenq pakagtseri mech 2*(3 + 4)   arajin@ katarvum e mish pakagtseri mechi gortsoxutyun@

2*(3 + 4)

# 3. Ինչպես կարանք կլորացնենք 2.555 որ ստանանք 2.56

# answer
round(2.555, 2)

# 4. Ունենք 2 բառից կազմված ինչ որ string օրինակ `'Hello world':
#  Օգտագործելով string-ի մեթոդներից պետքա ստանալ տեքստի հակառակ ձեվը - "world Hello"

# answer  "Hello world"[6:len("Hello world")] + " " + "Hello world"[0:5]

name = "Hello world"
name[6:len(name)] + " " + name[0:5]

# 5. Գնացեք այս հղումով (https://www.lipsum.com/) ու այնտեղ առաջին տեքստում կտեսնեք մոտավորապես սենց տեքստ
#   s1 = 'Lorem Ipsum is  ...  dummy text of the printing and typesetting industry.
#   Lorem Ipsum has been the industry's standard dummy text ever since the ...s,
#  when an unknown printer took a ...  of type and scrambled it to make a type
#   specimen book'.
# Օգտվելով առաջին տեքստից լրացրեք բառերը օգտագործելով string-ի format()-ի 3 գործիքները
# 1. "" % ()


word_one = 'simply'
word_two = '1500'
word_three = 'galley'


text = """Lorem Ipsum is %s  dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industrys standard dummy text ever since the %ss,
 when an unknown printer took a %s of type and scrambled it to make a type specimen book."""

print(text % (word_one, word_two, word_three))


# 2. .format


word_one = 'simply'
word_two = '1500'
word_three = 'galley'


text = """Lorem Ipsum is {0}  dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industrys standard dummy text ever since the {1}s,
 when an unknown printer took a {2} of type and scrambled it to make a type specimen book."""

print(text.format(word_one, word_two, word_three))

# 3. f""

word_one = 'simply'
word_two = '1500'
word_three = 'galley'


text = f"""Lorem Ipsum is {word_one}s  dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industrys standard dummy text ever since the {word_two}s,
 when an unknown printer took a {word_three} of type and scrambled it to make a type specimen book."""

print(text)


# 6. Ունենք սովորական int type-ի թիվ օրինակ` 97
#  Ինչպես կարող ենք ստանալ առանձին 7-ը հետո 9-ը օգտագործելով միայն օպերատորներ եվ թվեր (string չդարձնեք, եղավ՞ ։)

start_number = 97
# % operator@ kta mnacord@ 7@
print(start_number % 9)

#  // operator@ kta amboxch mas@

print(start_number // 10)

# 7. Ունենք սովորական int type-ի թիվ օրինակ` 123
#  Պետքա բոլոր թվերի գումարը ստանանք 6 օգտագործելով միայն օպերատորներ եվ թվեր (նորից, string չդարձնեք :) )

number = 123

print(round(number / 100) + (round(number / 10) % 10) + (number % 10))


# Research
# 1. Փորձեք գտնել թե ոնց կարանք վերցնենք միանգամից մեր string-ի վերջին տառը:
# answer 1- index@ kveradarcni stringi verchin char@

name = 'Grigor'
print(name[-1])
print(name[len(name) - 1])


# 2. Փորձեք հասկանալ ինչ է անում strip() մեթոդը:

# answer str.strip() method@ stringi mech jnjum e mer tvats parametrov char@.default vercnum e space

fruit = '    ap   ple       '
print(str.strip(''))

# ktpi 'ap    ple' kvercni skzbic ev verchic minchev mer tvats parametreri arajin chamnknum@ chmanknum@


# 3. Փորձեք հասկանալ ինչ են անում """-ը, օրինակ """some long
# text"""

# tuyl e lasis grel mi qani toxi vra mets texteri hamar
