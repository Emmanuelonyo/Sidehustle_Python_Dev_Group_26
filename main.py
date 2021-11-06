def average(class_score,totalstudents):
    avrg = class_score/totalstudents
    return avrg

#grade function
def grade(name,avg,newscore):
    if newscore >= 60 and avg-5 < newscore :
        result = "Congratulation " + name +" You have Passed the exams"
        return result
    else:
        result = "Sorry " + name + " you Failed"
        return  result


students = 3
score = [70, 70, 73]

# get student details
print("please enter student name")
newstudent = str(input())

print("please enter student score")
newscore = int(input())

# calculate total scores
totalstudents = students + 1
class_score = sum(score) + newscore;
# calculate average

avg = average(class_score,totalstudents)

response = grade(newstudent,avg,newscore)

print(avg)
print(class_score)
print(response)
