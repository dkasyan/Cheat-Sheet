import random

words_list = ["noga", "car", "epileptyka"]
empty_list = []

number = 0
len_special_word = len(special_word)


# TODO-1 Losowo wybierz slowo

# TODO-2

def generate_word(words_list):
    special_word = random.choice(words_list)
    return(special_word)

print(generate_word(words_list))

for i in special_word:
    empty_list.append("_")

while number <= len_special_word:
    guess = input("Guess a letter: ").lower()
    for z in empty_list:
        if guess == special_word[number]:
            empty_list[number] = guess
    print(empty_list)
    number = (number + 1)
    print(number)
    print(empty_list)




#print(f"Is this what you just said? {choice}")

