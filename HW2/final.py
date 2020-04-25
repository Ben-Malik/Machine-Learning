from nltk import pos_tag,word_tokenize
article = open("love.txt", "r") 
abstract_file = open("100-400.txt", "r")
concrete_file = open("400-700.txt", "r")

sentences = list()
abstract_words = list()
concrete_words = list()

for line in article.readlines():
    current = line.strip().split(' ')
    output = list()
    for word in current:
        word = word.strip(',.()\'\"').upper()
        output.append(word)
    sentences.append(output)


#Pos for each word
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        before_1 = None
        before_2 = None
        after_1 = None
        after_2 = None
        output = list()
        word = pos_tag(word_tokenize(sentences[i][j]))[0][1]
        if (i == 0):
            if (j == 0):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
            elif (j == 1):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]
            elif (j == len(sentences[i])-1):
                after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            elif (j == len(sentences[i])-2):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            else: 
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]   
        elif (i == len(sentences)-1 and j == len(sentences[i])-1):
            before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
            before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
        elif (i == len(sentences)-1 and j == len(sentences[i])-2):
            before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
            before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
        else: 
            if (j == 0): 
                before_1 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
            elif (j == 1):
                before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
            elif (j == len(sentences[i])-1):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]
            elif ( j == len(sentences[i])-2):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
            else: 
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
        output.append(before_2)
        output.append(before_1)
        output.append(sentences[i][j])
        output.append(word)
        output.append(after_1)
        output.append(after_2)
        #elif (i == 0 and len(sentences[j])-2 - j != 0):
        # if len(sentences) - i - 1 == 0:
        #     if len(sentences[i][j]) - j - 1 == 0:
        #         after_1 = pos_tag(word_tokenize(sentences[i][j+1]))
        #         after_2 = pos_tag(word_tokenize(sentences[i+1][0]))
        #     else:
        #         after_1 = pos_tag(word_tokenize(sentences[i][j+1]))
        #         after_2 = pos_tag(word_tokenize(sentences[i][j+2]))
        # if len(sentences[i][j]) - j - 2 == 0:
        #     print("Hello")

        print(output)

