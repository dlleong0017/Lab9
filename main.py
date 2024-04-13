#Darren Leong Repository
def encode(data_string):
    new_string=""
    for i in data_string:
        new_string+=str(int(i)+3)

    return new_string

if __name__ == "__main__":
    x=True

    while x:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        choice= int(input("Please enter an option: "))
        if choice==1:
            password= input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif choice==2:
            pass
        elif choice==3:
            quit
