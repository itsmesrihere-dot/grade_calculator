math = int(input("enter math marks:"))
eng = int(input("enter eng marks:"))
ds = int(input("enter ds marks:"))
average = math+eng+ds/3
print(average)
if average >=90:
    print("grade : A")
elif avegrage >=80 & average<90:
    print("grade :B")
elif average >=70 & average<80:
    print("grade:C")
else:
    print("grade: D")

          

