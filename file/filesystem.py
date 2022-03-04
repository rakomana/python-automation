name = input("Enter your name : ")

with open("info.txt", mode="w") as file:
    file.write(f"{name}")
