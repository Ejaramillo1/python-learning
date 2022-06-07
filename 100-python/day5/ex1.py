# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

    index = 0
    student_count = 0
for i in range(len(student_heights)):
    student_count += 1
    index += student_heights[i]
print(index/student_count)
