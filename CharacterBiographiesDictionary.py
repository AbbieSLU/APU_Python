#"samplecharacterbio1" dictionary items containing biographical information for my first constructed fictional character named Johnathan Gardner.
samplecharacterbio1 = { "charactername1":'[Name]: Johnathan Gardner', "charactergender1":'[Gender]: Male', "characterage1":'[Age]: 19', "characterhaircolor1":'[Hair Color]: Black', "charactereyecolor1":'[Eye Color]: Blue' }

#assigned variables: 'a' for representing the keys of the "samplecharacterbio1" dictionary's items and 'b' for representing the descriptive values of its items.
a = samplecharacterbio1.keys()

b = samplecharacterbio1.values()

#Two additional items added to the already existing "samplecharacterbio1" dictionary.
samplecharacterbio1["characteroccupation1"] = '[Occupation]: University Student'

samplecharacterbio1["charactermajor1"] = '[Major]: Psychology'

#for statement for running these lines of code in order to display the values for the "samplecharacterbio1" dictionary in a top to bottom structured format. 
for a, b in samplecharacterbio1.items():
    if "characterhaircolor1" in samplecharacterbio1:      #elif statement for executing the desired output values if the desired condition for the variables 'a' and 'b' assigned within these specified parameters is successfully met.
        print(b)
    elif "characteroccupation1" in samplecharacterbio1:
        print(a, b)
    else:
        print(a)

print() #adds a blank line of space separating the two dictionaries when the code is executed.


#"samplecharacterbio2" dictionary items containing biographical information for my second constructed fictional character named Allison Walters.
samplecharacterbio2 = { "charactername2":'[Name]: Allison Walters', "charactergender2":'[Gender]: Female', "characterage2":'[Age]: 23', "characterhaircolor2":'[Hair Color]: Brown', "charactereyecolor2":'[Eye Color]: Green' }

#assigned variables: 'c' for representing the keys of the "samplecharacterbio2" dictionary's items and 'd' for representing the descriptive values of its items.
c = samplecharacterbio2.keys()

d = samplecharacterbio2.values()

#Two additional items added to the already existing "samplecharacterbio2" dictionary.
samplecharacterbio2["characteroccupation2"] = '[Occupation]: Doctor'

samplecharacterbio2["characterdepartment2"] = '[Department]: Optometry'

#for statement for running these lines of code in order to display the values for the "samplecharacterbio2" dictionary in a top to bottom structured format. 
for c, d in samplecharacterbio2.items():
    if "charactermajor2" in samplecharacterbio2:     #elif statement for executing the desired output values if the desired condition for the variables 'c' and 'd' assigned within these specified parameters is successfully met.
        print(c, d)
    elif "characterhobby2" in samplecharacterbio2: 
        print(c)
    else:
        print(d)

print() #adds a blank line of space separating the two dictionaries when the code is executed.


#"characterbioinfo" dictionary items containing a sequence of values inputted by the user in order to construct a fictional character of their very own through a series of prompts.

characterbioinfo = { "name":input('I hope you liked those two sample character biography templates that I provided as reference! How about trying your hand at constructing your very own character with these few simple steps!'
                     'Let`s start by having you enter a name for your envisioned character!' '[Please Enter A Name For Your Character]: '), "gender":input('What is your character`s gender?' '[Enter Your Character`s Gender]: '),
                     "age":input('How old is your character?' '[Enter Your Character`s Age]: '), "hair color":input('Now what is the color of your character`s hair?' '[Enter A Hair Color For Your Character]: '),
                     "eye color":input('What is the color of your character`s eyes?' '[Enter An Eye Color For Your Character]: ') }

#assigned variables: 'e' for representing the keys of the "characterbioinfo" dictionary's items and 'f' for representing the descriptive values of its items.

e = characterbioinfo.keys()

f = characterbioinfo.values()

#Two additional items added to the already existing "characterbioinfo" dictionary.
characterbioinfo["occupation"] = input('What is your character`s occupation?' '[Enter Your Character`s Occupation]: ')

characterbioinfo["department/major"] = input('What is the name of the department in which your character works or what is the major that they are pursuing in school?' '[Enter Either Your Character`s Work Department or School Major]: ')

print()

#for statement for running these lines of code in order to display the values for the "characterbioinfo" dictionary in a top to bottom structured format. 
for e, f in characterbioinfo.items():
    if "career" in characterbioinfo:     #elif statement for executing the desired output values if the desired condition for the variables 'e' and 'f' assigned within these specified parameters is successfully met.
        print(e)
    elif "eye color" in characterbioinfo:
        print("Your character`s", e, "is", f, ".")
    else:
        print(e, f)
