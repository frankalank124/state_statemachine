## @package state
#
# Contains:
# State class
# End class, inherits State
#
# Last edit: 2/20/2014
# Last edit by: Johnny Mao


#python imports
import copy

## Class State
# The State class is the base class that all states will inherit from.
#    
# Variables:
#   name: the unique identifier for any specific state
#   machine: this is a reference to the StateMachine that initialized the
#       state
#   transitions: this is a mapping of transition identifiers to other
#       states' unique identifiers
#   enter: this is a mapping of transition identifiers to method handles
#   leave: this is a mapping of transition identifiers to method handles
#   curr_trans: this contains the current transition. This is used
#       returned via State.transition(), which is used by the StateMachine
#
# Methods:
#   __init__(self, name)
#   transition(self)
#   listTransitions(self)
#   get_state(self, transition)
#   enter_state(self, transition)
#   default_entry(self)
#   leave_state(self, transition)
#   default_leave(self)
#   is_end(self)
class State(object):
  
    ## Constructor
    # @ param self - The object pointer
    # @ param name - Unique State identifier
    # @ param machine - Reference to the containing StateMachine
    def __init__(self, machine, name = None):

        super(State, self).__init__()
        self.name = name
        self.machine = machine
        self.transitions = {} # dictionary of transition -> state IDs

        # dictionary of transition -> method, for entry
        # this mapping is user defined, unique to each State
        self.enter = {} 

        # dictionary of transition -> method, for exit
        # this mapping is mser defined, unique to each State
        self.leave = {} 
        self.currTrans = "NO_TRANS"

    ## transition
    # @ param self The object pointer
    #
    # 
    def getTransition(self):
        return self.currTrans

    ##
    #
    #def listTransitions(self):
    #    return 

    ## getState
    # @ param self The object pointer
    #
    def getState(self, transition): 
        return self.transitions.get(transition, "END")

    ## enterState
    # @ param self The object pointer
    #
    def enterState(self, transition = None):
        return self.enter.get(transition, self.defaultEntry)

    ## defaultEntry
    # @ param self The object pointer
    #
    def defaultEntry(self):
        raise NotImplementedError("defaultEntry is not implemented.")

    ## leaveState
    # @ param self The object pointer
    #
    def leaveState(self, transition = None):
        self.currTrans = "NO_TRANS"
        return self.leave.get(transition, self.defaultLeave)

    ## defaultLeave
    # @ param self The object pointer
    #
    def defaultLeave(self):
        pass

    ## isEnd
    #
    #
    def isEnd(self):
        return False
        
## Class End
#
#
class End(State):

    ## Constructor
    #
    def __init__(self, machine, name = "END"):
        super(End, self).__init__(machine, name)

    ## transition
    #
    def transition(self):
        return self.currTrans

    ## defaultEntry
    #
    def defaultEntry(self):
        pass

    ## isEnd
    #
    def isEnd(self):
        return True
    
        



 





    
