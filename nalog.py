income = float(input("Введите ваш доход: "))
tax = 0.13
tax_summ = income * tax
income_after_tax = income - tax_summ

print(f"""Общий доход: {f"{round(income, 2):,}".replace(',', ' ')} руб.
Сумма налога {f"{round(tax_summ, 2):,}".replace(",", " ")} руб.
Чистый доход {f"{round(income_after_tax, 2):,}".replace(",", " ")} руб.""")