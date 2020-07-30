from random import choice, randint
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
positive = [
    "It is cewtain",
    "It is decidedwy so",
    "Without a doubt",
    "Yes, definitewy",
    "U may rewy on it",
    "As I see it, yes",
    "Most wikewy",
    "Outwook good",
    "Yes",
    "Signs point to yes"
]
p_appends = [
    "$w$",
    "nwn",
    ":)",
    "owo",
    "uwuwuwu",
    "n3n"
]
neutral = [
    "Repwy hazy, twy again.",
    "Ask again water",
    "Bettew not teww you now",
    "Cannot pwedict now",
    "Concentwate and ask again"
]
neu_appends = [
    "e_e",
    "7w7",
    ":|",
    "o3o",
    "-w-",
    "-3-"
]

negative = [
    "Don't count on it",
    "My weply is no",
    "My souwces say no",
    "Outwook not so good",
    "Vewy doubtfuw",

]
neg_appends = [
    "unu",
    "u3u",
    ":(",
    "ono",
    "ene"
    "V_V"
]
sense.show_message("Ask a question uwu", text_colour=[12,160,235], scroll_speed=0.05)
sleep(3)
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 2 or y > 2 and z > 2:
        sleep(1)
        pnn = randint(1,3)
        if pnn == 1:
            sense.show_message(choice(positive) + " " + choice(p_appends), text_colour = [0,255,0], scroll_speed = 0.05)
        elif pnn == 2:
            sense.show_message(choice(neutral) + " " + choice(neu_appends), text_colour = [255,255,0], scroll_speed = 0.05)
        elif pnn == 3:
            sense.show_message(choice(negative) + " " + choice(neg_appends), text_colour = [255,0,0], scroll_speed = 0.05)
    else:
        sense.clear()
        