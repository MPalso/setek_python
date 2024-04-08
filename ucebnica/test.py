
#BMI KALKULACKA
""" 
vyska = input("vyska v metroch \n")
vaha = input("vaha: \n")
print(vyska)
print(vaha)
bmi = int(vaha) / float(vyska)**2
bmi = int(bmi)
print("Vase BMI je " + str(bmi))
"""



#NAHODNA STRANA MINCE
""" 
import random
strana_mince = random.randint(0,1)
if strana_mince == 1:
    print ("hlava")
else:
    print ("orel") 
"""

## List

""" 
clenovia = ["Martin", "Tibor", "Tete"]
print(clenovia)
print(clenovia[0])
print(clenovia[1])
print(clenovia[2])
""" 
## Menit polozku v LIST
""" 
clenovia[1] = "Lia"
print(clenovia)
"""
## Pridat obsah
"""
clenovia.append("Katka")
print(clenovia)
"""
##Pridat viac poloziek
"""
clenovia.extend(["Bea","Blabla"])
print(clenovia)
"""
##Odstranujeme polozku
"""
clenovia.remove("Blabla")
print(clenovia) """

#NAHODNY VYBER MENA
""" 
import random
mena = input("Napis mi mena vsetkych a oddel ich ciarkov\n")

list_mena = mena.split(", ")
print(list_mena)

nahodne_cislo = random.randint (0, len(list_mena)-1)
print(nahodne_cislo)
print(f"{list_mena[nahodne_cislo]} bude dnes platit ucet")  """


 #PISKORKY
"""
set1 = ["🟨", "🟨", "🟨"]
set2 = ["🟨", "🟨", "🟨"]
set3 = ["🟨", "🟨", "🟨"]
all_sets = [set1, set2, set3]
print(f"{set1}\n{set2}\n{set3}\n")
position = input("Zadajte suradnice: ")

num1 = int(position[0])
num2 = int(position[1])

all_sets[num1][num2] = "X"

print(f"{set1}\n{set2}\n{set3}\n")
 """

#KAMEN PAPIER NOZNICE
""" 
import random

kamen ="kamen"
papier = "papier"
noznice = "noznice"

vsetko = [kamen, papier, noznice]

vyber = int(input("Co si vyberies? kamen = 0, papier = 1, noznice = 2. Zadaj cislo \n"))
potvrd_vyber = vsetko[vyber]

pocitac = random.randint(0, 2)
potvrd_pocitac = vsetko[pocitac]

print(f"Ty mas {potvrd_vyber}")
print(f"PC ma {potvrd_pocitac}")

if vyber == pocitac:
    print("remiza")
elif vyber == 0 and pocitac == 1:
    print("Vyhrava pocitac lebo ma papier a ty kamen")
elif vyber == 1 and pocitac == 2:
    print("Vyhrava pocitac lebo ma noznice a ty papier")
elif vyber == 2 and pocitac == 0:
    print("Vyhrava pocitac lebo ma kamen a ty noznice")
else:
    print("Vyhravas lebo si super!")  """


 # GENERATOR HESIEL
"""
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_char = ['%','#','$','!','&','(',')','*','+','?']

print ("Generator hesiel")
num_letters = int(input("Kolko pismen chcete vo svojom hesle\n"))
num_numbers = int(input("Kolko cisiel chcete mat vo svojom hesle\n"))
num_special_char = int(input("Kolko specialnych znakov chcete mat vo svojom hesle\n"))

result = []

for index in range(0, num_letters):
    random_number = random.randint(0, len(letters)-1)
    result.append(letters[random_number])

for index in range(0, num_numbers):
    random_number = random.randint(0, len(numbers)-1)
    result.append(numbers[random_number])

for index in range(0, num_special_char):
    random_number = random.randint(0, len(special_char)-1)
    result.append(special_char[random_number])

random.shuffle(result)

result_password = ""

for one_character in result:
    result_password += one_character

print(result_password)
 """



