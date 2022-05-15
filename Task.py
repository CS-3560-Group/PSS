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
    @param startDate, integer in the form YYYYMMDD
    @param endDate, integer in the form YYYYMMDD
    @param freq, integer represents 1(daily), 7(weekly)
    @param taskType, integer with Transient(1), Recurring(2), Anti(3)
    '''

    def __init__(self, name, type, taskType, startTime, duration, startDate, endDate, freq):
        # add checks for valid duration, dates, type, and overlap
        self.name = name
        self.type = type
        self.startTime = startTime
        self.duration = duration
        self.startDate = startDate
        self.endDate = endDate
        self.freq = freq
        self.taskType = taskType




    #Function to convert Task object to string
    def __str__(self):
        frequent = "daily" if self.freq == 1 else "weekly"
        if self.taskType != 2:
            return ('\nTask: {name} is a {task}\n\t  It starts at {hour:02d}:{minute:02d} on {year}/{month:02d}/{day:02d}\n\t  It runs for {duration} hours'.format(name=self.name, task=self.type,
                    hour=int(float(self.startTime)), minute=int(((float(self.startTime) * 60) % 60)),
                    year=int(int(self.startDate) / 10000), month=int((int(self.startDate) % 10000) / 100),
                    day=(int(self.startDate) % 100), duration = self.duration))
        else:
            return ('\nTask: {name} is a {task}\n\t  It starts at {hour:02d}:{minute:02d} on {year}/{month:02d}/{day:02d} and runs '
                    '{frequency}\n\t  It ends on {eyear}/{emonth:02d}/{eday:02d}\n\t  It runs for {duration} hours'.format(name = self.name, task = self.type,
                     hour = int(float(self.startTime)), minute = int(((float(self.startTime)*60)%60)),
                     year = int(int(self.startDate)/10000), month = int((int(self.startDate) % 10000) / 100),
                     day = (int(self.startDate) % 100), frequency = frequent, eyear = int(int(self.endDate) / 10000),
                     emonth = int((int(self.endDate) % 10000) / 100), eday = (int(self.endDate)) % 100, duration = self.duration))


    #Getters
    def getName(self):
        return self.name

    def getType(self):
       return self.type


    def getStartTime(self):
      return self.startTime


    def getDuration(self):
      return self.duration


    def getStartDate(self):
      return self.startDate


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


    def setStartDate(self, startDate):
      self.startDate = startDate


    def setEndDate(self, endDate):
      self.endDate = endDate


    def setFrequency(self, freq):
      self.freq = freq

    def setTaskType(self, taskType):
      self.taskType = taskType
