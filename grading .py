print("Enter score: ")
workscores = int(input('ใส่คะแนนเก็บ :'))
midtermScores = int(input('ใส่คะแนนกลางภาค :'))
finalscores = int(input('ใส่คะแนนปลายภาค :'))


tot = workscores+midtermScores+finalscores


if tot >=80 :
    print("Your Grade is A1")
elif tot >=75 :
    print("Your Grade is A2")
elif tot>=70 :
    print("Your Grade is B1")
elif tot>=65 :
    print("Your Grade is B2")
elif tot>=60 :
    print("Your Grade is C1")
elif tot>=55 :
    print("Your Grade is C2")
elif tot>=50 :
    print("Your Grade is D")

else:
    print("F")

