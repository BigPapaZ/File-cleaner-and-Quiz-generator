#####################
# shakespearquiz.py
# Zaigham
# Generates an interactive quiz for plays
#####################

import random
import sys



def readPlay(file_name):
    '''Takes the file name as an input and opens, reads, cleans, and then returns it. 
    Input: File name
    Output: The edited version of the play data
    '''


    #reading the file
    with open(file_name, "r") as f:
        plainText = f.read()
        f.close()

    #splitting the file into acts
    new = plainText.split("ACT")
    new.pop(0)   #had to be removed

    #A list accumulator which will hold the final processed data
    play = []

    for i in new:                          #Iterating through the data. 'i' is the iterating variable.
        x = i[i.index("S"):]               #It needs to be processed
        act = x.split("SCENE")             #Breaking the act into a list of Scenes
        ACT = []
        for b in act:                      #Iterating for the scenes. b is the iterating variable and represents the scenes
            scene = b.split("\n")          #Removing the indent at the end of each sentence
            scene.pop(0)                   #Needs to be removed
            if len(scene) == 0: continue   #Making the process a bit faster. Some of the interating varaiables' instances were empty
            scene.pop()                    #needed to be removed
            dialogue_dict = {}             #A dictionary to later hold the character names along with its dialogue (in a list)
            for aline in scene:
                if aline == aline.upper(): #Characters are all in caps
                    if aline not in dialogue_dict: #addind the character names to the dictionary
                        dialogue_dict[aline] = []


            #A lot of accumulators and stuff. I would advice to just skip to the next block
            acc1 = 0
            acc4 = 1
            for i in range(len(scene)):
                if scene[i] == scene[i].upper():
                    if acc1 == 0:
                        acc2 = i
                        acc1 = 1
                        kivo = scene[i]
                    elif acc1 == 1:
                        acc3 = i
                        acc4 = 0
                        acc1 = 0
                if acc4 == 0:
                    properstuff = []
                    for y in range(acc2 + 1, acc3):
                        properstuff += [scene[y]]
                    dialogue_dict[kivo] += properstuff
                    acc4 = 1



            #Deleting the characters who didn't say anything but somehow popped up in the dictionary
            for dialogues in list(dialogue_dict.keys()):
                if len(dialogue_dict[dialogues]) == 0: del dialogue_dict[dialogues]

            #adding a scene's dictionary to the specific acts's list
            ACT += [dialogue_dict]
        play += [ACT]

    return play


'''
Takes a play and a series of indices into that play: an act, scene, character name, and an index into that character's list of lines and prints out a multiple-choice question about which character says that particular line in that particular act and scene. The last parameter is the number of the question. This function returns the letter associated with the correct answer (a, b, c, or d)
'''
def printQuestion(play, actIndex, sceneIndex, characterName, lineIndex, questionNum):
   
    #Print the question
    print("Question " + str(questionNum) + ": In act " + str(actIndex + 1) + ", scene " + str(sceneIndex + 1) + ", who says:")
    print('"' + play[actIndex][sceneIndex][characterName][lineIndex] + '"')

    #Now we have to build the list of choices the user
    #will choose from
    choices = [characterName]

    #Get the list of characters in the scene
    characterList = list(play[actIndex][sceneIndex].keys())
    characterList.remove(characterName)
    if len(characterList) > 3:
        #Pick 3 random alternate choices from the scene
        for i in range(3):
            idx = random.randint(0, len(characterList) - 1)
            choices.append(characterList[idx])
            characterList.pop(idx)
    else:
        #There are 4 or fewer characters in the scene
        #Just add all the characters to the list
        choices += characterList
            
    #Place the correct character in a random position
    #in the list of answers
    correctPos = random.randint(0, len(choices) - 1)
    tmp = choices[correctPos]
    choices[correctPos] = choices[0]
    choices[0] = tmp
        
    #Print the choices
    answerList = 'abcd'
    for i in range(len(choices)):
        print(answerList[i] + ") " + choices[i])
    
    return answerList[correctPos]


def main():
    '''Takes a play's text filename as an input and then gives the user an interactive quiz testing their memory about 
    the dialogues in the play. It at first edits the data into a specific format by calling another function. Then it 
    calls another function which will print a quiz question and return the correct answer. It handles with the rest of 
    the user interaction.
    '''

    #Setting up accumulators later to be used
    questionNum=0
    number_correct_answers=0


    file_name = sys.argv[1]

    play=readPlay(file_name)           #calling the readPlay function to convert the input data into the required format

    file = open(file_name, 'r')
    title=file.readline()     #reading the heading of the file
    print("How well do you know", title.strip()+"?", "\n", "Let's find out!")
    file.close()



    while True:
        questionNum+=1


        #Genenating random numbers for the acts, scenes, and characters to be called later on.
        #Also generating the inputs for the printQuestion() function.
        actIndex=random.randint(0,len(play)-1)
        sceneIndex=random.randint(0,len(play[actIndex])-1)
        list_of_characters=list(play[actIndex][sceneIndex].keys())
        characterName=list_of_characters[random.randint(0,len(list_of_characters)-1)]
        lineIndex=random.randint(0,len(play[actIndex][sceneIndex][characterName])-1)

        #calling the printQuestion
        answer=printQuestion(play, actIndex, sceneIndex, characterName, lineIndex, questionNum)


        #A lot of user interface stuff
        user_answer=input("Your answer:",)

        while user_answer not in ['a','b','c','d']:
            print("I don't understand. Please type a, b, c, or d.")
            user_answer = input("Your answer:", )

        if user_answer==answer:
            print ("Correct!")
            number_correct_answers+=1
        else:
            print("Sorry, the correct answer was", characterName)

        print("\nYour current score is:", str(number_correct_answers)+"/"+str(questionNum),"\n")
        continue_command=input("Do you want another question? (y/n):")

        while continue_command not in ["y","n"]:
            print ("I don't understand. Please type y or n.")
            continue_command = input("Do you want another question? (y/n):")

        if continue_command=="n":
            print("Your final score was:", str(number_correct_answers)+"/"+str(questionNum))
            sys.exit()

main()