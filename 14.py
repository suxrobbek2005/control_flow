# Dasturimizga foydalanuchi tamonidan malumot kiritilishi so'raldi
number = int (input("Birorta son kiritining = "))

# Kiritilgan sonlarning bo'luvchilarini aniqladik
print("Siz kiritgan soning jami buluvchilari ")
for i in range(1, number):
    if number % i == 0:
        print(i)