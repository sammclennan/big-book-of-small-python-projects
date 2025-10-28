# Converts English text into Pig Latin

import pyperclip

def main():
    text = ''
    while not text:
        print('Enter text to convert to Pig Latin:')
        text = input('> ').strip()

    words = text.split(' ')

    for x in range(len(words)):
        word = words[x]

        titlecase = False
        if word.istitle():
            titlecase = True
            word = word.lower()

        # Skip any words not containing letters
        if not any(i.isalpha() for i in word):
            continue

        # Capture leading chars
        leading_chars = ''
        while word and not word[0].isalpha():
            leading_chars += word[0]
            word = word[1:]

        # Capture trailing chars
        trailing_chars = ''
        while not word[-1].isalpha():
            trailing_chars += word[-1]
            word = word[:-1]
        
        # Capture leading consonants
        leading_consonants = ''
        while not word[0] in 'aiueoAIUEO' and len(word) > 1:
            leading_consonants += word[0]
            word = word[1:]

        word = word + leading_consonants + 'ay'
        if titlecase: word = word.title()
        words[x] = leading_chars + word + trailing_chars

    pig_latin_text = ' '.join(words)

    pyperclip.copy(pig_latin_text)

    print(pig_latin_text)
    print('(Copied Pig Latin to clipboard)')

if __name__ == '__main__':
    main()