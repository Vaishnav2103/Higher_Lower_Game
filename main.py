from art import logo , vs
from game_data import data
import random
from replit import clear
is_game_over = False
count = 0
def format_data(celeb):
  """Takes the data and returns the printable format"""
  name = celeb["name"]
  description = celeb["description"]
  country = celeb["country"]
  return (f"{name}, a {description}, from {country}")
#choose two celebrities
for celeb in range(1):
  celeb1 = random.choice(data)
  celeb2 = random.choice(data)
#while loop for whole programe
while is_game_over is not True:
  print(logo)
  # #displaying details
  print(f"Compare A: {format_data(celeb1)}")
  print(vs)
  print(f"Against B: {format_data(celeb2)}")

  #Checking if user is correct
  highest_count = 0
  follower_celeb1 = celeb1["follower_count"]
  follower_celeb2 = celeb2["follower_count"]
  if follower_celeb1 > follower_celeb2:
    highest_count = follower_celeb1
  else:
    highest_count = follower_celeb2
    
  #Ask for input
  choice = input("Who has more followers? Type 'A' or 'B' ").lower()
  if choice == "a":
    if highest_count == follower_celeb1:
      count += 1
      clear()
      print(f"You are right! Current score: {count}")
      celeb1 = celeb2
      celeb2 = random.choice(data)
    else:
      print(f"Wrong Answer Current score: {count}")
      is_game_over = True
  elif choice == "b":
    if highest_count == follower_celeb2:
      count += 1
      print(f"You are right! Current score: {count}")
      celeb1 = celeb2
      celeb2 = random.choice(data)
    else:
      print(f"Wrong Answer Current score: {count}")
      is_game_over = True
    