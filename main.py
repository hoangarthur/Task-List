"""
  Description: Create a program that maintains a task list for the user. 
  The user should be able to view the current task, list all of the tasks, 
  mark the current task complete, or to add a new task. 
  The program will read the list from a file (‘tasklist.txt’) when the program
  begins and then store the updated list by overwriting the old contents when 
  the user quits the program.
"""

import check_input
from tasklist import Tasklist


def get_date():
  """
  @param: none
  @return: the date in the format: MM/DD/YYYY.
  prompts the user to enter the year, month, and day. 
  Valid years are 2000-3000, valid months are 1-12, and valid days are 1-31.   
  If the inputted month or day is less than 10, then add a 0 to format it correctly
  """
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 3000)
  if (day < 10):
    day = "0" + str(day)
  if (month < 10):
    month = "0" + str(month)
  return f"{month}/{day}/{year}"


def get_time():
  """
  @param: none
  @return: the date in the format: HH:MM.
  prompts the user to enter the hour (military time) and minute.
  Valid hours are 0-23 and valid minutes are 0-59. If the inputted hour or minute
  is less than 10, then add a 0 to format it correctly
  """
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)
  if (hour < 10):
    hour = '0' + str(hour)
  if (minute < 10):
    minute = '0' + str(minute)
  return f"{hour}:{minute}"


def main_menu():
  """displays the main menu and returns the user’s valid input"""
  task_list = Tasklist()
  done = False
  while (not done):
    print(f"\n-Tasklist-\n Tasks to complete: {len(task_list)}"\
      "\n1. Display current task"\
      "\n2. Display all tasks"\
      "\n3. Mark current task complete"\
      "\n4. Add new task \n5. Save and quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 5)
    if (choice == 1):
      """ Display current task """
      print(f"Current task is: {task_list[0]}")
    elif (choice == 2):
      """ Display all tasks """
      print("Tasks: ")
      for task in task_list:
        print(task)
    elif (choice == 3):
      print(f"Marking current task as complete: {task_list[0]}")
      task_list.mark_complete()
      if (len(task_list) == 0):
        print("All tasks are completed")
        done = True
      else:
        print(f"New current task is: {task_list[0]}")
    elif (choice == 4):
      """ Add new task """
      task_list.add_task(input("Enter a task: "), get_date(), get_time())
    else:
      done = True

  task_list.save_file()


main_menu()
