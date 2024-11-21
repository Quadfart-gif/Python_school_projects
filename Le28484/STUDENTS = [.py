from numpy.ma.core import minimum

STUDENTS = [
    "Afonso Cruz", "Ahmed Khan", "Aiden Chen", "Alexey Petrov", "André Ferreira",
    "Ana Oliveira", "Anika Singh", "Arjun Patel", "Beatriz Cardoso", "Benjamin Thompson",
    "Bianca Moreira", "Bruno Figueiredo", "Camille Dubois", "Carolina Esteves", "Carlos Silva",
    "Catarina Nunes", "Chiara Bianchi", "Daniel Simões", "Daniela Rosetti", "David Fischer",
    "Diogo Moreira", "Diana Neves", "Emma Davis", "Emma Lunde", "Emily Thompson",
    "Eva Ramos", "Felipe Rodrigues", "Filipe Ribeiro", "Francisco Mendes", "Gabriel Almeida",
    "Hana Nguyen", "Hassan Abdel", "Helena Castro", "Hugo Pires", "Inês Santos",
    "Isabel Duarte", "Isabella Martínez", "Ivan Novak", "Ivy Wilson", "Joaquín López",
    "Joana Correia", "João Martins", "Jorge Cruz", "Julian Kim", "Leonardo Varela",
    "Leonor Almeida", "Liam Johnson", "Lila Rahman", "Linda Novak", "Lara Monteiro",
    "Lucas Fisher", "Lucas Kim", "Lucas Leclerc", "Lucas Morales", "Luana Ramos",
    "Luis Coelho", "Manuel Mendes", "Marcus Müller", "Maria Gonçalves", "Maria Ivanova",
    "Maria Martínez", "Marta Sousa", "Mariana Antunes", "Maximilian Schneider", "Matilde Teixeira",
    "Mei Chen", "Miguel Costa", "Maya Larsen", "Miguel Costa", "Miguel Costa",
    "Nikita Kuznetsov", "Nuno Lima", "Oliver Evans", "Olivia Green", "Oscar Andersen",
    "Patricia Barreto", "Paula Martins", "Pedro Matos", "Rafael Carvalho", "Ravi Desai",
    "Ricardo Rocha", "Rita Fernandes", "Ryo Tanaka", "Santiago Torres", "Sara Gomes",
    "Sara Peterson", "Sara Popov", "Sara Svensson", "Sofia Ribeiro", "Sophia Zhang",
    "Sophie Baker", "Tiago Pereira", "Tomás Baptista", "Vasco Lopes", "William Turner",
    "Yuki Suzuki"
]

GRADES = [
    [94, 68, 69, 73, 75, 78, 85, 86, 87, 69],
    [89, 87, 87, 63, 92, -1, 96, 89, 93, 89],
    [72, 84, 99, 100, 83, 81, 90, -1, 87, 95],
    [82, 82, -1, 69, 78, 85, 87, 84, 72, 93],
    [84, 78, 100, 79, 90, 91, 74, 83, 83, 100],
    [67, 77, 92, 84, 80, 60, 73, 91, 86, 70],
    [66, 63, 36, -1, 70, 41, 70, -1, 30, 45],
    [49, 72, 39, 35, 51, 47, -1, 48, 50, 62],
    [-1, 54, 56, 57, 50, 61, 47, 44, 53, -1],
    [71, 56, 54, -1, 82, 81, 70, 61, 65, 74],
    [59, 51, 51, 61, 63, 77, 64, 44, 54, -1],
    [84, 83, -1, 87, 97, 74, 91, 100, 87, 64],
    [71, 88, 74, 77, 79, 100, 94, 85, 69, 86],
    [100, 60, -1, 73, 89, 76, 60, 78, 59, 69],
    [81, 62, 71, -1, 65, 66, 57, 79, 78, 70],
    [92, 77, 80, 89, 79, 91, 68, 77, 91, 73],
    [70, 86, 77, 86, 81, 92, 88, 80, 63, -1],
    [76, 72, 64, 81, 86, 83, 71, 74, 90, -1],
    [-1, 33, 63, 36, 70, 71, 57, 55, 52, 58],
    [68, 73, 92, 79, -1, 65, 100, 94, 74, 66],
    [67, 61, 86, -1, 85, 100, 82, 86, 70, 76],
    [52, 53, 47, -1, 64, 58, 48, -1, 43, 57],
    [80, 91, -1, 67, 68, 64, 73, 89, 85, 68],
    [56, 60, 63, 51, 61, -1, 64, 48, -1, 52],
    [62, 57, -1, 68, 54, -1, 63, 73, 76, 53],
    [59, 84, -1, 76, 76, -1, 85, 77, 73, 76],
    [55, 56, 88, 81, 71, 72, 67, 52, -1, 51],
    [31, 43, 67, -1, 35, 38, 65, 62, 40, 94],
    [96, 98, 64, 69, 62, 64, 75, 67, 84, 70],
    [88, 79, 83, 81, 89, 89, 82, 74, -1, 95],
    [-1, 85, 85, 90, 90, 88, 94, -1, 87, 77],
    [48, 66, 24, 66, 55, 43, 58, -1, 63, 48],
    [-1, 60, 68, 63, 78, 64, 37, 70, 72, 70],
    [66, -1, 73, 56, 61, 63, 62, 57, 71, 61],
    [-1, 86, 92, 85, 77, 74, 65, 87, -1, 87],
    [52, -1, 91, 61, 21, 52, 67, 57, 65, 46],
    [57, 83, 94, 65, 64, -1, 81, 76, 62, -1],
    [80, 71, 87, 69, 65, -1, 82, 69, 77, 64],
    [88, 75, 69, 81, -1, 81, 73, 58, 77, 85],
    [-1, 100, 68, 92, 72, 78, 75, 79, 84, 100],
    [74, 69, -1, 87, 80, 24, 67, 74, 76, 79],
    [64, 95, 87, 63, -1, 64, 60, 68, 92, 79],
    [27, 57, 68, 59, 66, 61, 63, 69, 61, -1],
    [69, 96, 79, -1, 78, 79, -1, -1, -1, 100],
    [76, 78, 71, 74, 76, 81, -1, 68, 77, 73],
    [73, 72, 87, -1, 76, 76, -1, 76, 60, 89],
    [90, 88, 74, 82, 84, 87, 71, 59, 81, 50],
    [76, -1, 64, 52, 57, 72, -1, 78, 81, 82],
    [35, 51, 52, -1, 58, 37, 75, 50, 64, 46],
    [82, 96, 80, 100, 81, -1, 87, -1, 96, 72],
    [47, 54, 73, -1, 57, 48, 84, 58, 45, 46],
    [84, -1, 85, 77, 95, 100, 91, -1, 89, 91],
    [68, -1, 42, 82, 87, 70, 68, 73, -1, 26],
    [100, 70, -1, 91, 77, 92, 88, 77, 93, 78],
    [63, 56, 85, -1, 73, 63, -1, -1, 59, 66],
    [59, 70, 51, 56, 54, 45, 28, -1, -1, 55],
    [76, 81, 78, 84, 79, 79, 72, 71, 68, 69],
    [87, 54, 65, 61, -1, 90, 72, -1, 47, 80],
    [70, 76, -1, 78, 85, -1, -1, 72, 75, 81],
    [66, 68, -1, 59, 63, 63, 49, -1, -1, 69],
    [-1, 89, 72, 99, 81, 77, 87, 92, 74, 75],
    [78, 69, 66, 66, -1, 62, 70, 46, 71, 59],
    [85, 91, 79, 85, 87, 76, 63, 79, 23, 72],
    [84, 60, 72, 92, -1, 83, 66, 84, 79, 88],
    [100, 74, -1, 80, 86, 75, 84, 85, 61, 85]
]

#number of assessments
num_assessments = len(GRADES[0])
#range of num assesments outputs 10
print(num_assessments)

#calculates the maximum
#we assume there is only one maximum value for each assessment
# max_value = GRADES[0][0]
# for row in GRADES:
#     for element in row:
#         if element > max_value:
#             max_value = element

# print("max value is:", max_value)


#calculates the minimum
#we assume there is only one minimum value for each assessment
# min_value = GRADES[63][0]
# for row in GRADES:
#     for element_2 in row:
#         if element_2 < min_value:
#             if element_2 == -1:
#                 continue
#             min_value = element_2
#print("minimum value is:", min_value)


#Calculate max for each test
for j in range(10):
    MAX = GRADES[0][j]
    MAXINDEX = 0
    for i in range(50):
        if GRADES[i][j] == -1:
            continue
        elif GRADES[i][j] > MAX:
            MAX = GRADES[i][j]
            MAXINDEX = i
    print("The max grade for Test",j,"was",MAX)
    print("The student who received this grade was",STUDENTS[MAXINDEX])

    #calculating minimum for each test
for j in range(10):  # Iterate through each test (column)
    MIN = float('inf')  # Start with a very high value
    MININDEX = 0  # To store the index of the student with the min grade
    for i in range(50):  # Iterate through each student (row)
        if GRADES[i][j] == -1:  # Skip if the grade is -1 (invalid data)
            continue
        elif GRADES[i][j] < MIN:  # If current grade is less than MIN
            MIN = GRADES[i][j]  # Update MIN
            MININDEX = i  # Update the index of the student
    print("The min grade for Test", j, "was", MIN)
    print("The student who received this grade was", STUDENTS[MININDEX])
      



        
    
        
    



