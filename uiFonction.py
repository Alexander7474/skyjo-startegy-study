import os

def clearView():
    os.system('clear')

def sortClassment(classement: list[str],score: dict[int]):
    for i in range(len(classement),0,-1):
        for j in range(1,i):
            if score[classement[j]] < score[classement[j-1]]:
                save = classement[j]
                classement[j] = classement[j-1]
                classement[j-1] = save
    return classement
