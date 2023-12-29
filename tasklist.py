from task import Task


class Tasklist:

  def __init__(self):
    """
    @param: none
    @return: none
    Read in the list of tasks from the file and store them
    in the tasklist by opening the file, reading in each 
    line that consists of the task description, due date, 
    and time separated by commas, then construct the Task 
    object and appending it to the list, then sort the list
    """
    self.task_object = []
    file = open('tasklist.txt', 'r')
    for line in file:
      line = line.strip()
      desc, date, time = line.split(",")
      self.task_object.append(Task(desc, date, time))
    self.task_object.sort()

  def add_task(self, desc, date, time):
    """
    @param desc: description of the task
    @param date: the due date of the task
    @param time: the due time of the task
    function constructs a new task using the parameters, 
    appends it to the tasklist, and then sorts the list
    @return: none
    """
    new_task = Task(desc, date, time)
    self.task_object.append(new_task)
    self.task_object.sort()

  def mark_complete(self):
    """
    @param: none
    @return: none
    remove the current task from the tasklist."""
    self.task_object.pop(0)

  def save_file(self):
    """
    @param: none
    @return: none
    write the contents of the tasklist back to the file using the Task’s 
    __repr__ method (description, date, and time separated by commas).
    """
    with open('tasklist.txt', 'w') as file:
      for tasks in self.task_object:
        file.write(repr(tasks))

  def __getitem__(self, index):
    """
    @param index: the index of the item to get the item
    @return: the Task from the list at the specified index.
    """
    return self.task_object[index]

  def __len__(self):
    """
    @param: none
    @return: the number of items in the tasklist
    """
    return len(self.task_object)
