par = dict()
with open("B:\\FEFU\\Progi\\conf", 'r') as file:
    for line in file:
        if line[0] not in ['#', ';', ' ']:
            key, *value = line.rstrip("\n").split(" ")
            par[key] = value 
            
print(">>Параметры:")
for key in par:
    print(key)

flag = True
while flag:
    param = input(">>Введите параметр: ")
    print(">>Значение параметра: ", par.get(param))
    
    for i in range(2):
        command = input("Выйти из программы?(Yes/No)")
        if command == 'Yes':
            flag = False
            break
        elif command == 'No':
            flag = True
            break
        if i == 1:
            print(">>Неверная команда была введена слишком много раз\n>>Завершение работы.")
            flag = False
        print(">>Введена неверная команда!")
print(">>Выход")
            
