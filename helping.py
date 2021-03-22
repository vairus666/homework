

def write_to_file(data, filename="./text.txt"):
    with open(filename, 'wb') as crip:
        crip.write(data)


def read_from_file(filename="./text.txt"):
    with open(filename, 'rb') as crip:
        data = crip.read()
        return data

def read_to_file_key(filename="./key.txt"):
    with open(filename, 'r') as key_pass:
        data = key_pass.read()
        return data
    
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