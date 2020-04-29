from nltk import pos_tag,word_tokenize
article = open("love.txt", "r") 


def isWordConcrete(word): 
    abstract_file = open("100-400.txt", "r")
    concrete_file = open("400-700.txt", "r")
    is_concrete = False
    is_word_found = False

    for line in abstract_file.readlines():
        current = line.split("\t")

        if (word.lower() == current[0].split(" ")[0].lower()):
            is_word_found = True
            break
    if not is_word_found:
        for line in concrete_file.readlines():
            current = line.split("\t")
            
            if (word.lower() == current[0].split(" ")[0].lower()):
                is_concrete = True
                is_word_found =True
                break
    return is_concrete
    
def getWordSubjectiveness(word): 
    subsective_file = open("subjectives.tff", "r")
    isWordWeak = False
    isWordStrong = False
    for line in subsective_file.readlines():
        current = line.split()
        if (word.lower() == current[2].split("=")[1].lower()):
            output = current[0].split("=")[1]
            if (output == "weaksubj"): 
                isWordWeak = True
            else:
                isWordStrong = True

            break
    return (isWordStrong, isWordWeak)

def checkForPositivenessNegativeness(word):
    senti_word_net_file = open("SentiWordNet_3.0.0.txt", "r")
    isInPositive = False
    isInNegative = False
    wordFound = False
    for line in senti_word_net_file.readlines():
        current = line.split("\t")
        words = current[4].split(' ')
        for i in range(len(words)):
            if (words[i].split("#")[0].lower() == word.lower()):
                if (current[2]!='0'):
                        isInPositive = True
                if (current[3]!='0'):
                    isInNegative = True
                wordFound = True
            
            break
        if (wordFound == True):
            break

    return (isInPositive, isInNegative)

class Word:
    def __init__(self, w, w_pos, before_1_pos, before_2_pos, after_1_pos, after_2_pos, is_positive, is_negative, is_before_1_positive, is_before_1_negative, is_before_2_positive, is_before_2_negative, is_after_1_positive, is_after_1_negative, is_after_2_positive, is_after_2_negative, is_weak, is_strong):
        self.w = w
        self.w_pos = w_pos
        self.before_1_pos = before_1_pos
        self.before_2_pos = before_2_pos
        self.after_1_pos = after_1_pos
        self.after_2_pos = after_2_pos
        self.is_positive = is_positive
        self.is_negative = is_negative
        self.is_before_1_positive = is_before_1_positive
        self.is_before_1_negative = is_before_1_negative
        self.is_before_2_positive = is_before_2_positive
        self.is_before_2_negative = is_before_2_negative
        self.is_after_1_positive = is_after_1_positive
        self.is_after_1_negative = is_after_1_negative
        self.is_after_2_positive = is_after_2_positive 
        self.is_after_2_negative = is_after_2_negative
        self.is_weak = is_weak
        self.is_strong = is_strong
        self.is_concrete = isWordConcrete(w)
        
    
    def isConcrete(self):
        return self.is_concrete


    def toString(self): 
        return self.before_1_pos + " <-- " + self.before_2_pos + " <- " + self.w + " - " + self.w_pos + ' -> ' + self.after_1_pos + " --> " + self.after_2_pos

    def positivenessStringify(self):
        return self.is_before_2_positive , self.is_before_1_positive, self.is_positive,  self.w, self.is_negative, self.is_after_1_negative, self.is_after_2_negative

    def subjectivenessStringify(self):
        return self.is_weak, self.is_strong

    def equals(self, word):
        return word.is_strong == self.is_strong and word.is_weak == self.is_weak and word.is_positive == self.is_positive and word.is_negative == self.is_negative and word.is_before_1_positive == self.is_before_1_positive and word.is_before_1_negative == self.is_before_1_negative and word.is_before_2_positive == self.is_before_2_positive and word.is_before_2_negative == self.is_before_2_negative and word.is_after_1_positive == self.is_after_1_positive and word.is_after_1_negative == self.is_after_1_negative and word.is_after_2_positive == self.is_after_2_positive and word.is_after_2_negative == self.is_after_2_negative and word.w_pos == self.w_pos and word.before_1_pos == self.before_1_pos and word.before_2_pos == self.before_2_pos and word.after_1_pos == self.after_1_pos and word.after_2_pos == self.after_2_pos

