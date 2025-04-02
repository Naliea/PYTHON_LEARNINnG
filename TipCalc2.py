print("Welcome to the Tip Calculator")
Total_Bill=float(input("What was the total bill?"))
Tip= int(input("How much tip would you like to give?10 12 0r 15?"))
Calculate_Tip = Tip /100
Split_Bill = int(input("How many people to split your bill:"))
Amount_to_pay = (Total_Bill+(Total_Bill * Calculate_Tip ))/ Split_Bill
Last_Amount = f"Each person should pay:{Amount_to_pay:.2f} "
print(Last_Amount)

