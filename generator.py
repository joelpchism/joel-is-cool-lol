# The Generator

game_is_running = True

while game_is_running:

  print("")
  print("-------- THE GENERATORRRR ---------")

  print("The Options...")

  options = ["dog", "fish", "bird", "cow", "muffin","killer whale", "shark", "puffin",]

  for item in options:
    print(item)

  print("")

  option = input("Please enter one of the following: ")

  food = ""

  if option == "dog":
    food = "MEAT"
  elif option == "fish":
    food = "SEAWEED"
  elif option == "bird":
    food = "SEEDS"
  elif option == "muffin":
    food = "blueberry muffins"
  elif option == "puffin":
    food = "fish"
  elif option == "shark":
    food = "fish"
  elif option == "killer whale":
    food = "shark"
  elif option == "cow":
    food = "GRASS"
  elif option == "cow":
    food = "GRASS"

  print("")
  print("EAT " + food)
  print("")
  print(" ...You Filthy animal!")

  choice = input("Play again? (Y/N)")
  if choice == "Y":
    game_is_running = True
  if choice == "N":
    print("BYE BYE!")
    game_is_running = False
