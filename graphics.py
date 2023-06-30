

def Hanger():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print("/()\\__")

def Hang_A():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print("/()\\__")

def Hang_B():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||       (=)")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print("/()\\__")

def Hang_C():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||       (=)")
    print(" ||        |")
    print(" ||        |")
    print(" ||        |")
    print(" ||        |")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print("/()\\__")

def Hang_D():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||       (=)")
    print(" ||       /|")
    print(" ||      / |")
    print(" ||        |")
    print(" ||        |")
    print(" ||")
    print(" ||")
    print(" ||")

    print(" ||")
    print("/()\\__")

def Hang_E():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||       (=)")
    print(" ||       /|\\")
    print(" ||      / | \\")
    print(" ||        |")
    print(" ||        |")
    print(" ||")
    print(" ||")
    print(" ||")
    print(" ||")
    print("/()\\__")

def Hang_F():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||       (=)")
    print(" ||       /|\\")
    print(" ||      / | \\")
    print(" ||        |")
    print(" ||        |")
    print(" ||       /")
    print(" ||      /")
    print(" ||")
    print(" ||")
    print("/()\\__")

def Hang_G():
    print("/()\\")
    print(" ||=====><|||><")
    print(" ||        |")
    print(" ||       (=)")
    print(" ||       /|\\")
    print(" ||      / | \\")
    print(" ||        |")
    print(" ||        |")
    print(" ||       / \\")
    print(" ||      /   \\")
    print(" ||")
    print(" ||")
    print("/()\\__")


def hangman_state(lives):
    if lives == 1:
        Hang_G()

    elif lives == 2:
        Hang_F()

    elif lives == 3:
        Hang_E()

    elif lives == 4:
        Hang_D()

    elif lives == 5:
        Hang_C()

    elif lives == 6:
        Hang_B()

    elif lives == 7:
        Hang_A()


