#Used to store unused, but perhaps useful code    
    
    def generate_map(self):
        """generate_map
        looks at the list of modules the user provided and generates a mapping
        (a dict) of state_name -> state pairs.
        """
        modules = self.state_modules
        for module in modules:
            module_items = inspect.getmembers(module)
            for (memb_name, memb) in module_items:
                if inspect.isclass(memb) and \
                issubclass(memb, state.State) and \
                memb.__module__ == module.__name__:
                    temp = memb()
                    self.states[temp._name] = temp


class ManagementThread(threading.Thread):

    def __init__(self, thread_ID, function):
        super(ManagementThread, self).__init__()
        self.thread_ID = thread_ID
        self.function = function

    def run(self):
        self.function()
