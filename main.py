# #1-misol
# def teskari(royxat):
#     return royxat[::-1]

# royxat = input("Elementlarni kiriting (bo‘sh joy bilan): ").split()
# print("Teskari:", teskari(royxat))
# #2-misol
# def kalkulyator(a, b, amal):
#     if amal == '+':
#         return a + b
#     elif amal == '-':
#         return a - b
#     elif amal == '*':
#         return a * b
#     elif amal == '/':
#         return a / b
#     else:
#         return "Noto‘g‘ri amal!"

# a = float(input("Birinchi son: "))
# b = float(input("Ikkinchi son: "))
# amal = input("Amal kiriting (+, -, *, /): ")
# print("Natija:", kalkulyator(a, b, amal))
# #3-misol
# def sozlar_soni(s):
#     return len(s.split())

# matn = input("Matn kiriting: ")
# print("So‘zlar soni:", sozlar_soni(matn))
# #4-misol
# def juft_ikkilantir(royxat):
#     return [x*2 for x in royxat if x % 2 == 0]

# sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
# print("Juft sonlar 2 barobari:", juft_ikkilantir(sonlar))
# #5-misol
# def kalitlar_royxati(lugat):
#     return list(lugat.keys())

# lugat = {}
# n = int(input("Nechta element kiritasiz? "))
# for i in range(n):
#     k = input(f"{i+1}-kalit: ")
#     v = input(f"{i+1}-qiymat: ")
#     lugat[k] = v

# print("Kalitlar ro‘yxati:", kalitlar_royxati(lugat))
