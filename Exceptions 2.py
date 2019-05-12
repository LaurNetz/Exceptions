try:
    with open("datei.xyz", "r") as file:
        print(file)
    print(5 / 0)
except ( ZeroDivisionError):
    print("Du darfst nicht durch 0 teilen")