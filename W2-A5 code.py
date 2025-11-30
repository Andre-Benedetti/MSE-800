
def main():

    N = str(input("Enter the temperature in the format TNN as T = F for Fereinheint and C for Celsius and NN as two digits temperature: ")) #input from the user
      
    if len(N) < 2:
        print("Please enter the temperature in the correct format.")
        return # exit if error
       
    temp = N[0]

    if N[1:].isdigit() == False:
        print("Please enter a valid numeric temperature value.")
        return # exit if error
    
    num = float (N[1:]) #extracting the temperature value
    
    

    if temp == 'F':
        C = float ((num - 32) * 5.00/9.00)
        print (f"{N} degrees Fereinheint converted to Celsius is: {C:.2f} C")
    elif temp == 'C':
        F = (num * 9.00/5.00) + 32
        print (f"{N} degrees Celsius converted to Fereinheint is: {F:.2f} F") 
    else:
        print("Invalid Input. Please enter the temperature with the correct 'C' of 'F' prefix.")

if __name__ == "__main__":

    main()