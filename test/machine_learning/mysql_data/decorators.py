class logit(object):
    ClassIsSetup = True
    _logfile = 'out.log'
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        # log_string = self.func.__name__ + " was called"
        # # Open the logfile and append
        # with open(self._logfile, 'a') as opened_file:
        #     # Now we log to the specified logfile
        #     opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()
        if self.ClassIsSetup:
            self.ClassIsSetup=False
        # return base func
            return self.func(*args, **kwargs)
    def notify(self):
        # logit only logs, no more
        pass