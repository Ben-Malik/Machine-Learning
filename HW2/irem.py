elif (i == 0 and j == 0):
            after_1 = sentences[i][j+1][0][1]
            after_2 = sentences[i][j+2][0][1]
        elif (i == 0 and len(sentences[i])-1 == j):
            after_1 = sentences[i+1][0][0][1]
            after_2 = sentences[i+1][1][0][1]
            before_1 = sentences[i][j-1][0][1]
            before_2 = sentences[i][j-2][0][1]