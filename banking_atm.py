n = int(input("Enter the Amount of Money you want :"))

money = 1000

try :
    if money < n:
        break
except:
    print("You have Less than "n, "In your account")

finally:
    print("Finally Block")
