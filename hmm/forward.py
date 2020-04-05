""" Created by minhnq """
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

def forward(observations, states, a_matrix, b_matrix):
    output = [[0 for col in range(len(states) + 2)] for row in range(len(observations))]
    for index,s in enumerate(states):
        output[index+1][0] =  a_matrix[0][index+1] * b_matrix[index][observations[0]]
    for t in range(1,len(observations)):
        for s in range(len(states)):
            sum = 0
            for s_hat in range(len(states)):
                print(output[s_hat+1][t-1],a_matrix[s_hat+1][s+1],b_matrix[s][observations[t]])
                sum += output[s_hat+1][t-1]*a_matrix[s_hat+1][s+1]*b_matrix[s][observations[t]]
            output[s+1][t] = sum
        print(output)
    final_prob=0
    for prob in output:
        final_prob+=prob[len(observations)-1]
    return final_prob

if __name__ == '__main__':
    b_matrix = [[0.2,0.4,0.4],
                  [0.5,0.4,0.1]]
    a_matrix =  [[0, 0.8, 0.2],
                 [0, 0.7, 0.3],
                 [0,0.4,0.6]]
    observations = [2,0,2] # Which is corresponding to 3, 1, 3 as column in A matrix
    states = ["hot","cold"]
    print(forward(observations, states, a_matrix, b_matrix))

