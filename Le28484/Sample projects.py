Scores = [[98, 68, 65, 73, 67],
          [77, 77, 88, 78, 90],
          [54, 65, 74, 85, 72],
          [77, 77, 68, 78, 91],
          [88, 86, 90, 56, 81]]
TCOUNTER = 1

for student in range(4):
    print(student+1, "student")
    for exam in range(5):
        X = 1
        counter = 0
        X = Scores[student][exam]
        while X>0:
            if X % 10 == 8:
                counter += 1
                TCOUNTER += 1
                X = X//10
            print("----", "The grade of exam", exam+1), "has", counter, "eight(s)"

print("a total of", TCOUNTER, "eights appear in all grades")



























#for student in range(5):
    #print(student +1, "student")
    #for exam in range(5):
           # if Scores[student][exam] % 10 == 5:
               # print("----", "exam", exam+1, Scores[student][exam])
                
       




