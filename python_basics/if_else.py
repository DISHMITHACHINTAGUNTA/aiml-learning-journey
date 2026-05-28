# If-Else Practice - Conditional Statements
# AIML Learning Journey

gen = input("Do you belong to GenZ? (y/n): ").lower()
persona = input("Are you a woman or man? (f/m): ").lower()

if gen == "" or persona == "":
    print("Oops! Looks like you forgot to enter something. Please try again!")
elif gen == "y" and persona == "f":
    print("Hey girl! Great to have you here, welcome!")
elif gen == "y" and persona == "m":
    print("Hey buddy! Great to have you here, welcome!")
elif gen == "n":
    print("Hey there! This one's built for Gen Z, but thanks for stopping by!")
else:
    print("Hmm, that doesn't look right. Please enter 'y' or 'n' for genZ and 'f' or 'm' for persona.thankyou, try it once again")