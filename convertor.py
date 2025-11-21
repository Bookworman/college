
def convert_usd_to_rub (amount_usd):

    """Конвертирует введенную сумму $ в руб
    args:
        amount_usd: float
    returns:
        float: сумма руб"""

    usd_to_rub = 95.50
    amount_rub = amount_usd * usd_to_rub
    return amount_rub

amount_usd = float(input("Введите кол-во $ "))
print(convert_usd_to_rub(amount_usd))
