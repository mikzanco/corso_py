# CICLI WHILE

# x = ["milano", "veneiza", "roma"]
# print(x[0])
# print(x[1])
# print(x[2])

# i è un contatore
i = 0

while i < 6:
    print(i)
    i += 1
    
print("stop")

# break rompe il ciclo e lo blocca al momento scelto per l'if
i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("stop")

# continue serve per passare all'interazione successiva
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("stop")
