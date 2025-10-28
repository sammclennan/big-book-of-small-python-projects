# Magic 8 Ball

import random
import time

def delay_print(text, pause=0.1):
    for char in text:
        print(char.upper(), end=' ', flush=True)
        time.sleep(pause)
    print()
    print()

delay_print('Magic 8 ball')
time.sleep(0.7)

delay_print('Ask me your yes/no question')

input('> ')
print()

comments = [
    "I see...",
    "That's an interesting question...",
    "Let me think about that...",
    "Let me see...",
    "Brace yourself...",
    "Let me consult the mystical powers...",
    "An interesting question... Let's see...",
    "Ooh, this one's tricky..."
]
delay_print(random.choice(comments))
time.sleep(1)

delay_print('I have an answer...')
delay_print('.....', 1)

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]
delay_print(random.choice(answers), 0.04)