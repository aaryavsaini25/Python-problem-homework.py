global text
text=str
def count_vowels(text):
    text=input("Enter a word or sentence:")
    vowels='aeiou'
    vowel_count=0
    for txt in text:
        if txt in vowels:
            vowel_count=vowel_count+1
    print(f"The word/sentence {text} has {vowel_count} vowels!")
count_vowels(text)