import random
values = ["1", "2", "3", "5", "8", "13", "21"]
estimates_list = []
num_tickets = int(input("How many tickets do you need story points for?\n"))
for i in range (num_tickets):
    estimates_list.append(random.choice(values))
print(f"Your Story Point Estimates Are: {estimates_list}")
