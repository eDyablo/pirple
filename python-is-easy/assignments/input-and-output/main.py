'''
Homework assignment for the 'Python is easy' course by Pirple.

Written by Ed Yablonsky
'''

import os

def askUser(prompt):
    answer = ''
    while answer == '':
        answer = input(prompt)
    return answer

def askFileName():
    return askUser('Input file name: ')

def askFileOption(fileName):
    print('What do you want to do with the ' + fileName + ' file?')
    print('A) Read the file')
    print('B) Delete the file and start over')
    print('C) Append the file')
    print('D) Replace a single line')
    return askUser('Select the option: ')

def displayFile(filename):
    with open(fileName) as file:
        for line in file:
            print(line, end='')
    print()

def addTextToFile(fileName):
    text = askUser('Please enter the text to be added to the ' + fileName + ' file:\n')
    with open(fileName, 'a') as file:
        file.write(text)
        file.write('\n')

def replaceFileLine(fileName, lineToReplace):
    text = askUser('Please enter the text to replace line ' + str(lineToReplace) + ' of ' + fileName + ' file:\n')
    lines = []
    with open(fileName) as file:
        lines = file.readlines()
    with open(fileName, 'w') as file:
        lineNumber = 1
        for line in lines:
            lineToWrite = line
            if lineNumber == lineToReplace:
                lineToWrite = text + '\n'
            file.write(lineToWrite)
            lineNumber += 1

def wipeOutFileContent(fileName):
    open(fileName, 'w').close()

fileName = askFileName()

if os.path.isfile(fileName):
    print('The specified file', fileName, 'already exists.')
    option = askFileOption(fileName).lower()
    if option == 'a':
        displayFile(fileName)
    elif option == 'b':
        wipeOutFileContent(fileName)
        addTextToFile(fileName)
    elif option == 'c':
        addTextToFile(fileName)
    elif option == 'd':
        lineToReplace = int(askUser('Enter the line number you want to update: '))
        replaceFileLine(fileName, lineToReplace)
else:
    addTextToFile(fileName)
