
import random

def DFAWalk():
    state_set = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13']
    
    noun = ['man','woman','student','teacher','programmer','geek','nerd','genious','princess','prince','ninja','wizard','toad']
    det = ['a','the','some','that','this']
    hpv = ['is','was','were']
    conj = ['and','or','but']
    adv = ['sometimes','often','never','always']
    adj = ['happy','sad','good','bad','clever','lazy','briliant','stupid','lame','useless','crazy','silly']
    pnoun = ['Ted','Paul','Jason','Jim','Duane','Mario','Harry Potter','Gandalf','Ada','Ron Weasley']
    endp = ['.','!','?']
    
    start_state = 'q0'
    final_state_set = ['q10']

    sentence = ""
    state=start_state
    while True:
        
        if(state == 'q0'):
            rng = random.randint(0,1)
            if(rng == 0):
                sentence+=random.choice(det)
                sentence+=" "
                state = 'q2'
            elif(rng == 1):
                sentence+=random.choice(pnoun)
                sentence+=" "
                state = 'q3'
            else:
                return False
        elif(state == 'q1'):
                return False
        elif(state == 'q2'):
            sentence+=random.choice(noun)
            sentence+=" "
            state = 'q3'
        elif(state == 'q3'):
            rng = random.randint(0,1)
            if(rng == 0):
                sentence+=random.choice(hpv)
                sentence+=" "
                state = 'q4'
            elif(rng == 1):
                sentence+=random.choice(conj)
                sentence+=" "
                state = 'q0'
            else:
                return False
        elif(state == 'q4'):
            rng = random.randint(0,2)
            if(rng == 0):
                sentence+=random.choice(det)
                sentence+=" "
                state = 'q5'
            elif(rng == 1):
                sentence+=random.choice(adv)
                sentence+=" "
                state = 'q6'
            elif(rng == 2):
                sentence+=random.choice(adj)
                sentence+=" "
                state = 'q7'
            else:
                return False
        elif(state == 'q5'):
            rng = random.randint(0,1)
            if(rng == 0):
                sentence+=random.choice(noun)
                sentence+=" "
                state = 'q11'
            elif(rng == 1):
                sentence+=random.choice(adj)
                sentence+=" "
                state = 'q5'
            else:
                return False
        elif(state == 'q6'):
            rng = random.randint(0,1)
            if(rng == 0):
                sentence+=random.choice(det)
                sentence+=" "
                state = 'q5'
            elif(rng == 1):
                sentence+=random.choice(adj)
                sentence+=" "
                state = 'q7'
            else:
                return False
        elif(state == 'q7'):
            rng = random.randint(0,2)
            if(rng == 0):
                sentence+=random.choice(conj)
                sentence+=" "
                state = 'q9'
            elif(rng == 1):
                sentence+=random.choice(adj)
                sentence+=" "
                state = 'q7'
            elif(rng == 2):
                sentence = sentence[0:-1]
                sentence+=random.choice(endp)
                sentence+=" "
                state = 'q10'
            else:
                return False
        elif(state == 'q8'):
            rng = random.randint(0,2)
            if(rng == 0):
                sentence+=random.choice(hpv)
                sentence+=" "
                state = 'q4'
            if(rng == 1):
                sentence+=random.choice(conj)
                sentence+=" "
                state = 'q12'
            elif(rng == 2):
                sentence = sentence[0:-1]
                sentence+=random.choice(endp)
                sentence+=" "
                state = 'q10'
            else:
                return False
        elif(state == 'q9'):
            rng = random.randint(0,3)
            if(rng == 0):
                sentence+=random.choice(det)
                sentence+=" "
                state = 'q13'
            elif(rng == 1):
                sentence+=random.choice(adv)
                sentence+=" "
                state = 'q6'
            elif(rng == 2):
                sentence+=random.choice(adj)
                sentence+=" "
                state = 'q7'
            elif(rng == 3):
                sentence+=random.choice(pnoun)
                sentence+=" "
                state = 'q3'
            else:
                return False
        elif(state == 'q10'):
            break
        elif(state == 'q11'):
            rng = random.randint(0,1)
            if(rng == 0):
                sentence+=random.choice(conj)
                sentence+=" "
                state = 'q12'
            elif(rng == 1):
                sentence = sentence[0:-1]
                sentence+=random.choice(endp)
                sentence+=" "
                state = 'q10'
            else:
                return False
        elif(state == 'q12'):
            rng = random.randint(0,4)
            if(rng == 0):
                sentence+=random.choice(det)
                sentence+=" "
                state = 'q2'
            elif(rng == 1):
                sentence+=random.choice(hpv)
                sentence+=" "
                state = 'q4'
            elif(rng == 2):
                sentence+=random.choice(conj)
                sentence+=" "
                state = 'q0'
            elif(rng == 3):
                sentence+=random.choice(adv)
                sentence+=" "
                state = 'q6'
            elif(rng == 4):
                sentence+=random.choice(pnoun)
                sentence+=" "
                state = 'q3'
            else:
                return False
        elif(state == 'q13'):
            rng = random.randint(0,1)
            if(rng == 0):
                sentence+=random.choice(noun)
                sentence+=" "
                state = 'q8'
            elif(rng == 1):
                sentence+=random.choice(adj)
                sentence+=" "
                state = 'q5'
            else:
                return False
        else:
            return False
    if state in final_state_set:
        return sentence
    return False


for i in range(100):
    print(str(i+1)+".", DFAWalk())


