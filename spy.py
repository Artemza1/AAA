alphabet_rus=[
"А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М","Н","О","П",
"Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"
]

# alphabet_eng=[
# "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
# "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
# ]

# print()
def matrix(n):
    with open ("csvvti.csv", "w", encoding="utf8") as file:
        while n < 32:
            for i in alphabet_rus:
                if i == alphabet_rus[0]:
                    print(end="|")
                    file.write('|')
                print(i,end="|")
                file.write(i + '|')
            print()
            file.write("\n")

            alphabet_rus.append(alphabet_rus[0])

            alphabet_rus.remove(alphabet_rus[0])

            n += 1

matrix(0)
print("\n")



# def matrix1(n):
#     with open ("csvvti1.csv", "w") as file1:
#         while n < 26:
#             for i in alphabet_eng:
#                 if i == alphabet_eng[0]:
#                     print(end="|")
#                     file1.write('|')
#                 print(i,end="|")
#                 file1.write(i + '|')
#             print()
#             file1.write("\n")
#
#             alphabet_eng.append(alphabet_eng[0])
#
#             alphabet_eng.remove(alphabet_eng[0])
#
#             n += 1
# matrix1(0)
# print("\n")