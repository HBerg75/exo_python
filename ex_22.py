def verify_emails():
    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if "@" in line and line.endswith(".com"):
                print(line + " est un email valide")
            else:
                print(line + " n'est pas un email valide")
                

verify_emails()