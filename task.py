class Task:

  def __init__(self, desc, date, time):
    """
    @param desc: description of the task
    @param date: the due date of the task
    @param time: the due time of the task
    Assign self object to values
    @return: none
    """
    self.desc = desc
    self.date = date
    self.time = time

  def __str__(self):
    """
    @param: none
    @return: a string used to display the task’s information to the user 
    in the format Description - Due: date at time
    """
    return f"{self.desc} - Due: {self.date} at {self.time}"

  def __repr__(self):
    """
    @param: none
    @returns a string used to write the task to the file.
    """
    return f"{self.desc}, {self.date}, {self.time}\n"

  def __lt__(self, other):
    """
    @param other: other object to compare with self object
    @return: true if the self task is less than the other task. 
    Compare by year, then month, then day, then hour, then minute, 
    and then the task description by alphabetical order.
    """
    if self.date[-4:] != other.date[-4:]:
      return self.date[-4:] < other.date[-4:]
    if self.date[:2] != other.date[:2]:
      return self.date[:2] < other.date[:2]
    if self.date[3:5] != other.date[3:5]:
      return self.date[3:5] < other.date[3:5]
    if self.time[:2] != other.time[:2]:
      return self.time[:2] < other.time[:2]
    if self.time[3:] != other.time[3:]:
      return self.time[3:] < other.time[3:]
    return self.desc < other.desc
