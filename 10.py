# Dasturga foydalanuvchi malumit kiritishi taminlandi 
word = input ("Biror bir matn kiritining ")
max_word = word.split()
max_words = max_word[0]


for i in max_word:
    if len(i) > len(max_words):
        max_words = i
print("Siz kiritgan matn ichida eng uzun so'z = ")
print(max_words)