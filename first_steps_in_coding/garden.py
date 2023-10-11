meters_needed = float(input())
price = meters_needed * 7.61
discount = price * 0.18
final_price = price - discount

print(f"The final price is: {final_price} lv." 
      f"The discount is: {discount} lv.")
