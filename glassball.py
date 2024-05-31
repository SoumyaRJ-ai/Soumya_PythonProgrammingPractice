# Consider a shuffle game. There are 3 glasses numbered from 1 to 3 and one ball is hidden 
# under any one of the glass. Then any 2 of the glasses are shuffled. This operation is made 3 times. 
# Given an integer N ranged [1, 3] and 3 pairs of integers of the same range. The N-th glass contain 
# the ball initially and every pair of the given integers represents the indices of the glasses needs 
# to be shuffled. Remember the glasses are renumbered after each shuffle.
# The task is to find out the index of the glass which contains the ball after all the shuffle operation.

def glassballIndex(n, shuffle):
    for i in range(len(shuffle)):
        # compare with each index value and swap if matches
        if shuffle[i][0] == n:
            n = shuffle[i][1]
            
        elif shuffle[i][1] == n:
            n = shuffle[i][0]
    print(n)

if __name__ == "__main__":
    
    n = 3 # the index number where the ball is located initially.
    
    shuffle = [
        [2, 3],
        [2, 1],
        [1, 3]
    ]
    glassballIndex(n, shuffle)
    