try:
    with open ("Datei.xyz", "r") as file:
        print(file)
        print(5 / 0)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")


