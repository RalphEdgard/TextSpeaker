from gtts import gTTS
import os

def is_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            first_character = file.read(1)
            return not bool(first_character)
    except FileNotFoundError:
        return True
    
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    os.system("afplay output.mp3")

def main():
    while True: 
        try:
            inputCommandBoolean = input("Have you input some text? (Y or N): ")
            # Open the file in read mode
            if inputCommandBoolean == 'Y':
                content = ""
                if is_file_empty("inputFile.txt"):
                    print("\n\nThe file is empty. Put some text! (Open the file with the name inputFile.txt)\n\n")
                    if not os.path.exists("inputFile.txt"):
                        os.system("touch inputFile.txt")
                        print("File Created!")
                else:
                    with open("inputFile.txt", 'r') as file:
                        # Read the content of the file
                        content = file.read()
                    print("\n\n" + str(content) + "\n\n")
                    text_to_speech(str(content))
                    binaryInput = "Y"
                    
                    while binaryInput != 'N':
                        if input("Would you like the program to speak again? (Y or N): ") == "Y":
                            print("\n\n" + str(content) + "\n\n")
                            text_to_speech(str(content))
                        else:
                            break
                    
                    if len(content) != 0:
                        with open("inputFile.txt", "w") as file:
                            pass  # Pass does nothing, effectively emptying the file
            else:
                os.system("osascript -e 'quit app \"Terminal\"'")
        except FileNotFoundError:
            print("\n\nFile not found\n\n")
            os.system("touch inputFile.txt")
        

if __name__ == "__main__":
    main()
