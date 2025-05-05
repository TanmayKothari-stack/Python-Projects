dic = {"Aman":9785013758,"Ajay":8890653276,"Naman":9908765439,"Ankit":7789065438}
print(dic)
def delete(name):
    if name in dic:
        del dic[name]
        print(dic)
    else:
        print("This name is not present")

name = input("Enter name to delete: ")
delete(name)
