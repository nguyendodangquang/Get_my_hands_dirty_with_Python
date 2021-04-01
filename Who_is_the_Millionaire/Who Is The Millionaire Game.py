import random
f = open("C:/Users/Dang Quang/desktop/wwbm_qa.txt", "r")
listOfQuestion = f.read().split('\n')
reward = ['$100', '$200', '$300','$500', '$1000', '$2000', '$4000', '$8000', '$16000', '$32000', '$64000', '$125000', '$250000', '$500000', '$1000000']
ind = 0

for i in range(15):
    randomquest = random.sample(listOfQuestion, 1)[0]
    listOfQuestion.remove(randomquest)
    question = randomquest.split('[')[0]
    anwsers = randomquest.split('[')[1].split(',')[0:4]
    rightanswer = randomquest.split('[')[1].split(',')[-1]
    if rightanswer not in anwsers:
        anwsers[0] = rightanswer
    dic_anwsers = {}
    dic_anwsers['A'] = anwsers[0]
    dic_anwsers['B'] = anwsers[1]
    dic_anwsers['C'] = anwsers[2]
    dic_anwsers['D'] = anwsers[3]
    print(question)
    for key, value in dic_anwsers.items():
        print(f'{key}: {value}')
    response = input()
    if dic_anwsers[response] == rightanswer:
        print('Good job')
        ind += 1
        if ind == 15:
            print('You are the Millionaire')
            break
        next = input('Do you want to continue: ')
        if next.lower() == 'quit':
            print('You won: ' + reward[ind-1])
            break
    else:
        print('Sorry, you lost all of your money')
        break
