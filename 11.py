# Dasturga foydalanuvchi tamonidan malumot kiritilishi taminlandi 
word = input("Biror bir so'z kiritining ")

# Kiritilgan so'z polindirom ekanligi tekshirildi
text_1 = word[::-1]
text_2 = word[0:]
if text_1 == text_2:
    print ("Siz kiritgan so'z palindirom ")
else :
    print ("Siz kiritgan so'z palindrom emas ")



