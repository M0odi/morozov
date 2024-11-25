# Пицца – любимое лакомство Васи, он постоянно покупает и с 
# удовольствием употребляет различные сорта этого великолепного блюда. 
# Однажды, в очередной раз, разрезая круглую пиццу на несколько частей, 
# Вася задумался: на какое максимальное количество частей можно разрезать 
# пиццу за N прямых разрезов? Помогите Васе решить эту задачу, определив 
# максимальное число не обязательно равных кусков, которые может получить 
# Вася, разрезая пиццу таким образом. На вход программе подаётся 
# натуральное число N – число прямых разрезов пиццы (N ≤ 1000). Программа 
# должна вывести одно число – ответ на задачу. 

def execution(amountLines:int):
    return (amountLines**2 + amountLines + 2) / 2