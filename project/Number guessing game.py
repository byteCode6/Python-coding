import random
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male voice        1 = female voice
engine.setProperty('rate', 145)  # Speech speed {words per minute}

def speak(text):
    
    """AI voice"""
    print(text)  #  print for Text
    engine.say(text)  # Toking for AI voice 
    engine.runAndWait()

def number_guessing():
    speak('Welcome to the Number Guessing Game.')
    
    while True:
        speak("\nSelect any level.")
        print("1. Easy level (1-30, 10 attempts) ")
        print("2. Medium level (1-40, 6 attempts)")
        print("3. Hard level (1-50, 4 attempts)")
        difficulty = int(input('Enter your choice (1, 2, or 3): '))
        
        if difficulty == 1:
            range_min, range_max, attempts_allowed = 1, 30, 10
        elif difficulty == 2:
            range_min, range_max, attempts_allowed = 1, 40, 6
        elif difficulty == 3:
            range_min, range_max, attempts_allowed = 1, 50, 4
        else:
            speak("Invalid choice. Defaulting to Easy level difficulty.")
            range_min, range_max, attempts_allowed = 1, 30, 10
            
        secret_number = random.randint(range_min, range_max)
        attempts = 0
        guessing = False
        
        speak(f"\nI have picked a number between {range_min} and {range_max}. Can you guess it?")
        speak(f"You have {attempts_allowed} attempts.")
        
        while attempts < attempts_allowed and not guessing:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                if guess < secret_number:
                    speak("Too low! Try again.")
                elif guess > secret_number:
                    speak("Too high! Try again.")
                else:
                    guessing = True
                    speak(f"Congratulations! You guessed the number in {attempts} attempts.")
            except ValueError:
                speak("Invalid input. Please enter a valid number.")
        
        if not guessing:
            speak(f"Sorry, you've run out of attempts. The number was {secret_number}.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            speak("Thanks for playing! Goodbye!")
            break
    
number_guessing()



