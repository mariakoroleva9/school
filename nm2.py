class Studentik:
    fio=''
    score=0
    clas=''
    id=0

students=[]
f=open('students.csv', encoding = 'utf8')
for i in range(501):
    students.append(Studentik())
    s = f.readline().split(',')
    if s[4] == None:
        s[4] = -10
    students[i].id = s[0]
    students[i].fio = s[1]
    students[i].clas = s[3]
    students[i].score = s[4]

studentiki10=[]

for i in range(len(students)):
    if students[i].clas[:-1]=='10':
        studentiki10.append(students[i])

for i in range(len(studentiki10)):
    t=studentiki10[i]
    j=i-1
    while j>=0 and t.score > studentiki10[j].score:
        studentiki10[j+1]=studentiki10[j]
        j-=1
    studentiki10[j+1]=t

print('10 класс:')
for i in range(3):
    print(i+1, 'место:', studentiki10[i].fio)