#activity 1
"""
name = "John Doe"
Age = 28
Skills = ["Python","SQL","Power Bi"]
Education = ("BSC Computer Science", 2020)
Contact_Details = {"email": "jdoe@gmail.com", "phone": "0222222222"} 
Certifications = {"Azure", "AWS"}
"""

#activity 2

"""
#Assigning weekly hours worked
hours = 25
#Assingning weekly Payrate
payrate = 31.2
grosspay = hours * payrate
#Priting the Weekly grosspay
print (grosspay)

e_grosspay = grosspay * 54

if e_grosspay <= 15600
    netpay = grosspay * (1-10.5%)
elif e_grosspay  <= 53500
    netpay = 15600 * (1-10.5%) + (grosspay - 15600) * (1-17.5%)
elif e_grosspay  <= 78100
    netpay = 15600 * (1-10.5%) + (53500-15600)*(1-17.5%) + (grosspay - 78100)* (1-30%)
elif e_grosspay  <= 180000
    netpay = 15600 * (1-10.5%) + (53500-15600)*(1-17.5%) + (78000 - 53500)* (1-30%) + (grosspay - 180000) * (1-33%)
else
    netpay = 15600 * (1-10.5%) + (53500-15600)*(1-17.5%) + (78000 - 53500)* (1-30%) + (180000-78000) * (1-33%) + (grosspay-180000) * (1-39%)
"""
    

#activity 3 Fibonacci

def main():

    Fibo = 1 #smallest Fiboacci element considering the series started as 0, 1
    Factorial = 1 #smallest Factorial 
    i = 1 # aux variables
    
    N = int(input("Enter N: ")) #enter from the user

    j = N # aux variables

    while i < N: #calculating element N of Fibonacci series
        Fibo = Fibo + i
        i = Fibo - i

    print (f"The Nth element of the Fibonacci series is: {Fibo}")

    while j > 0: #calculating factorial
        Factorial = j * Factorial
        j=j-1

    print (f"The Factorial of {N} is: {Factorial}")

if __name__ == "__main__":

    main()

