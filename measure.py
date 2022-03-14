"""Modul zum Messen von Laufzeiten"""

from time import time
import os


def join_uncorrectly(durchlauf):
    """Joinen mit arithmetischen Operatoren"""
    f = open("strings.py", "a")
    method = '"BLA" + '
    string = ""
    for i in range(durchlauf):
        string += method

    string += '"BLA"'
    string = "test = " + string + "\n"

    # string += "print(test)"

    f.write(string)
    f.close()
    first_time = time()
    os.system("python strings.py")
    second_time = time()
    os.remove("strings.py")

    return second_time - first_time


def join_correctly(durchlauf):
    """Joinen mit join Funktion"""
    f = open("strings.py", "a")
    method = '"BLA", '
    string = ""
    for i in range(durchlauf):
        string += method

    string = '"".join((' + string + ' "BLA"))'
    string = "test = " + string + "\n"
    # string += "print(test)"

    f.write(string)
    f.close()
    first_time = time()
    os.system("python strings.py")
    second_time = time()
    os.remove("strings.py")

    return second_time - first_time


if __name__ == "__main__":
    join_uncorrectly(100)
    join_correctly(100)
