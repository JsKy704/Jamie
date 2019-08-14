###############################################################################################
######################################## For option 1 #########################################
###############################################################################################
                                                                                            ###
def decompressionfor1():                                                                    ###
    list1=[]                                                                                ###         #making a list to store all the final outputs
    number=0                                                                                ###
    number= int(input('Please enter the number of lines that the file has: '))              ###         #converts the number into integer
    while number <= 2:                                                                      ###         #if the number is smaller than 2, which was the input above
        print('Invalid Number')                                                             ###         #will print invalid number if the number is smaller than 3
        number=int(input('Please enter your number again: '))                               ###
    print('Now please start entering your compressed strings ')                             ###
    for i in range (number):                                                                ###         #number will be the input number and the for loop will stop when the number reaches 0
        StartStr=input()                                                                    ###         #will be the user input. loop the number of times
        FinalStr=''                                                                         ###
        length=len(StartStr)-1                                                              ###         #getting the length of the line
        for i in range(0,length,3):                                                         ###         #the 2 is used to see the numbers only while 0 is for the first number
            number=int(StartStr[i] + StartStr[i+1])                                         ###         #since 0 and 1 position would be a character eg 01 (2 letters)
            character=StartStr[i+2]                                                         ###         
            FinalStr=FinalStr+(character*number)                                            ###         #FinalStr will be the number found above multiply but the character
        list1.append(FinalStr)                                                              ###         #using append to continuously put lines in a list
                                                                                            ###
    for line in list1:                                                                      ###         #for every line/item in the list
        print(line)                                                                         ###         #prints all the lines
                                                                                            ###
###############################################################################################
######################################## For option 2 #########################################
###############################################################################################
                                                                                            ###
def ImportFilefor2():                                                                       ###        
    while True:                                                                             ###         #keeps the loop
         filename=input('Please input the file name with .txt in the end : ')               ###         #requir .txt since it is included in the whole filename
         try:                                                                               ###            
             with open(filename,'r') as f:                                                  ###         #open file for reading
                 f_contents = f.readlines()                                                 ###         #read() method returns all content in the file
         except FileNotFoundError:                                                          ###         #if the filename is not found in the file
            print('This file cannot be found, please enter again')                          ###         #requires the person and enter again
         else:                                                                              ###         #otherwise
            break                                                                           ###         #break the loop after finding the file
                                                                                            ###
    theFile = []                                                                            ###         #storing the contents into a list
    for line in f_contents:                                                                 ###         #conditional for loop
        theFile.append(line.rstrip('\n'))                                                   ###         #all characters has been striped in the end of the string (white characters)
                                                                                            ###
    print('')                                                                               ###         #decoration purposes
    print('')                                                                               ###
    for item in theFile:                                                                    ###         #for every line in theFile
        print(item)                                                                         ###         #prints the content in theFile
    print('')                                                                               ###
    print('')                                                                               ###    
                                                                                            ###
###############################################################################################
######################################## For option 3 #########################################
###############################################################################################
                                                                                            ###
def decompressionfor3():                                                                    ###
    while True:                                                                             ###         #keeps the loop continuing if the file isnt found
        filename=input('Please input the file name : ')                                     ###         #requir .txt since it is included in the whole filename
        try:                                                                                ###            
            with open(filename,'r') as f:                                                   ###         #open file for reading
                f_contents = f.readlines()                                                  ###         #read() method returns all content in the file
        except FileNotFoundError:                                                           ###         #if the filename is not found in the file
            print('This file cannot be found, please enter again')                          ###         #requires the person and enter again
        else:                                                                               ###         #otherwise
            break                                                                           ###         #break the loop after finding the file
                                                                                            ###
    theFile = []                                                                            ###         #storing the contents of the file into a list
    list1=[]                                                                                ###         #list1 for storing the final output  
    for line in f_contents:                                                                 ###         #conditional for loop
        theFile.append(line.rstrip('\n'))                                                   ###         #all characters has been striped in the end of the string (white characters)
        StartStr=(line)                                                                     ###         #the input for StartStr will be the line in the file
        FinalStr=''                                                                         ###    
        length=len(StartStr)-1                                                              ###         #getting the length of the line
        for i in range(0,length,3):                                                         ###         #the 2 is used to see the numbers only while 0 is for the first number
            number=int(StartStr[i] + StartStr[i+1])                                         ###            
            character=StartStr[i+2]                                                         ###         #since 0 and 1 position would be a character eg 01 (2 letters)
            FinalStr=FinalStr+(character*number)                                            ###            
        list1.append(FinalStr)                                                              ###         #continously put the output in the list
                                                                                            ###            
    for line in list1:                                                                      ###         #for every line in list
        print(line)                                                                         ###         #prints every line
                                                                                            ###
                                                                                            ###
                                                                                            ###
