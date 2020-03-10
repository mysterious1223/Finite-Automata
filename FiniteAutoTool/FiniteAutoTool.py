import os
import sys
from terminaltables import AsciiTable
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
    #mylist = list of all states and mystringlist is all accept states
    @staticmethod
    def CheckIfListContainsList (myStringList, myList):

        count = 0
        for i in myList:
            

            for j in myStringList:
                if (i == j):
                    count += 1
                    

        if (count == len (myStringList)):
            return True
        else:
            return False

class State:

    symbol = ""
    accepting = False
    starting = False

    def __init__ (self, symbol, accepting, starting):
        self.symbol = symbol
        self.accepting = accepting
        self.starting = starting
    def print_details (self):
        print ("State: " + self.symbol, ", Accepting: " + str (self.accepting), ", Starting: " + str (self.starting))

class StateHandle:
 
    list_of_states = []

    def CreateState (self,symbol, accepting, starting):
        myState = State (symbol, accepting, starting)
        self.list_of_states.append (myState)
        print ("state created: " + symbol)
    def AppendState (self, s):
        self.list_of_states.append (s)
    def GetStateBySymbol (self, symbol):
        sym_list = FA_String_Parser.ParseToList (",", symbol)
        listofstates = []
        for i in sym_list:
            for s in self.list_of_states:
                if i == s.symbol:
                    listofstates.append (s)

        return listofstates
class Delta:
    thisState = State
    input = ""
    outState = []
    def __init__ (self, thisState, input, outState):

        self.thisState = thisState
        self.input = input
        self.outState = outState

    def print_info (self):
        if not self.outState == None:  
            print ("Delta of " + self.thisState.symbol + " at " + self.input + " is state " + self.getOutStates())
        else:
            print ("Delta of " + self.thisState.symbol + " at " + self.input + " is state EMPTY")


    def getOutStates (self):

        StateMaster = ""
        for i in self.outState:
            if StateMaster != "":
                StateMaster = StateMaster + ","
            StateMaster = StateMaster + i.symbol


        if StateMaster != "":
            return StateMaster
        return "Empty"

class Deltafunction:
    deltalist = []

    def CreateDelta (self, state , input, outstate):
        d = Delta (state, input, outstate)
        self.deltalist.append (d)
    
class FiniteAuto:

    s_states = []
    alphabet = []
    s_startpoint = ""
    s_acceptstates = []
    NFAStates = StateHandle()
    NFADelta = Deltafunction()

    def __init__ (self, states, alphabet, startpoint, acceptstates):
        print ("[+] initializing Finite App")
        self.alphabet = alphabet
          

        # use the above variable to create our states
        
        for s in states:
            tempState = State (s, False, False)
            
            if s == startpoint:
                tempState.starting = True
            
            for a in acceptstates:
                if s == a:
                    tempState.accepting = True
                    break
                else:
                    continue
            self.NFAStates.AppendState (tempState)
        
        

        self.list_states_debug_nfa()

        #states created, now we need to create delta
        # loop through states and ask user for inputs (size of alphabet)
    
        #self.NFADelta.CreateDelta (tempState, "0", tempState2)

        #for i in self.NFADelta.deltalist:
            #i.print_info()
        

        # fix this to restart on error - Create a function to handle this
        # delta needs to take a list of states as out state
        for s in self.NFAStates.list_of_states:
            print ("Delta of " + s.symbol)

            for i in self.alphabet:
                i_input = input("At " + i + " state: ")
                i_input = i_input.strip()
                i_input = i_input.replace (" ", "")
                # we need to find the output state
                # we can just rework this to return a list
                outState = self.NFAStates.GetStateBySymbol (i_input)

                if outState == None and i_input == "":
                    print ("Blank state selected")
                #elif outState == None and i_input != "":
                    #print ("Multiple states selected")

                    
                # create delta
                self.NFADelta.CreateDelta (s, i, outState)

        for i in self.NFADelta.deltalist:
            i.print_info()

        self.PrintNFATable()


    def list_states_debug_nfa (self):
       
       for i in self.NFAStates.list_of_states:
           i.print_details()

    def PrintNFATable(self):
        data = []
        header = ["delta"]

        for a in self.alphabet:
            header.append (a)

        data.append (header)

        currSym = ""
        row = []
        for d in self.NFADelta.deltalist:
            if currSym == "":
                row.append(d.thisState.symbol)
                row.append(d.getOutStates())
                print (d.getOutStates())
                currSym = d.thisState.symbol
            else:
                row.append(d.getOutStates())
                data.append (list (row))
                row.clear()
                currSym = ""

        table = AsciiTable(data)
        print (table.table)

def init_call ():

    print ("********* Initializing Finite ***********")

    #check for dupes and process before going onto the next step
    s_states = input ("Please enter the states seperated by comma :")
    
    s_states=s_states.strip()
    s_states=s_states.replace(" ","")
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
    s_alphabet=s_alphabet.strip()
    s_alphabet=s_alphabet.replace(" ","")

    if (FA_String_Parser.CheckStringForDuplicate (",",s_alphabet)):
        print ("[!] Duplicate alphabet please enter unique alphabet!")
        init_call ()

    alphabet = FA_String_Parser.ParseToList (",",s_alphabet)


    # these will need to be checked to make sure they exist in our state list

    s_start = input ("Please enter the start state (must be one of the previously entered states) : ")
    print (s_start)
    s_start=s_start.strip()
    s_start=s_start.replace(" ","")
    if (not FA_String_Parser.CheckIfListContainsString (s_start, states)):
        print ("[!] State was not found in state list!")
        init_call ()


    s_accept = input ("Please enter the accept states seperated by comma : ")
    print (s_accept)
    s_accept=s_accept.strip()
    s_accept=s_accept.replace(" ","")
    
    if (FA_String_Parser.CheckStringForDuplicate (",",s_accept)):
        print ("[!] Duplicate accept states please enter unique accept states!")
        init_call ()


    AcceptStates = FA_String_Parser.ParseToList (",",s_accept)
    if (not FA_String_Parser.CheckIfListContainsList (AcceptStates, states)):
        print ("[!] States were not found in state list!")
        init_call ()

    return FiniteAuto(states, alphabet, s_start, AcceptStates)



# create a finite auto class to process and create a table

#data = []

#data.append (["column1","column2"])

#table = AsciiTable(data)

#print (table.table)

#data = []

#r1 = ["a", "b", "c"]

#r2 = ["a1", "b1", "c1"]

#data.append (r1)

#data.append (r2)
#table = AsciiTable(data)

#print (table.table)

fa = init_call ()

#print (fa.startpoint)
