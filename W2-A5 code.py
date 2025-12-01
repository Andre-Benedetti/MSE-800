
class Temp_converter:#Class to handle temperature conversion
   
    def __init__(self, full_input): #Constructor to initialize input
        
        self.N = full_input
       
    def validate_and_extract(self): #Method to validate input and extract scale and value
        
        if len(self.N) < 2: #input must be at least 2 characters long
            print("Please enter the temperature in the correct format.")
            return False

        self.scale = self.N[0]
        value_str = self.N[1:]
        
        if not value_str.isdigit():#check if the value part is not numeric
             try:
                 self.temp_value = float(value_str)
             except ValueError:
                 print("Please enter a valid numeric temperature value.")
                 return False
                
        if value_str.isdigit():#convert string to float
             self.temp_value = float(value_str)

        if self.scale not in ['F', 'C']:#check if the scale is valid
            print("Invalid Input. Please enter the temperature with the correct 'C' of 'F' prefix.")
            return False

        return True

    def convert(self):#Method to perform the conversion
             
        num = self.temp_value
        temp = self.scale

        if temp == 'F':#convert F to C
            C = (num - 32) * 5.0 / 9.0
            print(f"{self.N} degrees Fereinheint converted to Celsius is: {C:.2f} C")
        
        elif temp == 'C':#convert C to F
            F = (num * 9.0 / 5.0) + 32
            print(f"{self.N} degrees Celsius converted to Fereinheint is: {F:.2f} F")
        
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