def game():
    return 123

a = str(game())
with open('Highscore.txt','r') as f:
    score = str(f.read())
if int(a) > int(score) :
    with open('Highscore.txt','w') as s:
        s.write(a)

if score == '':
    with open('Highscore.txt','w') as s:
        s.write(a)

