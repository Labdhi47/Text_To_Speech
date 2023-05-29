import pyttsx3
friend=pyttsx3.init()
friend. setProperty("rate", 110)
speech=input("Enter the text:")
friend.say(speech)
friend.runAndWait()