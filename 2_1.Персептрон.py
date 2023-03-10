# Тут мы моделируем самую простую модель персептрона,которая будет идти через начало системы координат,
#  и разделять данные ,которые находятся во 2 и 4-й плоскости 
import numpy as np
import matplotlib.pyplot as plt

N = 5 # Берем по пять точек для первого и второго класса 

x1 = np.random.random(N) # Создаем по 5 разнодных числа от 0 до 1 
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] # Содаем 5(range(5)) рандомных чисел от 1 до 10 ,потом делим на 10 и добавляем x1
C1 = [x1, x2] # Создаем list of lists 

x1 = np.random.random(N) # Делаем тоже самое
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 # Тут мы меняем все на знак -,чтобы числа получились намного меньше + отрицательные числа 
# Также добавляем -0.1,чтобы точка была точно ниже нашей прямой  
C2 = [x1, x2] # Создаем array

f = [0, 1] # Создаем прямую под 45 градусов,проходящей через (0,0),(1,1)

w = np.array([-0.3, 0.3]) # Создаем веса,которые при делении должны выводить -1,чтобы потом получить угловой коэфициент(1)
for i in range(N):
    x = np.array([C2[0][i], C2[1][i]]) # Перебираем все числа в list of lists 
    y = np.dot(w, x) # Перемножаем все числа с весовыми коэфициентами 
    print(y)
    if y >= 0:
        print("Класс C1")
    else:
        print("Класс C2")

plt.scatter(C1[0][:], C1[1][:], s=10, c='red') 
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()
