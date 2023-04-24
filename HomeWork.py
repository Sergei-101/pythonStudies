enter_revenue = int(input('Введите выручку фирмы '))
enter_costs = int(input('Введите издержки фирмы '))
if enter_revenue>enter_costs:
    employees = int(input('Введите численность сотрудников'))
    fin_resylt = enter_revenue-enter_costs
    rent = fin_resylt/enter_revenue
    profit_emp = fin_resylt/employees
    print(f'Фирма отработала с прибылью = {fin_resylt}. Рентабильность выручки = {rent}, прибыль фирмы в расчете на одного сотрудника {profit_emp}')
else:
    print("Фирма отработала в убыток")