class Group: 

    def __init__(self, words):
        self.group = list()
        self.groupAbstactness = 0.0
        self.groupConcreteness = 0.0

        for word in words:
            self.group.append(word)
    
    def __init__(self):
        self.group = list()
    
    def addWord(self, word):
        self.group.append(word)
    
    def computeProbs(self):
        total = len(self.group)
        concrete = 0
        for word in self.group:
            if (word.isConcrete()):
                concrete+=1
        self.groupConcreteness = concrete/total
        self.groupAbstactness = (total-concrete)/total
        return (self.groupConcreteness, self.groupAbstactness)

    def getConcretenessProb(self):
        return self.groupConcreteness
    
    def getAbstractnessProb(self):
        return self.groupAbstactness
    
    def toString(self):
        for word in self.group:
            print(word.toString())

class Sentence:
    def __init__(self, words):
        self.sentence = list()
        self.groups = list()
        for word in words:
            self.sentence.append(word)
    def __init__(self):
        self.sentence = list()
        self.groups = list()

    def addWord(self, word):
        self.sentence.append(word)

    def addGroup(self, group):
        self.groups.append(group)

    def toString(self): 
        for word in self.sentence:
            print(word.toString())

allSentences = list()
sentences = list()
abstract_words = list()
concrete_words = list()
entire_article = list()

def readArticle():
    for line in article.readlines():
        current = line.strip().split(' ')
        output = list()
        for word in current:
            word = word.strip(',.()\'\"').upper()
            output.append(word)
        sentences.append(output)

