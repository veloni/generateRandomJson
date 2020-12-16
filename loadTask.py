import random

i = 0

while i < 500:
    i = i + 1

    randomGenerateNumber = random.randint(1, 28)
    randomMonth = random.randint(0,11)
    randomTask = random.randint(0,2)
    
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    conditionTask = ['completed','active', 'ended']
    vvs = '"'
    
    number = randomGenerateNumber
    monthOne = month[randomMonth]
    task = conditionTask[randomTask]
    
    createDate = vvs + str(number) + " " + str(monthOne) + vvs +"," 
    createTask = vvs +  str(task) + vvs +"," 
     
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    
    conditionTask = ['completed','active', 'ended']
    
    print("{")
    print('nameUser: "Alex",')
    print('dueDate:',createDate)
    print('nameTask: "Fix bag",')
    print("conditionTask:", createTask)
    print('typeTask: "fix task",')
    print("},")

