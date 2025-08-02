def play_hangman() :
    "this just a waste of line in the code "

print("welcome to Hangman")
print("guess the letters of the secret word")
no_of_guesses = 8
word = list("pradeep")
appear = ["_"] * len(word)
print(" " . join(appear))
guessed = []
while appear != word and no_of_guesses > 0:
    guess = input("no of guess left :" + str(no_of_guesses) + " \n enter your guess :").strip().lower()

    for i in range(len(word)) :
        if word[i] == guess :
            appear[i] = guess
            guessed.append(guess)
    if guess in guessed :
        print("you already guessed that letter ")
    else :
        guessed.append(guess)
    if appear == word :
        print(f"congratulations you guessed all the letters in the word {"".join(appear)}")
        break
    if guess not in word :
        print("your guess is wrong , guess again until you're right ")
    no_of_guesses -= 1
    if no_of_guesses == 0:
        print("You have no guesses left. The word was:", "".join(word))
    print(" ".join(appear))

while True :
    play_hangman()
    play = input("Do you like play hangman ? yes/no ").strip().lower()
    if play != "yes" :
        print("Thank you for playing ")
        break
    