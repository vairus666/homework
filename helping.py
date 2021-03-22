def isint(s):
    # Проверка на целочисленность
    try:
        int(s)
        return True
    except ValueError:
        return False

def isfloat(s):
    # Проверка на float
    try:
        float(s)
        return True
    except ValueError:
        return False
