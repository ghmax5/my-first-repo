# name = input("Enter Your Name: ")
# print("Good Afternoon",  name)
print("Small Practical On String Replacement")
usrname = input("Enter your name:")
letter = '''Dear <|NAME|>,
                You are Selected ! 
                <|DATE|>'''
letter = (letter.replace("<|NAME|>",usrname).replace("<|DATE|>","3/5/23"))
print(letter)
