EPSILON = 1e-9
REPEAT = 10
CROSS = 'Cross'
X = 'X'


#################### 판 정   #################################
def judge(score_cross, score_x):
    if abs(score_cross - score_x) < EPSILON:
        return 'UNDECIDED'  
    return CROSS if score_cross > score_x else X
