from gtts import gTTS
import os
import time
import pyperclip
import pyautogui
from pydub import AudioSegment

def is_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            first_character = file.read(1)
            return not bool(first_character)
    except FileNotFoundError:
        return True
    
def text_to_speech(text):
    if text.strip():
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        os.system("afplay output.mp3")


def main():
    try:
        autoOrManual = input("would you like to run this program in auto or manual? (Type in auto or manual): ")
        if autoOrManual == 'auto':
            print("You are in auto mode")

            while True:
                time.sleep(2)
                pyautogui.moveTo(x=412, y=558)
                pyautogui.click()
                pyautogui.click()

                pyautogui.keyDown('ctrl')
                pyautogui.keyUp('ctrl')

                pyautogui.keyDown('ctrl')
                pyautogui.keyUp('ctrl')

                if input("Are you done? (Press Y if so): ") == 'Y':
                    time.sleep(1)
                    pyautogui.moveTo(492, 565)
                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()

                if input("Has the AI finished its response? (Press Y if so): ") == 'Y':
                    pyautogui.moveTo(479, 483)
                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()

                    message = pyperclip.paste()

                    if message == "Zulu, Echo, 11":
                        os.system("osascript -e 'quit app \"Terminal\"'")

                    for sentence in message.split("."):
                        print('\n' + sentence)
                        text_to_speech(sentence)

        elif autoOrManual == 'manual':
            while True: 
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
                elif inputCommandBoolean == 'N':
                    os.system("osascript -e 'quit app \"Terminal\"'")
    except FileNotFoundError:
        print("\n\nFile not found\n\n")
        os.system("touch inputFile.txt")
    

if __name__ == "__main__":
    main()
