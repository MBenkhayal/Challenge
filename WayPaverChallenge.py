# Muhammed Benkhayal, WayPaver Challenge


'''
Although there is a Python extension for computing the Levenshtein distance, I decided
to write the implementation completely separate from the extension so that my program
can run on any machine that has Python 3.4 and there is no need for the user to get
any extra extensions.
'''

'''
This function basically just calculates the distance, and returns 0 if the distance
is greater than 1, or the string if it is valid
'''
def levDistance(s1, s2):
    distance = 0
    is2 = s2
    if (len(s1) > len(s2)):
        temp = s1
        s1 = s2
        s2 = temp
    distance += (len(s2) - len(s1))
    for i in range(len(s1)):
            if (s1[i] != s2[i]):
                distance += 1
                if (distance == 2):
                    return 0
    return is2
'''
The loop function allows me to call levDistance using the word on every word in the
user given list
'''
def loop(origWord, wordList, friendList):
    for i in range(len(wordList)):
        if (origWord != wordList[i] and (abs((len(origWord) - len(wordList[i]))) < 2)):
            temp = levDistance(origWord, wordList[i])
            if (temp != 0):
                friendList.append(temp)

inFile = input('What is the name of the file containing the word list you would like to use? ')
wordList = []
data = open(inFile, 'r')
for line in data:
    wordList.append(line.rstrip('\n'))
data.close()

origWord = input('What word would you like to find a social network for? ')

'''
Originally, I was just going to print out the matching word and/or store them in a single
list. However, storing them in separate lists based on their ordering in the social network
allows the data to be used in other ways if desired later on. Also, this makes it so that
if there is a person who is a friend of a person, then person two is also a friend of person
one (ie both people will be on both lists
'''

origFriends = []
loop(origWord, wordList, origFriends)
if (len(origFriends) != 0):
    print('The original friends:')
    print(origFriends)

    orig2XFriends = []
    for i in range(len(origFriends)):
        loop(origFriends[i], wordList, orig2XFriends)
    if (len(orig2XFriends) != 0):
        print('The original friends friends:')
        print(orig2XFriends)

        orig3XFriends = []
        for i in range(len(orig2XFriends)):
            loop(orig2XFriends[i], wordList, orig3XFriends)
        if (len(orig3XFriends) != 0):
            print('The friends of friends of friends:')
            print(orig3XFriends)
