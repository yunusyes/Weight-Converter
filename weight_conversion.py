def main():
    while True:
        try:
            weight = float(input("Enter your weight: "))
            break
        except ValueError:
            print("You didn't enter your weight correctly, try again")
            weight = None
            
    kgs_lbs = input("Kilograms or Pounds? (K or L): ")
    converted_weight = weight_conversion(weight, kgs_lbs)
    
    if kgs_lbs == "K":
        print(f"Your weight is {converted_weight} lbs.")
    elif kgs_lbs == "L":
        print(f"Your weight is {converted_weight} kgs.")
       
def weight_conversion(weight, kgs_lbs):
    if kgs_lbs == "K":
        converted_weight = weight*2.205
    elif kgs_lbs == "L":
        converted_weight = weight/2.205
    else:
        print("Invalid input, You are allowed to type K or L only for conversion")
        return None
    
    return round(converted_weight, 2)
  
if __name__ == "__main__":
    main()
    
