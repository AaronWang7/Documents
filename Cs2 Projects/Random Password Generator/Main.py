#Aaron Wang 
#import random, to be used for random pick
import random
#password generater, adds letters, numbers specials, to create password, repeat length times.
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ""
    
    if use_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if use_numbers:
        characters += "0123456789"
    if use_special:
        characters += "!@#$%^&*()"

    password = ""
    #repeat length times, add random picked
    for i in range(length):
        password += random.choice(characters)
    #return, so all program can recive
    return password
#main function to ask to requirments, and print out the final password, list them with numbers.
def main():
    length = int(input("Password length: "))
    use_uppercase = input("uppercase?  y = yes,no = n: ") == "y"
    use_lowercase = input("lowercase?? y = yes : ") == "y"
    use_numbers = input("numbers? y = yes: ") == "y"
    use_special = input("special characters? y = yes: ") == "y"
    num = 0
    for i in range(4):
        num = num + 1
        print(f"This is your password number :{num}")
        print(generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special))

main()




def lengthh():
    howlong = input("How long should it be?:")


main()
