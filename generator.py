# The Generator

game_is_running = True

while game_is_running:

  print("")
  print("-------- THE GENERATORRRR ---------")

  print("The Options...")
  
  options2 = {'dog': "meat", 'fish': "seaweed", "bird": "seeds",'muffin': "bluberry",'puffin': "fish",'shark': "fish",'killer whale': "shark",'cow': "grass",'apple': "google",}

  for item in options2.keys():
    print(item)

  print("")

  option = input("Please enter one of the following: ")

  # Look up the food in the dictionary from the animal the user entered
  food = options2[option]

  print("")
  print("EAT " + food)
  print("")
  print(" ...You Filthy animal!")

  choice = input("Play again? (Y/N)")
  if choice == "y":
    game_is_running = True
  if choice == "n":
    print("BYE BYE!")
    game_is_running = False
# testing