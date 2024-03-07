class Studentik:
    fio = ''
    score = 0
    clas = ''
    id = 0
    title = 0

students=[]
f=open('students.csv',encoding='utf-8')
name = f.readline().split()
j=0
for i in f:
    s = i.strip().split(',')
    students.append(Studentik())
    students[j].id = s[0]
    students[j].fio = s[1]
    students[j].title = s[2]
    students[j].clas = s[3]
    students[j].score = s[4]
    j+=1

n=len(students)
for i in range(1,n):
    t=students[i]
    j=i-1
    if t.score!='None' and students[j].score!='None':
        while j>=0 and int(t.score)<int(students[j].score):
            students[j+1]=students[j]
            j-=1
            while students[j].score=='None':
                j-=1
    students[j+1]=t
k=1
print('10 класс')
for i in range(len(students)):
    if '10' in students[i].clas and k<=3:
        print(f'{k} место: {students[i].fio} ')
        k+=1
