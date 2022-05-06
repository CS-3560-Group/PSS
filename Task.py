'''
Task class holds attributes for the three
different Task Types: Recurring, Transient, Anti
'''


class Task:
    '''
    @param name, user selected string
    @param type, string from defined list (reference lecture 15 page 7)
    @param startTime, float of 24 hour clock rounded to nearest 15 minutes
    @param duration, float of number of hours rounded to nearest 15 minutes
    @param date, integer in the form YYYYMMDD
    @param endDate, integer in the form YYYYMMDD
    @param freq, integer represents 1(daily), 7(weekly)
    @param taskType, integer with Transient(1), Recurring(2), Anti(3)
    '''

    def __init__(self, name, type, taskType, startTime, duration, date, endDate, freq):
        # add checks for valid duration, dates, type, and overlap
        self.name = name
        self.type = type
        self.startTime = startTime
        self.duration = duration
        self.date = date
        self.endDate = endDate
        self.freq = freq
        self.taskType = taskType




    #Function to convert Task object to string
    def __str__(self):
        frequent = "daily" if self.freq == 1 else "weekly"
        if self.taskType != 2:
            return ('\nTask: ' + self.name + ' is a ' + self.type + ' task'+
                '\n\tIt starts at ' + str(int(float(self.startTime))) + ':' + str(int(((float(self.startTime)*60)%60))) +
                ' on ' + str(int(int(self.date)/10000)) + '/' + str(int((int(self.date) % 10000) / 100)) + '/'
                + str((int(self.date) % 100)))
        else:
            return ('\nTask: ' + self.name + ' is a ' + self.type + ' task'+
                    '\n\tIt starts at ' + str(int(float(self.startTime))) + ':' + str(int(((float(self.startTime)*60)%60))) +
                    ' on ' + str(int(int(self.date)/10000)) + '/' + str(int((int(self.date) % 10000) / 100)) + '/'
                    + str((int(self.date) % 100)) + ' and runs ' + frequent +
                    '\n\tIt ends on ' + str(int(int(self.endDate) / 10000)) + '/'
                   + str(int((int(self.endDate) % 10000) / 100)) + '/' + str((int(self.endDate)) % 100))


    #Getters
    def getName(self):
        return self.name

    def getType(self):
       return self.type


    def getStartTime(self):
      return self.startTime


    def getDuration(self):
      return self.duration


    def getDate(self):
      return self.date


    def getEndDate(self):
      return self.endDate


    def getFrequency(self):
      return self.freq

    def getTaskType(self):
      return self.taskType


    #Setters
    def setName(self, name):
        self.name = name

    def setType(self, taskType):
       self.type = taskType


    def setStartTime(self, startTime):
      self.startTime = startTime


    def setDuration(self, duration):
      self.duration = duration


    def setDate(self, date):
      self.date = date


    def setEndDate(self, endDate):
      self.endDate = endDate


    def setFrequency(self, freq):
      self.freq = freq

    def setTaskType(self, taskType):
      self.taskType = taskType
