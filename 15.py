# Dasturga foydalanuvchi tamonidan kirtitilishi taminlandi
number = int (input ("Nechta son kiritasiz  = "))
i = 1
# Foydalanuvchi kiritgan songacha toq va 3 ga bulinadiganlari choq etildi
print ("Siz kiritgan sonlar toq va 3 ga bulinadiganlari \n")
for i in range(number) :
    if i % 2 == 1:
        print (i)
    elif number % 3 == 0:
        print (i)

