names = list(map(str, input().split()))
quantity = int(input())
expenses = {}
for i in range(len(names)):
    expenses[names[i]] = 0
for _ in range(quantity):
    name, money_spend = input().split()
    money_spend = int(money_spend)
    expenses[name] += money_spend


def average_value():
    total_sum = 0
    for name in expenses:
        total_sum += expenses[name]
    average = total_sum / len(names)
    return round(average, 2)
    

def distribution_cred_debt(average_val):
    creditors = []
    debtors = []
    for name in names:
        balance = expenses[name] - average_val
        if balance > 0:
            creditors.append((name, balance))
        elif balance < 0:
            debtors.append((name, -balance))
    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1], reverse=True)
    return creditors, debtors


def transactions_all(creditors, debtors):
    transactions = []
    i = j = 0
    while i < len(creditors) and j < len(debtors):
        creditor, credit_amount = creditors[i]
        debtor, debt_amount = debtors[j]

        transfer_amount = min(credit_amount, debt_amount)
        
        transactions.append((debtor, creditor, round(transfer_amount, 2)))
        creditors[i] = (creditor, credit_amount - transfer_amount)
        debtors[j] = (debtor, debt_amount - transfer_amount)
        if creditors[i][1] < 1e-9:
            i += 1
        if debtors[j][1] < 1e-9:
            j += 1
    return transactions


result = average_value()
creditors, debtors = distribution_cred_debt(result)
result = transactions_all(creditors, debtors)
print(len(result))
for debtor, creditor, amount in result:
    print(f"{debtor} {creditor} {amount:.2f}")
