score = 100


def first():
    global score
    score = 200


def second():
    score = 300
    print(score)


first()
second()

print(score)