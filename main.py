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
            encoded_pass=encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif choice==2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}")
            print()
        elif choice==3:
            quit

#my addition - Avi M
def decode(encoded_password):
	new_string=""
	for i in encoded_password:
		new_string+=str(int(i)-3)
	
	return new_string
