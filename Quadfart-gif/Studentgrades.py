grades = [[79, 75, 80, 81, 78, 82, 67, 92, 76, 77],
[72, 71, 69, 70, 64, 57, 81, 72, 73, 61],
[77, -1, 76, 87, 83, -1, -1, 89, 80, 78],
[68, 86, 84, -1, 78, 80, 82, 95, 76, 74],
[56, 64, 73, 69, 66, 69, 63, 71, 70, 84],
[74, 78, 60, 81, -1, 67, 76, -1, 65, 71],
[63, 54, -1, 74, 65, 59, 63, 65, 74, 61],
[73, 59, 75, 77, 68, 70, 81, 64, -1, 68],
[64, 67, -1, 74, 78, 70, 75, 85, 84, 90],
[74, -1, 88, 77, 87, 89, 81, 77, 80, 71],
[83, 74, 76, 73, 78, 69, 80, 76, 82, 84],
[79, 70, 75, 68, 68, 73, -1, 63, 68, 65],
[61, 72, 70, 72, -1, 69, 72, 69, -1, 76],
[74, 81, 70, 72, 81, 94, 79, -1, 68, -1],
[86, -1, 89, 78, -1, 88, 69, -1, 76, 78],
[74, 72, 74, 69, -1, 68, 82, 64, 71, 66],
[86, 76, 84, 79, 73, 79, 69, -1, 75, 77],
[82, 73, 70, 79, 76, 72, 81, 74, 81, 66],
[73, 72, 71, 75, 68, 64, 72, 77, 83, -1],
[-1, 74, 73, 71, 63, 79, 54, 63, 65, 67],
[74, 82, 84, 81, 73, 100, 64, 69, 87, 70],
[72, 70, 66, 76, 82, 72, 80, -1, -1, -1],
[75, 73, 65, -1, 75, 66, 70, 74, 75, -1],
[83, 73, 88, 95, 77, -1, 81, 90, 88, -1],
[77, 74, 83, 66, 76, 72, -1, 81, 73, 70],
[73, 84, 82, 84, 84, 74, 77, 86, 80, 83],
[78, 77, 80, 79, 86, 82, 76, 71, 81, 74],
[61, 72, 56, 71, 67, 69, 54, 69, 70, 62],
[77, 79, 82, 83, 72, 67, 71, 80, 76, 89],
[72, -1, 62, 66, 64, -1, 74, -1, 74, 68],
[88, 80, 85, 63, 68, 79, 83, 73, 77, 85],
[69, 83, 71, 69, 70, 76, 79, 73, 65, 77],
[70, 76, 68, 66, 75, 78, 83, 72, 66, 76],
[-1, 67, -1, 70, 62, 67, -1, 55, 63, -1],
[-1, -1, 85, 79, 77, 75, 88, 84, 93, 72],
[71, 67, 70, 83, 72, 83, -1, 80, 81, 71],
[62, 74, 69, 82, 61, 76, -1, -1, 65, 74],
[-1, 56, 72, 63, 61, 66, 63, -1, 67, 46],
[68, 91, 72, 75, 79, 77, 82, 84, 80, 81],
[76, 82, 75, 65, 62, 75, 67, 60, 60, 70],
[-1, 77, 72, 68, 78, 81, 73, 86, 74, 70],
[71, 70, -1, -1, 74, 67, 54, 71, 72, 64],
[63, 63, 73, 69, 59, 49, -1, 65, 60, -1],
[82, 88, 84, 79, 83, 96, 82, 90, 89, 84],
[75, 76, 77, 84, 84, 85, 67, 86, -1, 81],
[77, 87, 78, 82, 69, 69, 71, 89, 81, 77],
[78, 61, 78, 84, 72, -1, 66, 69, 70, 77],
[75, 57, 75, 61, 63, 74, 67, 78, 61, 67],
[66, 80, 80, 74, 76, -1, 80, 63, 64, 73],
[-1, -1, 70, 73, 74, 68, 75, 70, 66, 78],
[74, 72, 67, 72, 73, 69, 76, 76, 69, 60],
[88, -1, 73, -1, 70, 79, 72, 69, 80, 80],
[-1, 71, 80, 78, 81, 81, 67, 64, 78, 62],
[-1, -1, 69, 93, 82, -1, 77, 81, 82, 88],
[66, 64, 53, 70, 70, -1, 64, 71, 67, 52],
[76, 87, 83, 80, 68, 70, 72, 78, 75, 71],
[52, 66, 70, 69, 61, 65, 52, 72, 73, 68],
[82, 81, 71, -1, 70, 66, 73, 71, 80, 79],
[77, -1, 82, 78, 74, 76, 83, 75, 66, 75],
[68, 86, 86, 73, 67, 92, -1, 76, 73, 79],
[72, 83, 81, 66, 71, 84, 67, 79, 76, 63],
[72, 74, 83, 92, 76, 83, 87, 91, 86, 88],
[85, 70, 66, 61, 64, 66, 74, 53, 75, 67],
[73, 76, 70, 77, 81, 83, 70, 85, 68, 72],
[75, 85, 83, 94, 81, 66, 89, 81, 87, 88],
[76, 85, 85, 79, 89, 89, 68, 78, 85, 84],
[78, 87, 81, 84, -1, 66, 74, 85, 76, 73],
[86, 78, 92, 79, 87, 92, 78, 94, 78, 79],
[69, 74, 73, 67, -1, -1, 63, 61, 70, 78],
[71, 70, 65, 58, 73, 46, 64, 60, 72, -1],
[73, 81, 73, -1, 61, 66, -1, 58, 65, 58],
[92, 71, 77, 80, 75, 66, 85, 82, 82, 88],
[81, 73, 72, -1, 55, 70, 71, 62, 67, 68],
[78, -1, 69, 83, 73, -1, 71, 82, 77, 74],
[-1, 70, 80, 76, 74, 69, -1, 72, 71, 68],
[86, 80, 84, 71, 78, 61, 67, 64, 68, -1],
[63, 74, 62, 72, 68, 77, 81, 75, 60, -1],
[90, -1, 71, 71, 71, 81, 68, 71, 89, 82],
[79, 72, 84, -1, 89, 63, 74, 72, 70, 77],
[75, 52, 78, 65, 83, 69, 82, 59, 55, -1],
[66, 66, 70, 63, 71, 74, 67, -1, 72, 78],
[76, 79, 81, -1, 99, 78, 80, 90, 86, 85],
[67, 76, 63, 71, 68, 73, 73, 66, 61, 82],
[80, 82, 87, 70, 79, 67, 78, 72, 91, 77],
[67, 62, 76, 76, 75, 81, 71, 84, 71, 74],
[78, 74, 70, 73, 61, 67, 77, 66, -1, 91],
[54, 59, 72, 68, 78, 64, 81, 74, 74, 64],
[70, -1, 80, 75, -1, -1, 86, 71, 85, -1],
[77, -1, 72, 82, 70, 79, 83, 73, 56, 76],
[61, 67, 69, 63, 66, 67, 76, 67, 78, -1],
[76, 66, 80, 74, 71, 83, 71, 72, -1, 74],
[73, 62, 66, 59, 62, 63, -1, 50, 61, 68],
[78, 90, 79, 78, -1, 75, 83, 83, 90, 77],
[81, 73, 74, 75, 75, -1, 62, 68, 81, 77],
[83, 77, 86, 80, 73, 88, 75, 85, -1, 82],
[73, 77, 91, 86, 81, 76, 80, 81, 86, 71],
[-1, 80, 77, 85, 70, -1, 79, 88, 79, 86],
[-1, 99, 85, 71, 83, 84, 85, -1, 79, 92],
[63, 87, -1, 63, 74, 73, 86, 69, 66, 78],
[77, 66, 74, 65, 82, 87, 70, -1, 71, 76],]

students = [
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
    "Yuki Suzuki", "A", "B", "C", "D"]
# Iterate over each student
#Calculate max for each test
for j in range(10):
    MAX = grades[0][j]
    # set index=0 and max to first value in test j
    MAXINDEX = 0
    for i in range(100):
        # if test i j equals neg 1 ignore else check for max, and if max set index equal to i
        #tesT += 1
        #current_stu += 1
        # Calculate average, max, and min if there are valid grades
        if grades[i][j] == -1:
            continue
        elif grades[i][j] > MAX:
            MAX = grades[i][j]
            MAXINDEX = i
            # avg_grade = sum(students[i]) / len(students[i])
            # max_grade = max(students[i])
            # min_grade = min(students[i])
                # print the outputs by test and student
    print(f"Test#{j}:\n"f"The student with the maximum grade for test {j} was {(students[MAXINDEX])}, with {MAX}!")
    # print(f"The student with the minimum grade for test {tesT} was {(students[i])}, with {min_grade}.")
    # print(f"The average grade for test {tesT} is: {avg_grade:.2f}!")
    # print("The max grade for Test",j,"was",MAX)
    # print("The student who received this grade was", students[MAXINDEX])
