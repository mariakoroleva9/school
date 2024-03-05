class Studentik:
    pass


students=[]
f=open('students.csv')
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
for i in students:
    s=0
    k=0
    if i.score=='None':
        for j in students:
            if j.clas==i.clas and j.score!='None':
                k+=1
                s+=int(j.score)
        i.score=f'{s/k:.3f}'

for i in range(len(students)):
    if 'Хадаров Владимир Валерьевич' == students[i].fio:
        print('Ты получил:', students[i].score, 'за проект -', students[i].id)

f=open('students_new.csv','w')
print(name,file=f)
for i in students:
    print(i.id,',',i.fio,',',i.title,',',i.clas,',',i.score)
f.close

