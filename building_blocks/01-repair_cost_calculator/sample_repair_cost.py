from repair_cost import calculate_total, calculate_amount_to_be_paid
deposit_amount = 200
# List to save price of items
items = []
# Loop until user enters a value <= 0
while True:
    price = int(input('Enter value less than or equal to 0 to exit\nEnter price of the item: '))
    if price <= 0:
        break
    items.append(price)

total_price = calculate_total(items)
pending_payment = calculate_amount_to_be_paid(total_price, deposit_amount)
print(f"Net Amount Payable: {pending_payment}")