import random

capitals={
    'Kenya':'Nairobi',
    'Egypt':'cairo',
    'Ethiopia':'AdisAbaba',
    'Eritrea':'Asmara',
    'Somalia':'Mogadishu',
    'Djibouti':'Djibouti',
    'Tanzania':'Arusha',
    'Uganda'  :'Kampala',
    'South Sudan':'Juba',
    'Sudan'   :'Khartoum',
    'DRC'    :'Kinshasa',
    'South Africa':'Pretoria',
    'Namibia'  :'Namib',
    'Nigeria' :'Abuja',
    'Morrocco': 'Rabat'
}

multiple_choice=['A','B','C','D']
#generate 10 quiz files
for x in range(10):
    quizfile=open('capitalquiz %s'% (x+1),'w')
    answerfile=open('capitalquiz_answer %s'%(x+1),'w')

    quizfile.write('NAME:   \n\nDATE:   \n\nPERIOD:   \n\n')
    quizfile.write((''*20)+'Country capital quiz(Form  %s)'%(x+1))
    quizfile.write('\n\n')

    #shuffle the order of the states
    countries=list(capitals.keys())
    random.shuffle(countries)


    #loop through all 15 countries ,making a question for each
    for questionnumber in range(15):
        # get right and wrong answers
        correct_answer=capitals[countries[questionnumber]]
        wrong_answers=list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers=random.sample(wrong_answers,3)
        answer_options=wrong_answers+ [correct_answer]
        random.shuffle(answer_options)


        #write the question and answers to their respective files
        quizfile.write(f'{questionnumber +1 }. What is the capital city of {countries[questionnumber]}\n')

        for i in range(4):
            quizfile.write(f'{multiple_choice[i]}. {answer_options[i]}\n')

        #write answer to file
        answerfile.write(f"{questionnumber+1}. {multiple_choice[answer_options.index(correct_answer)]} \n")
        
    quizfile.close()
    answerfile.close()