# Trick questions

import random
import string
import sys

questions = [
    {'question': "How many letters are in the alphabet?",
     'answer': "11.",
     'accept': ['11', 'eleven']},
    {'question': "If you build a fort, drive a Ford and fill out a form, then what do you eat soup with?",
     'answer': "A spoon.",
     'accept': ['a spoon', 'spoon']},
    {'question': "What thrives when you feed it but dies when you give it something to drink?",
     'answer': "A fire.",
     'accept': ['a fire', 'fire']},
    {'question': "What kind of button can't be unbuttoned?",
     'answer': "A belly button.",
     'accept': ['a belly button', 'belly button', 'a bellybutton', 'bellybutton']},
    {'question': "What is the answer to this question?",
     'answer': "What.",
     'accept': ['what']},
    {'question': "What can run but never walks, has a mouth but never talks, and is often found between banks?",
     'answer': "A river.",
     'accept': ['a river', 'river']},
    {'question': "The more of this there is, the less you see. What is it?",
     'answer': "Darkness.",
     'accept': ['darkness', 'dark']},
    {'question': "What's something that has teeth but can't chew?",
     'answer': "A comb.",
     'accept': ['a comb', 'comb']},
    {'question': "You can catch me, but I can't be thrown. What am I?",
     'answer': "A cold.",
     'accept': ['a cold', 'cold', 'a flu', 'the flu', 'flu']},
    {'question': "What's something that always wants an answer but doesn't have a question?",
     'answer': "A phone.",
     'accept': ['a phone', 'phone']},
    {'question': "What's something that copies your looks but not your sounds?",
     'answer': "A mirror.",
     'accept': ['a mirror', 'mirror']},
    {'question': "I wave, even if you don't say hello. What am I?",
     'answer': "A flag.",
     'accept': ['a flag', 'flag']},
    {'question': "What word becomes longer after you add two letters to it?",
     'answer': "Long.",
     'accept': ['long']},
    {'question': "What's something you can break but can't put back together?",
     'answer': "A promise.",
     'accept': ['a promise', 'promise']},
    {'question': "What has a spine but no bones?",
     'answer': "A book.",
     'accept': ['a book', 'book']},
    {'question': "What has a bottom at the top and helps you stand?",
     'answer': "A leg.",
     'accept': ['a leg', 'leg']},
]

random.shuffle(questions)
score = 0

for number, info in enumerate(questions):
    total_questions = len(questions)
    question = info['question']
    answer = info['answer']
    accepted_solutions = info['accept']

    print(f'Question: {number + 1}')
    print(f'Score: {score}/{total_questions}')
    print(f'QUESTION: {question}')
    response = input('ANSWER: ').strip(string.whitespace + string.punctuation).lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()
    elif response in accepted_solutions:
        print('Correct!')
        score += 1
    else:
        print(f'Incorrect! The answer is: {answer}')

    if number < total_questions - 1:
        input('Press Enter for the next question...')

if score <= total_questions // 4:
    print(f'You {score} out of {total_questions} correct. Better luck next time!')
elif score <= total_questions // 2:
    print(f'You {score} out of {total_questions} correct.')
else:
    print(f'Congratulations! You got {score} out of {total_questions} correct!')