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
    '''

    def __init__(self, name, type, startTime, duration, date, endDate, freq):
        # add checks for valid duration, dates, type, and overlap
        self.name = name
        self.type = type
        self.startTime = startTime
        self.duration = duration
        self.date = date
        self.endDate = endDate
        self.freq = freq

    def __str__(self):
        return '\nTask: ' + self.name + ' starts at ' + str(self.startTime) + ' on ' + str(self.date)

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
