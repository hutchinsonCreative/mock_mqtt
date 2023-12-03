


def colourString(i):
    return f"\u001b[38;5;{i}m"

def listColours():
    for i in range(255):
        print(f"\u001b[38;5;{i}m{i} The quick brown fox jumped over the lazy brown dog.")

def green():
    return colourString(46)

def red():
    return colourString(9)

def white():
    return colourString(10)

def blue():
    return colourString(21)

def teal():
    return colourString(3)

def brown():
    return colourString(1)

def grey():
    return colourString(0)

def orange():
    return colourString(4)

def purple():
    return colourString(57)

def pink():
    return colourString(197)