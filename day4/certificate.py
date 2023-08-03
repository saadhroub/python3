# 4 students, each one did 3 exams,
# we need to know the first student

def average(g1,g2,g3):
    sum = g1+g2+g3
    avg = sum/3
    return int(avg)

def top_one(s1,s2,s3,s4,s5):
    top_avg = max(s1,s2,s3,s4,s5)
    return top_avg

def reward_calculator(top_avg):
    if top_avg>=99:
        reward = 5000
    elif top_avg>=98:
        reward = 3000
    elif top_avg>=95:
        reward = 1000
    else:
        reward = top_avg*10
    return reward
        
s1_avg = average(57,78,91)
s2_avg = average(85,85,98)
s3_avg = average(87,79,91)
s4_avg = average(71,88,61)
s5_avg = average(77,92,61)

top = top_one(s1_avg, s2_avg, s3_avg, s4_avg, s5_avg)
reward = reward_calculator(top)
print("The best student in this class got: ", top)
print("He gots reward: ", reward, "USD")





