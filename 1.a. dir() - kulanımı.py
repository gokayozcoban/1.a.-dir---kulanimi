
# Data Types - Strings - Metodlar

# Genelde kullanılan metodlar a.b.c.d. vs. diye sıraladıklarım metodlar ama
# her hangi bir yapının metodlarına ulaşmak için dir() fonksiyonunu kullanabi-
# lirim:
print(dir(str))
print(dir(list))
print(dir(tuple))
print(dir(dict))

# Yukarıdaki kodlar string, listler, demetler ve sözlüğün metodlarını çıktı
# olarak verir.
# Aynı zamanda bu dir() fonksiyonun içeriğini de istediğim şekilde değiştire-
# bilir ve içinden index alabilirim:
metodlar = dir(tuple)
print("Tuple Metodları: ",metodlar[0])
Tuple Metodları:  __add__

metodlar[0] = "gökay"
print("Tuple Metodları: ",metodlar[0])
Tuple Metodları:  gökay
