print("Name the Lyrics game!!!!!\n\nFill in the blank Lyrics\n\nType in the blank lyrics and see in how many attempts you get it right.\n\n")

counter = 0

while True:
  print("Never gonna _____ you up, never gonna let you down!")

  answer = input("What's the missing word in lyrics?\n")

  if answer == "give" or answer == "Give" or answer == "GIVE":
    print("Correct! It took you",counter,"attempts\n")
    break
  else:
    print("Wrong answer! Rick Astley would be disappointed! Try Again!!!\n")

    counter+=1