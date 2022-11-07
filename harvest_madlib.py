# -*- coding: utf-8 -*-

print("Lets do a madlib!")

last_name = input( 'What is your last name? ')
noun = input('Give me a harvest noun: ')
noun2 = input("Let's use another noun: ")
noun3 = input("One more makes three nouns: ")
holiday = input("What's your favorite holiday? ")
noun4 = input("What's a noun associated with your favorite holiday? ")
adj = input("Now we need an adjective: ")
plural_noun = input("Followed by a plural noun: ")
noun5 = input("Yes, this story is noun heavy, give us another one: ")
noun6 = input("This is the last noun you will have to think of: ")
adj2 = input("One more adjective: ")
animals = input("Finally, what is your favorite animal? ")

title = " \n HARVEST FESTIVAL \n"
mad_lib = f'''Every Fall there is a Harvest Festival at {last_name} {noun} Farm, 
where there is something for everyone.  You can go to the {noun2} patch where 
you can pick out a {noun3} to decorate for {holiday}. At the {noun4} orchard,
you can pick {adj} {plural_noun} to eat fresh or bake into pies. There is a maze
in the {noun5} field and a {noun6} ride on a big wagon that is pulled by {adj2}
{animals}.'''

print(title)
print(mad_lib)
