#! python3

# Creates quizes with questions and answers in random order, along with the answer key.

import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento"
   
}

for quiz_num in range(5):
    
    # Create a quiz file
    
    quiz_file = open('capital_quiz%s.txt' %(quiz_num + 1), 'w')
    answers_file = open('capital_answers%s.txt' %(quiz_num + 1), 'w')
    
    # header for quizfile
    
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State capitals quiz (Form %s)' %(quiz_num + 1))
    quiz_file.write('\n\n')
    
    # shuffle order of states
    
    states = list(capitals.keys())
    random.shuffle(states)
    
for question_num in range(5):
    correct_answer = capitals[states[question_num]]
    wrong_answer = list(capitals.values())
    del wrong_answer[wrong_answer.index(correct_answer)]
    wrong_answer = random.sample(wrong_answer, 3)
    answer_options = wrong_answer + [correct_answer]
    random.shuffle(answer_options)    
    # write the question and the answer options in quiz file
        quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
    
        for i in range(4):
        quiz_file.write('    %s. %s\n' %('ABCD'[i], answer_options[i]))
    quiz_file.write('\n')
    
        # write the answer to a file
        answers_file.write("%s. %s\n" %(question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

quiz_file.close()
answers_file.close()
    