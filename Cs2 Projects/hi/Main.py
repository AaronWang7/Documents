# english and morse Code lists
# english list
english = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
#morse code list
morse = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
]
#Engilsh to morse code,check if user entered the right thing, if not display "?"
def english_to_morse(text):
    """English to morse Code."""
    for i in text.upper():  #make every thing user had entered uppercase 
        if i in english: 
            print(morse[english.index(i)]) 
        else:
            print("?")
    print()
# morse code to english translate, check if user entered the right thing, if not display "?"
def morse_to_english(code): 
    """morse Code to English."""
    for i in code.split(): # a loop named for that splits the code
        if i in morse: #if code is one of the morse code letters
            print(english[morse.index(i)]) #display the translated version
        else:#else
            print("?")
    print()
#Gives user choice of what to do, 1 and 2 for translate and 3 for exit
def main():
    """Main loop for user choice."""
    while True:# A loop named while
        choice = input("1 = English to morse, 2 = morse to English, 3 = Exit: ") # place for user to enter choice
        if choice == "1": # if choice = 1
            english_to_morse(input("Enter English text: "))
        elif choice == "2":# else if choice = 2
            morse_to_english(input("Enter morse code: "))
        elif choice == "3":#else if choice = 3
            break#stop the loop
        else:
            print("Wrong choice")#display wrong choice
#Runs everying
main()
