#################### MAC 연산 ################################
def mac(pattern, filter_):
    score = 0.0
    n = len(pattern)

    for i in range(n):
        for j in range(n):
            score += pattern[i][j] * filter_[i][j]
    return score
