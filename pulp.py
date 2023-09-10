import pulp

# Создаём задачу линейного программирования
problem = pulp.LpProblem("Load_Placement", pulp.LpMinimize)

# Определяем переменные решения (например, размещение груза)
x1 = pulp.LpVariable("Load1", lowBound=0)
x2 = pulp.LpVariable("Load2", lowBound=0)

# Определяем целевую функцию (например, минимизировать транспортные расходы).
problem += 2 * x1 + 3 * x2  # Корректируем коэффициенты в зависимости от вашей цели

# Определяем ограничения (например, ограничения по весу)
problem += x1 + x2 <= 10  # Ограничение по общему весу

# Решаем задачу оптимизации
problem.solve()

# Выводим результаты
if problem.status == pulp.LpStatusOptimal:
    print("Оптимальное решение найдено:")
    print(f"Груз 1: {x1.varValue}")
    print(f"груз 2: {x2.varValue}")
else:
    print("Оптимального решения не найдено.")