def parseToSentences():
    #Pos for each word
    for i in range(len(sentences)):
        sentence = Sentence()
        for j in range(len(sentences[i])):
            before_1 = "No Before 1"
            before_2 = "No Before 2"
            after_1 = "No After 1"
            after_2 = "No After 2"
            word_before_1 = ""
            word_before_2 = ""
            word_after_1 = ""
            word_after_2 = ""
            subjectiveness = getWordSubjectiveness(sentences[i][j])
            is_weak = subjectiveness[1]
            is_strong = subjectiveness[0]
            output = list()
            word = pos_tag(word_tokenize(sentences[i][j]))[0][1]
            if (i == 0):
                if (j == 0):
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                    word_after_1 = sentences[i][j+1]
                    word_after_2 = sentences[i][j+2]
                elif (j == 1):
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                    before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]

                    word_after_1 = sentences[i][j+1]
                    word_after_2 = sentences[i][j+1]
                    word_before_1 = sentences[i][0]
                elif (j == len(sentences[i])-1):
                    if (i != len(sentences)-1):
                        after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                        after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]
                    before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]

                    if (i != len(sentences)-1):
                        word_after_1 = sentences[i+1][0]
                        word_after_2 = sentences[i+1][1]
                    word_before_1 = sentences[i][j-1]
                    word_before_2 = sentences[i][j-2]
                elif (j == len(sentences[i])-2):
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    if (i != len(sentences)-1):
                        after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]

                    before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]

                    word_after_1 = sentences[i][j+1]
                    if (i != len(sentences)-1):
                        word_after_2 = sentences[i+1][0]
                    word_before_1 = sentences[i][j-1]
                    word_before_2 = sentences[i][j-2]
                else: 
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                    before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]   

                    word_after_1 = sentences[i][j+1]
                    word_after_2 = sentences[i][j+2]
                    word_before_1 = sentences[i][j-1]
                    word_before_2 = sentences[i][j-2]
            elif (i == len(sentences)-1 and j == len(sentences[i])-1):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]

                word_before_1 = sentences[i][j-1]
                word_before_2 = sentences[i][j-2]
            elif (i == len(sentences)-1 and j == len(sentences[i])-2):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]

                word_before_1 = sentences[i][j-1]
                word_before_2 = sentences[i][j-2]
                word_after_1 = sentences[i][j+1]
            else: 
                if (j == 0): 
                    before_1 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-2]))[0][1]
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]

                    before_word_1 = sentences[i-1][len(sentences[i-1])-1]
                    before_word_2 = sentences[i-1][len(sentences[i-1])-2]
                    after_word_1 = sentences[i][j+1]
                    after_word_2 = sentences[i][j+2]
                elif (j == 1):
                    before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]

                    before_word_1 = sentences[i][0]
                    before_word_2 = sentences[i-1][len(sentences[i-1])-1]
                    after_word_1 = sentences[i][j+1]
                    after_word_2 = sentences[i][j+2]
                elif (j == len(sentences[i])-1):
                    before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                    after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]

                    before_word_1 = sentences[i][j-1]
                    before_word_2 = sentences[i][j-2]
                    after_word_1 = sentences[i+1][0]
                    after_word_2 = sentences[i+1][1]
                elif ( j == len(sentences[i])-2):
                    before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]

                    before_word_1 = sentences[i][j-1]
                    before_word_2 = sentences[i][j-2]
                    after_word_1 = sentences[i][j+1]
                    after_word_2 = sentences[i+1][0]
                else: 
                    before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                    before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                    after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                    after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]

                    before_word_1 = sentences[i][j-1]
                    before_word_2 = sentences[i][j-2]
                    after_word_1 = sentences[i][j+1]
                    after_word_2 = sentences[i][j+2]

            is_positive = checkForPositivenessNegativeness(sentences[i][j])[0]
            is_negative = checkForPositivenessNegativeness(sentences[i][j])[1]  

            is_word_before_1_positive = checkForPositivenessNegativeness(word_before_1)[0]
            is_word_before_1_negative = checkForPositivenessNegativeness(word_before_1)[1]

            is_word_before_2_positive = checkForPositivenessNegativeness(word_before_2)[0]
            is_word_before_2_negative = checkForPositivenessNegativeness(word_before_2)[1]

            is_word_after_1_positive = checkForPositivenessNegativeness(word_after_1)[0]
            is_word_after_1_negative = checkForPositivenessNegativeness(word_after_1)[1]

            is_word_after_2_positive = checkForPositivenessNegativeness(word_after_2)[0]
            is_word_after_2_negative = checkForPositivenessNegativeness(word_after_2)[1] 
    
            myWord = Word(sentences[i][j], word, before_1, before_2, after_1, after_2, is_positive, is_negative, is_word_before_1_positive, is_word_before_1_negative, is_word_before_2_positive, is_word_before_2_negative, is_word_after_1_positive, is_word_after_1_negative, is_word_after_2_positive, is_word_after_2_negative, is_weak, is_strong)
            # print(myWord.positivenessStringify())
            # print(myWord.subjectivenessStringify())
            sentence.addWord(myWord)
            entire_article.append(myWord)
        allSentences.append(sentence)
        
def groupifyAll():
    tempWords = entire_article.copy()
    allGroups = list()
    while tempWords:
        currentGroup = Group()
        currentWord = tempWords[len(tempWords)-1]
        for i in range(len(tempWords)-1, -1, -1):
            if (tempWords[i].equals(currentWord)):
                currentGroup.addWord(tempWords[i])
                del tempWords[i]
        currentGroup.computeProbs()
        allGroups.append(currentGroup)
    return allGroups


    
def groupifyBySentence():

    tempSentences = allSentences.copy()
    for sentence in tempSentences:
        tempSentence = sentence.sentence.copy()
        while tempSentence:
            currentGroup = Group()
            currentWord = tempSentence[len(tempSentence)-1]
            for i in range(len(tempSentence)-1, -1, -1):
                if (tempSentence[i].equals(currentWord)):
                    currentGroup.addWord(tempSentence[i])
                    del tempSentence[i]
            sentence.addGroup(currentGroup)
    return tempSentences

readArticle()
parseToSentences()
allGroups = groupifyAll()
for group in allGroups:
    print(group.computeProbs())
    group.toString()
