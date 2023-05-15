from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a word: ")
if word in corrector:
    print("correct")
else:
    correct_word = corrector.correction(word)
    print("Correct spelling is: ", correct_word)