# PRIEMERNA VYSKA ZADANA UZIVATELOM
"""
vyska = input("Zadajte vysku ludi odelenu ciarkou a medzerou\n")
list_vyska = vyska.split(", ")
cislo = 0

for jedna_vyska in list_vyska:
    cislo = cislo + int(jedna_vyska)

average = cislo / len(list_vyska)
print(f"Priemerna vyska je: {average}") """


# NAJVACSIE SKORE V TESTE

""" score = (98, 50, 25, 78, 92)
print(min(score))
print(max(score)) """

## tu si to rozdelim na LIST

""" score = input("Napiste skore jednotlivych studentov odelene ciarkou a medzerou:\n")
score_list = score.split(", ")
print(type(score_list))
print(score_list)
""" 
## spravim z toho int
""" 
score_list_number = []

for index in range(0, len(score_list)):
   score_list_number.append(int(score_list[index]))
""" 
##cyklom for prejdem vsetky cisla v liste a vyberieme maximu
""" 
maximum = 0

for cislo_z_listu in score_list_number:
   if cislo_z_listu > maximum:
      maximum = cislo_z_listu

print(f"Maximum je {maximum}")
 """
#GAUSIVO cislo ...pozri wikipediu

""" suma = 0

for jedno_cislo in range (1, 101):
    ## suma = suma + jedno_cislo
    ## skrateny zapis
    suma += jedno_cislo

print(suma)  """


#HADACIA HRA
##Hadanie postav z filmu herry potter

""" import random
characters = ["Harry", "Ron", "Hermiona"]
character = characters[random.randint(0, len(characters)-1)]
guess = ""
guess_count = 2
print("Vitaj v hadacej hre HP")
print(f"Pocer pokusov: {guess_count}")  


while character != guess:
    if guess_count != 0:
        guess = input("Uhadni postavu z filmu HP\n")
        guess_count -= 1  
    else:
        print("Uz nemas pokusy")
        break
    if character == guess:    
        print(f"Spravne uhadol si, si super. Hadane slovo bolo {character}")
 """

 #HANGMAN alebo OBESENEC

""" import random
from test2 import stages
##Generovanie nahodne slova
words = ["harry", "ronald", "albus", "hermiona"]
random_word = words[random.randint(0, len(words)-1)]
##print(random_word)

##generovani podrzitok
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")

#zivoty
lives = 6
print(stages[lives])

printedWord = " "
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord) 
##po zadani pismena uzivatelom, ho prevediem na male pisemno, keby ho zadal velkym. na to sluzi .lower()
    
while "_" in hidden_word:   
    guess = input("Zadaj hadane pisemno\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess
  
# kontrola zivota

    if guess not in random_word:
        lives -= 1
        print(stages[lives])
        print(f"pocet zivotov je {lives}")
        if lives == 0:
            print("Prehral si")
            break


##vypisanie slova v normalnej podobe a nie ako list. 
    printedWord = " "
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord) 
    print("_________________________________")

#kontrola vytaztva
    if "_" not in hidden_word:
        print("Vyhral si!!") """


#FUNKCIE
## Kalkulacka plochy na natieranie
""" import math

'''musi sa mi vyratat

--zada uzivatel
vyska steny: 6
sirka steny: 3
jedna plechovka pokryje 5m2
zaokruhlovanie smerom nahor nejaky round
'''

vyska_steny = int(input("Zadaj vysku steny v m2 : "))
sirka_steny = int(input("Zadaj sirku steny v m2 : "))
obsah_plechovky = 5

def kalkulacka(vyska_steny=vyska_steny, sirka_steny=sirka_steny, plechovky=obsah_plechovky):
    plocha = vyska_steny * sirka_steny
    plechovky = math.ceil(plocha / 5)
    print(f"Budete potrebovat {plechovky}")

kalkulacka() """

#PRVOCISLO

""" def kontorla_prvocisla(number):
    result = "Je to prvocislo"
    for one_number in range(2, number):
        if number % one_number == 0:
            result = "nie je to prvocislo"
    print(result)

n = int(input("Zadaj cislo : "))
kontorla_prvocisla(n) """

###pokracujem
##66. Python - Tvoříme vlastní šifrovací nástroj, Caesarova šifra 17:07