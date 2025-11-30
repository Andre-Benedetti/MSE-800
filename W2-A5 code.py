
class Temp_converter:
   
    def __init__(self, full_input):
        
        self.full_input = full_input
        self.scale = None
        self.temp_value = None

    def validate_and_extract(self):
        N = self.full_input

        if len(N) < 2:
            print("Please enter the temperature in the correct format.")
            return False

        self.scale = N[0].upper()
        value_str = N[1:]
        
        if not value_str.isdigit():
             try:
                 self.temp_value = float(value_str)
             except ValueError:
                 print("Please enter a valid numeric temperature value.")
                 return False
                
        if value_str.isdigit():
             self.temp_value = float(value_str)

        if self.scale not in ['F', 'C']:
            print("Invalid Input. Please enter the temperature with the correct 'C' of 'F' prefix.")
            return False

        return True

    def convert(self):
             
        num = self.temp_value
        temp = self.scale

        if temp == 'F':
            C = (num - 32) * 5.0 / 9.0
            print(f"{self.full_input} degrees Fereinheint converted to Celsius is: {C:.2f} C")
        
        elif temp == 'C':
            F = (num * 9.0 / 5.0) + 32
            print(f"{self.full_input} degrees Celsius converted to Fereinheint is: {F:.2f} F")
        
def main():
    
    # 1. Request user input
    uinput = input("Enter the temperature in the format UMM (U=F/C, MM=temperature value): ")
    converse = Temp_converter(uinput)
    
    # 2. validade the input and extract values
    if converse.validate_and_extract():
        # 3. Execute if validation was successful
        converse.convert()

if __name__ == "__main__":
    main()