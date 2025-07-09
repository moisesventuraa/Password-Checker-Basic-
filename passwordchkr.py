print("Hi, enter your password")
subject = input("Password: ")

score = 0

length = len(subject)
if length < 8:
    print("Inadequate Length..|")
else:
    print("Length Satisfatory..")
    score += 1 

capitals = False
for i in subject:
    
    if i.isupper():
     
     capitals = True
     break



if capitals == True:
      print("Capital Letters: Passed..")
      score += 1
else:
    print("Fail: No capital letters")


lowers = False
for i in subject:
    if i.islower():
        lowers = True
        break

if lowers == True:
    print("Lowercase letters detected..")
    score += 1 
else:
    print("Fail : No lowercase found..")


numerics = False 
for i in  subject:
    if i.isdigit():
        numerics = True
        break

if numerics == True:
    print("Numbers detected...")
    score += 1 
else:
    print("Fail: No numbers found")

# no special syntax for symbols (manual check)
special_chek = False
symbols = "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~"

for i in subject:
    if i in symbols:
        special_chek = True
        break

if special_chek == True:
    print("Special charecters detected..")
    score += 1 
else:
    print("Fail: No special charecters")


if score <= 2:
    print("Weak password: Please Review Criteria")
elif score == 3 or score == 4:
    print("Moderate Password: Consider slight changes")
elif score == 5:
    print("Strong Password!")











