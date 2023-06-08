import random

characters = ['U', 'D', 'L', 'R', 'O', 'Z', 'N', 'V']
paragraph = ''

for _ in range(30):
    paragraph += random.choice(characters) + ' '
    

print(paragraph)


