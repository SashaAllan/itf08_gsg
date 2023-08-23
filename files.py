with open("sasha.txt","w") as files:

 name=input("Enter student name :  ")
 age=input("Enter student age :  ")
 date_birth=input("Enter student date_birth :  ")
 files.writelines(name+"\n")
 files.writelines(age+"\n" )
 files.writelines(date_birth )
 files.close()
 data={"name ":name ,"age ":age,'date_birth':date_birth}
 print(data)




