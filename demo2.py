import csv

with open("student.txt","r") as file:
    for data in file:
     print(data)
    print(file.readlines())

    with open("student.txt","w") as file:
       file.write("BCA")


with open("student.txt","a") as file:
          file.write("\n niha")

# with open("student.csv",mode="w", newline="") as file:
#      writer=csv.writer(file)
#      writer.writerrows(data)
      

