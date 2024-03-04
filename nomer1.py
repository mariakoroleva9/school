class Studentik:
    fio=''
    score=0
    clas=''
    id=0

students=[]
f=open('students.csv', encoding = 'utf8')
for i in range(501):
    students.append(Studentik())
    s = f.readline().split()
    students[i].fio=s[1]
    students[i].id=s[0]
    students[i].score = s[4]
    students[i].clas = s[3]

    if 'Хадаров Владимир' in students[i].fio:
        print('Ты получил:', students[i].score, 'за проект -', students[i].id)
