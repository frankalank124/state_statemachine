"""@package docstring state_machine.py

Contains:
StateMachine class

Edited: 1/22/2014
Last Edit by: Johnny Mao
"""

#python imports
import threading
import time
import inspect
import traceback

#project imports
import state

class StateMachine(threading.Thread):
    """StateMachine
    TODO: Add stuff to this documentation comment 
    """


    def __init__(self, machineID, currentStateID = None, states = {}):
        super(StateMachine, self).__init__()
        
        self.machineID = machineID
        self.currentStateID = currentStateID
        self.lastTransition = "NO_TRANS"
        self.currentTransition = "NO_TRANS"
        
        # mapping of state IDs and instantiated states
        self.states = {"END" : state.End(self)}
        self.states.update(states)

        
    def run(self):
        """run
        main functionality is in here
        also required by threading.Thread.start()

        """
        try:
            while not self.isComplete():
                self.startState()
                self.getTransition()
                self.doTransition()
            
        except Exception as fatal:
            print traceback.format_exc() # currently prints, later log

           
    def startState(self):
        """start_state
        function is called to perform whatever the entering state needs to do

        **note: this one line could be written in place of the function call
        within the above thread
        """
        self.states[self.currentStateID].enterState(self.lastTransition)()


    def getTransition(self, pause = 0.05):
        """get_transition
        this function is used to update the current transition that the
        StateMachine will be using to perform transitions
        """
        
        while(self.currentTransition == "NO_TRANS"):
            self.currentTransition = self.states[self.currentStateID]\
                                      .getTransition()
            time.sleep(pause)


    def doTransition(self):
        """do_transition
        performs transitions
        """

        self.states[self.currentStateID].leaveState(self.currentTransition)()
        self.currentStateID = self.states[self.currentStateID]\
                              .getState(self.currentTransition)
        self.lastTransition = self.currentTransition
        self.currentTransition = "NO_TRANS"


    def isComplete(self):
        """is_complete
        indicates that this StateMachine has reached a terminating State.
        """
        return self.states[self.currentStateID].isEnd()

    def leave(self):
        self.currentTransition = "END"

    

    
