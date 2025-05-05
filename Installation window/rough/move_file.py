import shutil
try:
    file = input("Enter A File Name: ")
    copy = shutil.copy(file, "Roaming")
#move = shutil.move(copy, "Roaming")
    print("Sucess")
except:
    print("Failed")