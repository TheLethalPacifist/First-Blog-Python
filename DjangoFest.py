volume = 76
if volume < 20:
    print("I can't hear shit.")
elif 20 <= volume < 40:
    print("Nice little bop in the back")
elif 40 <= volume < 60:
    print("This is perfection, down to the last detail")
elif 60 <= volume < 80:
    print("Getting a little loud but not bad for blastin' time")
elif 80 <=volume <= 100:
    print("Hey you kids shut up or I am summoning the water on ya")
else:
    print("what noise?")

def hi():
    print("howdy pardner")
    print("how can I help ya today?")

def hi(name):
    if name =='Sheriff':
        print('Howdy Sheriff, how can I help you?')
    else:
        print('Howdy Pardney, how can I help ya?')

hi("Sheriff")