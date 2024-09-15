# great marking system
# total marks greater than equal to 80 than Great A+
# total marks greater than equal to 60 and less than 80 then Great B
# total marks greater than equal to 40 and less than 60 then Great C
# other wish Great F

total_marks = 45

if total_marks >= 80:
    print("A+")
elif total_marks >= 60 and total_marks < 80:
    print("B")
elif total_marks >= 40 and total_marks < 60:
    print("C")
else:
    print("F")