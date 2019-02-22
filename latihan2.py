print("==============================latihan2 =============================")
print("menampilkan bilangan,berhenti ketika bilangan 0 dan menampilkan bilangan terbesar")


listl=[]
a=int (input("masukan angka"))
listl.append(a)
while (a != 0 ):
    a=int(input("masukan angka"))
    listl.append(a)
print(listl)
print ("Bilangan terbesar adalah = ",max(listl))