n = int(input())
List = []
for i in range(n):
    List.append(list(map(int,input().split())))

for i in range(n):
    grade = 1
    for j in range(n):
        if i==j:
            continue
        elif List[i][0] < List[j][0] and List[i][1] < List[j][1]:
            grade += 1
        
    print(grade, end= ' ')