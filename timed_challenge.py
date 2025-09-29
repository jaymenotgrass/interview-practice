# Pick one question from timed_challenge.txt
# Paste the question as a comment below
##8. Already Seen
##Track a series of user IDs and return the number of new users.
##Input: [101, 102, 101, 103, 104, 102]
##Output: 3
# Set a timer for 30 minutes and complete the question!

class UserTracker:
    def __init__(self):
        self.seen = set()
        self.new_user_count = 0
    
    def add(self,user_id):
        if user_id not in self.seen:
            self.seen.add(user_id)
            self.new_user_count += 1
        

    def get_new_user_count(self):
        return self.new_user_count
    
#Edge 1
tracker = UserTracker()
inputs = [101, 102, 101, 103]
for user in inputs:
    tracker.add(user)
print("Output: ", tracker.get_new_user_count())

#Edge 2 - Empty List
tracker2 = UserTracker()
print("Output: ", tracker2.get_new_user_count())

#Edge 2 - Wrong Input
try:
    tracker3 = UserTracker()
    tracker3.add("not-an-int")
    print("Wrong type accepted:", tracker3.get_new_user_count())
except Exception as e:
    print("Caught error for wrong type:", e)

#Create a comment or separate .txt file that provides a brief reflection (200 to 300 words) that answers the following:
#What structure you chose and why
# - The question was very similar to what I have been working on all week and so
#   creating a class with certain functions to orchestrate the function of this problem
#   was the best way to go. This problem requires iterating through the input that is given
#   and not printing out the actual numbers, but the count of how many unique numbers there are.
#   Creating a set allows you to add the values to the set and check if the other inputs are found
#   within that set. If they are not found multiple times, then the "count" adds 1 everytime a new value is found.

#How the time limit shaped your decision
#  - I have never worked with a time limit especially that short of one. It challenged me to think quickly
#    and effectively. It also forced me to figure out a way that is the most simple.
#    It takes a lot more time if I am trying to make a lot of complex functions and statements,
#    so I tried to think of the simple ways to accomplish this goal. 

#What trade-offs or compromises you made under time pressure
#  - Like said prior, being under the pressure of the time limit, it forced me to do basic things with my code.
#    I was worried about the errors that might occur with certain inputs but I didn't have the time to either implement
#    or fully understand what inputs would run as needed. 

