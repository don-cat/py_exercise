def move():
    d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

    sum = 0.0
    avr = 0.0
    print(d.values())
    print(d.itervalues())
    for score in d.values():
        sum = sum + score
        avr = sum / len(d)
    print(avr)

move()