###############################################################################################
######################################## For option 4 #########################################
###############################################################################################
                                                                                            ###
def lengthofasciifor4():                                                                    ###
    while True:                                                                             ###         #keeps the loop continuing if the file isnt found
        filename=input('Please input the ascii art file name with .txt in the end : ')      ###         #requir .txt since it is included in the whole filename
        try:                                                                                ###
            with open(filename,'r') as f:                                                   ###         #open file for reading
                f_contents = f.readlines()                                                  ###
                f_contents2 = f.readlines()                                                 ###         #read() method returns all content in the file
        except FileNotFoundError:                                                           ###         #if the filename is not found in the file
            print('This file cannot be found, please enter again')                          ###         #requires the person and enter again
        else:                                                                               ###
            break                                                                           ###         #break the loop after finding the file
                                                                                            ###
    characters1 = 0                                                                         ###         #puts the character into 0 before counting
    for line in f_contents:                                                                 ###         #conditional for lines
        line = line.replace('\n', '')                                                       ###         #/n could be counted as a character so it is replaced with a space instead
        characters1 = characters1 + len(line) - line.count(' ')                             ###         #find the total number of character and deduct the spaces
                                                                                            ###
    list1=[]                                                                                ###
    for line2 in f_contents2:                                                               ###         #conditional for loop                                       
        StartStr=(line2)                                                                    ###
        CompStr=""                                                                          ###
        Counter=0                                                                           ###         #set counter for 0 before counting
        previous=StartStr[0]                                                                ###         #set the previous to the first letter
        for letter in StartStr:                                                             ###         #for every letter in the line
            if letter==previous:                                                            ###         #e.g. bbwww, when they reach w, they will then look at b to see that its different
                Counter=Counter+1                                                           ###         #counting the number of Bs
            else:                                                                           ###
                y = str (Counter)                                                           ###
                if int(Counter) < 10:                                                       ###
                    y = '0' + str (Counter)                                                 ###
                CompStr=CompStr+y+previous                                                  ###
                previous=letter                                                             ### 
                Counter=1                                                                   ###         #to change the program to focus on the current letter
                                                                                            ###
        CompStr=CompStr+str(Counter)+previous                                               ###
        list1.append(CompStr)                                                               ###         #puts the output in the list
    list1 = str(list1)                                                                      ###         #converts the list into str since .write can only read str
                                                                                            ###
    while True:                                                                             ###
        filename1=input('Please input the new text file for storage with .txt in the end: ')###
        try:                                                                                ###         
            with open(filename1,'w') as f:                                                  ###         # puts file as write
                f.write(list1)                                                              ###         #input contents of list1 into the file
        except FileNotFoundError:                                                           ###
            print('This file could not be found, Please enter again')                       ###`
        else:                                                                               ###
            break                                                                           ###
                                                                                            ###
    characters2 = 0                                                                         ###         #set to 0 before counting
    characters3 = 0                                                                         ###      
    for line in list1:                                                                      ###         #conditional for loop to count
        characters2 = characters2 + len (line)                                              ###         #find the length of the list
                                                                                            ###
    characters3 = characters1 - characters2                                                 ###         #the total sum of characters in LogoArt.txt - the total sum of characters in the new text file
    print ('The difference in character of both text files are', characters3, 'letters')    ###         #outputs the total difference in number
                                                                                            ###
###############################################################################################
###############################################################################################
###############################################################################################
option=''
while option != '5' :                                                                                   #while option does not equal to 5
    print('''         #####################################
        #  Please choose from the following : #
        #        1. Enter RLE                 #
        #        2. Display ASCII Art         #
        #        3. Convert to ASCII art      #
        #        4. Convert to RLE            #
        #        5. Quit                      #
         ####################################

         ''')                                                                                           #menu
    option=(input('      Please choose your option : '))                                                #asks for user input
    print('')                                                                                           #decoration purposes
    print('')

    if option == '1':                                                                                   #if option 1 is chosen, the define made above will be used
        decompressionfor1()

    elif option == '2':
        ImportFilefor2()

    elif option == '3':
        decompressionfor3()
        
    elif option == '4':
        lengthofasciifor4()
        
    elif option == '5':                                                                                 #however if option 5 is chosen, the user will be have ended the program
        print('You are leaving the program. Goodbye')
        menu()
