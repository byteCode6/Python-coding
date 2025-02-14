import random
from gtts import gTTS
import os
from playsound import playsound

def speak(text):

    print(text)  # টেক্সট প্রিন্ট করুন
    tts = gTTS(text=text, lang='en')  # ইংরেজি ভাষায় টেক্সট-টু-স্পিচ
    tts.save("output.mp3")  # অডিও ফাইল হিসেবে সেভ করুন
    playsound("output.mp3")  # অডিও ফাইল প্লে করুন
    os.remove("output.mp3")  # অডিও ফাইল ডিলিট করুন

def number_guessing_game():
    speak("Welcome to the Number Guessing Game!")
    
    while True:
        # Difficulty selection
        speak("Choose a difficulty level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        difficulty = input("Enter your choice (1, 2, or 3): ")

        # Set range and attempts based on difficulty
        if difficulty == "1":
            range_min, range_max, attempts_allowed = 1, 50, 10
        elif difficulty == "2":
            range_min, range_max, attempts_allowed = 1, 100, 7
        elif difficulty == "3":
            range_min, range_max, attempts_allowed = 1, 200, 5
        else:
            speak("Invalid choice. Defaulting to Medium difficulty.")
            range_min, range_max, attempts_allowed = 1, 100, 7

        # Computer picks a random number
        secret_number = random.randint(range_min, range_max)
        attempts = 0
        guessed_correctly = False

        speak(f"I have picked a number between {range_min} and {range_max}. Can you guess it?")
        speak(f"You have {attempts_allowed} attempts.")

        while attempts < attempts_allowed and not guessed_correctly:
            try:
                # Ask the user to guess the number
                guess = int(input("Enter your guess: "))
                attempts += 1

                # Check if the guess is correct
                if guess < secret_number:
                    speak("Too low! Try again.")
                elif guess > secret_number:
                    speak("Too high! Try again.")
                else:
                    guessed_correctly = True
                    speak(f"Congratulations! You guessed the number in {attempts} attempts.")
            except ValueError:
                speak("Invalid input. Please enter a valid number.")

        if not guessed_correctly:
            speak(f"Sorry, you've run out of attempts. The number was {secret_number}.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            speak("Thanks for playing! Goodbye!")
            break

# Run the game
number_guessing_game()