import random

brands = ["GIORGIO ARMANI", "GUCCI", "PRADA", "LOUIS VUITTON", "MICHAEL KORS", "HERMES", "FENDI", "BALENCIAGA", "GIANNI VERSACE", "BURBERRY", "CALVIN KLEIN", "DOLCE & GABBANA", "GUESS", "RALPH LAUREN", "TOMMY HILFIGER", "SAINT LAURENT"]

selection = random.choice(brands)
answer = selection

jumble = list(selection)

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,


guess = raw_input("\nWhat kind of brand is jumbled?")
guess = guess.upper()

if guess == answer:
    print("Got It")
else:
    print (answer)
