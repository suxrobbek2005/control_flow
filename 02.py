# Dasturimizga foydalanuvchi tamonidan malumot kiritdi 
word = str(input("Biror bir malumot kiritining "))
count = 0

# Kiritilgan malumotdagi so'zlar hisoblandi
for i in word.split():
    count += 1

# Dasturda bajarilgan amallar terminalga chiqarildi
print ("Siz kiritgan matndai so'zlar soni = ")
print(count)