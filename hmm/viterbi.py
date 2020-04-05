""" Created by minhnq """
import numpy as np
# B matrix:
#       1      2     3
# hot   0.2 | 0.4 | 0.4
# cold  0.5 | 0.4 | 0.1
#
#
# A matrix:
#         start   hot  cold
# start   0       0.8    0.2
# hot     0       0.7    0.3
# cold    0       0.4    0.6


def viterbi(observations, states, a_matrix, b_matrix):
    viterbi =  [[0 for col in range(len(states)+2)] for row in range(len(observations))]
    for index,s in enumerate(states):
        viterbi[index+1][0] =  a_matrix[0][index+1] * b_matrix[index][observations[0]]
    for t in range(1,len(observations)):
        for s in range(len(states)):
            temp=[]
            for s_hat in range(len(states)):
                temp.append(float(viterbi[s_hat + 1][t - 1] * a_matrix[s_hat + 1][s + 1] * b_matrix[s][observations[t]]))
            viterbi[s+1][t]=max(temp)

    backpointers = [states[i] for i in np.argmax(np.array(viterbi),axis=0)[:-1] - 1]
    return backpointers

if __name__ == '__main__':
    b_matrix = [[0.2, 0.4, 0.4],
                [0.5, 0.4, 0.1]]
    a_matrix = [[0, 0.8, 0.2],
                [0, 0.7, 0.3],
                [0, 0.4, 0.6]]
    observations = [2, 0, 2]  # Which is corresponding to 3, 1, 3 as column in A matrix
    states = ["hot", "cold"]
    print(viterbi(observations, states, a_matrix, b_matrix))