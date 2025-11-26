import random

money = 10

files = ["names.txt", "moves.txt", "pokemon.txt", "types.txt"]
file_name = random.choice(files)

with open(f"{file_name}", "r") as file:
    text = file.read().splitlines()

with open("saves.txt", "w") as save_file:
    save_file.write("Information about the save")
    save_file.write(f"{money}")

print(text)