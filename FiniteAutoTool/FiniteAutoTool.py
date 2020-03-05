import os
import sys

class FA_String_Parser:

    #convert string to array
    @staticmethod
    def ParseToList (delimeter,inputString):
        mylist = inputString.split(delimeter)
        return mylist
    # before parsing lets make sure there arent dupes in the string
    @staticmethod
    def CheckStringForDuplicate (delimeter, inputString):
        mylist = inputString.split(delimeter)
        length = len(mylist) 
   
        for i in range(length): 
            mylist[i] = mylist[i].strip()

        return (len(mylist) != len(set(mylist)))


    @staticmethod
    def CheckIfListContainsString (myString, myList):
        for i in myList:
            if myString == i:
                return True
        return False
    @staticmethod
    def CheckIfListContainsList (myStringList, myList):
        count = 0
        for i in myStringList:
            for j in myList:
                if (i == j):
                    count += 1

        if (count == len (myStringList)):
            return True
        else:
            return False

            
class FiniteAuto:

    states = []
    alphabet = []
    startpoint = ""
    acceptstates = []

    def __init__ (self, states, alphabet, startpoint, acceptstates):
        print ("[+] initializing Finite App")
        self.states = states
        self.alphabet = alphabet
        self.startpoint = startpoint
        self.acceptstates = acceptstates

    


def init_call ():

    print ("********* Initializing Finite ***********")

    #check for dupes and process before going onto the next step
    s_states = input ("Please enter the states seperated by comma :")
    print (s_states)

    #if true crash
    if (FA_String_Parser.CheckStringForDuplicate (",",s_states)):
        print ("[!] Duplicate states please enter unique states!")
        init_call ()


    states = FA_String_Parser.ParseToList (",",s_states)


    if (len(states) < 2):
        print ("[!] Please enter more than one states")
        init_call ()


    #print (str(len(states)))

    s_alphabet = input ("Please enter the alphabet seperated by comma :")
    print (s_alphabet)


    if (FA_String_Parser.CheckStringForDuplicate (",",s_alphabet)):
        print ("[!] Duplicate alphabet please enter unique alphabet!")
        init_call ()

    alphabet = FA_String_Parser.ParseToList (",",s_alphabet)


    # these will need to be checked to make sure they exist in our state list

    s_start = input ("Please enter the start state (must be one of the previously entered states) : ")
    print (s_start)

    if (not FA_String_Parser.CheckIfListContainsString (s_start, states)):
        print ("[!] State was not found in state list!")
        init_call ()


    s_accept = input ("Please enter the accept states seperated by comma : ")
    print (s_accept)


    if (FA_String_Parser.CheckStringForDuplicate (",",s_accept)):
        print ("[!] Duplicate accept states please enter unique accept states!")
        init_call ()


    AcceptStates = FA_String_Parser.ParseToList (",",s_accept)
    if (not FA_String_Parser.CheckIfListContainsList (AcceptStates, states)):
        print ("[!] States were not found in state list!")
        init_call ()

    return FiniteAuto(states, alphabet, s_start, AcceptStates)



# create a finite auto class to process and create a table


fa = init_call ()

#print (fa.startpoint)
