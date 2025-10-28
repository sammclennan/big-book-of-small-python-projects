# Creates quizzes with questions and answers in random order along with answer key.

import random

capitals_dict = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    # Open quiz and answer key files for writing
    quizFile = open(f'quiz{quizNum + 1}.txt', 'w')
    keyFile = open(f'answerKey{quizNum + 1}.txt', 'w')

    # Write text headers
    quizFile.write('U.S. capitals Quiz\nName: ____________\nDate: __________\nPeriod: __________\n\n')
    keyFile.write('U.S. capitals Answer Key\n\n')

    # Create shuffled list of U.S. states
    states = list(capitals_dict)
    random.shuffle(states)

    # Loop through states list
    for i in range(50):
        correctAnswer = capitals_dict[states[i]]

        # Create shuffled list of capitals and remove correct answer 
        capitals = list(capitals_dict.values())
        capitals.remove(correctAnswer)

        # Create shuffled multi-choice list
        multiChoice = random.sample(capitals, 3) + [correctAnswer]
        random.shuffle(multiChoice)

        # Write multi-choice question to quiz file
        quizFile.write(f'{i + 1}. What is the capital of {states[i]}?\n')
        for j in range(4):
            quizFile.write(f' {'ABCD'[j]}. {multiChoice[j]}\n')
        quizFile.write('\n')

        # Write answer key for corresponding question
        keyFile.write(f'{i + 1}. {'ABCD'[multiChoice.index(correctAnswer)]}\n')

    quizFile.close()
    keyFile.close()