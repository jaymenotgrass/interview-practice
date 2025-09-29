"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for product in product_ids:
        if product in seen:
            return True
        seen.add(product)
    return False

#Since we are looking at unique values, we want to use a set to prevent any chance of a duplicate number being added.
#We want to iterate through each number from the input given, and check the set if the number is there. 
#If the current product matches a value in the set "seen", then it returns True because a duplicate has been found.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
#A list is being created because that's what the assignment says to manage. Then to add a task,
#you must use the append method. And to remove the oldest task, I created an "if" statement
#checking if there were any values in the list, and if there are, then I used the pop method to remove the value 
#at the index value "0".

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)
#In this assignment I used the method of implementing a set. Since it automatically 
#is built to not have duplicates, there is nothing that needs to be done to filter out the
#duplicated numbers. The "unique" function just returns the length of the set because it should've automatically gotten rid of the duplicates.