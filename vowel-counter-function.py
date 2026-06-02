global text
text=str
def count_vowels(text):
    text=input("Enter a word or sentence:")
    vowels='aeiou'
    vowel_count = sum(text.count(v) for v in vowels)
    print(f"The word/sentence {text} has {vowel_count} vowels!")
count_vowels(text)