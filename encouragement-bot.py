while True:
  description = input("How do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("life is programmed to make you sad")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("happiness is ephremal :D ")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you should sleep. unless you can't, because sometimes it's impossible to fall asleep. Also keep in mind that it is possible to never wake up.")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("the longer you suppress it, the bigger the explosion")
      counter += 1
    if each_word == "overwhelmed":
      feelings_list.append("overwhelmed")
      encouragement_list.append("Xanax is a thing")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
