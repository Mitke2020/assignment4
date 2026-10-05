# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

#2. Running Total with Reset
#Track a running total of values. If a negative number is added, reset the total to 0.

#Input: [5, 7, -1, 3, 2]
#Output: [5, 12, 0, 3, 5]

input_list=[]


def track(input_list):
    output=[]
    score=0
    for num in input_list:
        if num>-1:
             
             output.append(score+num)
             score+=num
        else:
            output.append(0)
            score=0
    return output

print(track([5, 7, -1, 3, 2]))  # Expected: [5, 12, 0, 3, 5]
print(track([]))                 # Expected: []
print(track([0]))                # Expected: [0]
print(track([-5, -1]))           # Expected: [0, 0]
print(track([4, -2, -3, 6]))     # Expected: [4, 0, 0, 6]


#I chose a list for the running total problem because the order of the numbers matters, and I need to return a result for every number in that same order. I used a second list to store the results and a variable called score to keep track of the total. When a number is zero or positive, I add it to score and save the updated total. When a number is negative, I reset score to zero and add zero to the output list. This approach goes through the input once, so its runtime is O(n).

#The time limit encouraged me to use familiar tools instead of creating a more complicated solution.
# A list and a for loop were enough for the task, so I did not need a custom class or linked nodes. 
# One mistake I noticed was that adding score and the number inside append did not actually update score. Separating the update from appending the result made the logic clearer.

#One trade-off was focusing on the calculation before adding detailed input validation. 
# My solution assumes the list contains numbers, so a string such as "hello" would cause an error. 
# A stronger version could check the values and give a clear message when an unsupported type appears. 
# I also used extra space for the output list, but that lets me keep every intermediate total without changing the original input. 
# Under time pressure, I prioritized a simple solution that was easy to understand and check.