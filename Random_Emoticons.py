import random
eyes = [':', '8', 'x', ';']
noses = ['-', '~', 'っ', '^', '\'', ''] #empty string at end will give program an option to randomly produce emoticon without a nose
mouths = ['D', 'O', 'o', ')', '(', '<', 'v', 'P']

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)

print(eye + nose + mouth)
#concatenation using plus signs allows us to print each string next to each other, assembling the emoticon on one line


#Advanced Version 1
import random
eyes = [':', '8', 'x', ';']
noses = ['-', '~', 'っ', '^', '\'', '']
mouths = ['D', 'O', 'o', ')', '(', '<', 'v', 'P']

for i in range(5):  #for loop generates 5
    eye = random.choice(eyes)   #insert random.choice values into the loop
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    print(eye + nose + mouth)   #prints 5 random faces
