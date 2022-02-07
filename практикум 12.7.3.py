per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму, которую вы намерены положить на депозит:"))
deposit_TKB = money * per_cent['ТКБ'] * 0.01
deposit_CKB = money * per_cent['СКБ'] * 0.01
deposit_VTB = money * per_cent['ВТБ'] * 0.01
deposit_SBER = money * per_cent['СБЕР'] * 0.01
deposit = [deposit_TKB, deposit_CKB, deposit_VTB, deposit_SBER]
print("deposit = ", deposit)
print("В банке ТКБ ваша приыбль за один год составит: ", deposit_TKB)
print("В банке СКБ ваша приыбль за один год составит: ", deposit_CKB)
print("В банке ВТБ ваша приыбль за один год составит: ", deposit_VTB)
print("В банке СБЕР ваша приыбль за один год составит: ", deposit_SBER)

max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать: ", max_deposit)
