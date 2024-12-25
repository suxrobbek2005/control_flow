# Dastimizga foydalanuchi taminadan malumot kiritsh taminlandi 
number = int (input ("Biror bir raqam kiritining = "))
print("Siz kiritgan songacha bulgan juft sonlar qatori \n")

# Dasturizga kiritilgan songacha bulagan sonlarni for loopida aylatirib oldik
for i in range(0, number):
    if int(i% 2 == 0):
        print(i)

