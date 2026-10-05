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
    x=len(product_ids)
    y=len(set(product_ids))
    if x==y:
        return False
    else:
        return True
    
# A set fits this task because it stores only unique product IDs. Creating a set takes O(n) average time, while comparing the length with the original list takes O(1), which gives us 0(N) time overall.

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

class Node:
    def __init__(self):
        self.value=None
        self.next=None

class TaskQueue:
    def __init__(self):
        self.front=None
        self.rear=None

    def add_task(self, task):
        new_node=Node(task)
        if not self.front:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
            
            
    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node=self.front
        self.front=self.front.next
        return removed_node.value

# A queue fits this task as we are dealing with the FIFO structure. The order is important, and also the tasks that are added prior have the priority. It would be resolved in O(1) time.


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
        self.values=set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

#I have chosen to use the set for this problem, as we are dealing with the number of the unique elements, so set will automatically reject the duplicate and we can return the number of unique values by
# accessing the length of the set implicitly