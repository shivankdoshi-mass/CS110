print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print("Stock contains:")
print("   25 nickels")
print("   25 dimes")
print("   25 quarters")
print("   0 ones")
print("   0 fives")

nickel = 5
dime = 10
quarter = 25
onedollar = 100
fivedollar = 500

a = ''
b = ''
c = ''
d = ''

while True:
    print("")
    k = input("Enter the purchase price (xx.xx) or `q' to quit:")
    print("")

    if k == "q": #to quit
        break

    if "-" in k: #for minus signs
        print("Illegal price: Must be a non-negative multiple of 5 cents.")     


    ############


    elif "." in k: #for decimal place
        c = k.split(".") # split decimal place right and left
   



        if c[0].isdigit() == True and c[1].isdigit() == True:       # #checks if right and left values are numbers    

            a = float(k) #converts input to float
            b = a*100   #multiplies into 100
            g = round(b)    #round
            dollar_value = c[0]
            cent_value = c[1]

            if g % 5 == 0:  #checks if number is multiple of 5


                ####   #digits that are decimals 



                ##menu1
                print("")
                print("Menu for deposits:")
                print("  'n' - deposit a nickel")
                print("  'd' - deposit a dime")                
                print("  'q' - deposit a quarter")                
                print("  'o' - deposit a one dollar bill")                
                print("  'f' - deposit a five dollar bill")
                print("  'c' - cancel the purchase")

                ## input dollar or cent value 



                total1 = g


                

                while True:


                    if total1<0:
                        print("Please take the change below.")
                        print(str(abs(float(total1)/100)))
                    





                    
                    str1 = str(float(total1)/100)
                    strsplit = str1.split(".")
                    strsplitdollar = strsplit[0]
                    strsplitcent = strsplit[1]
    




                    if int(strsplitdollar) != 0 and int(strsplitcent) != 0:
                        print("")
                        print("Payment due: " + strsplitdollar + " dollars and " + strsplitcent + " cents")
                    
                    elif int(strsplitdollar) == 0 and int(strsplitcent) != 0:
                        print("")
                        print("Payment due: "  + strsplitcent + " cents")     

                    elif int(strsplitdollar) != 0 and int(strsplitcent) == 0:
                        print("")
                        print("Payment due: " + strsplitdollar + " dollars and " + strsplitcent + " cents")

 


                    deposit = input("Indicate your deposit:")


                    if deposit == "n":
                        total1 = int(total1) - int(nickel)
                        float(total1)/100

                    elif deposit == "d":
                        total1 = int(total1) - int(dime)
                        float(total1)/100

                    elif deposit == "q":
                        total1 = int(total1) - int(quarter)
                        float(total1)/100

                    elif deposit == "o":
                        total1 = int(total1) - int(onedollar)
                        float(total1)/100

                    elif deposit == "f":
                        total1 = int(total1) - int(fivedollar)
                        float(total1)/100

                    elif deposit == "c":
                        print("Please take the change below.")
      
                        print(total1//25, "quarters")
                        total1 = total1%25
                        print(total1//5, "nickles")
                        total1 = total1%5

                        print(total1//10, "dimes")
                        total1 = total1%10

                        print(total1//1, "pennies")
                        break
                        


                    else:
                        print("Illegal selection: " + deposit)








            else :                
                print("Illegal price: Must be a non-negative multiple of 5 cents.")     








        #############

        elif c[0] == d and c[1].isdigit() ==  True:             #checks if input is number like .5, .45 etc
            a = float(k)
            b = a*100
            g = round(b)
            
            cent_value = c[1]

            if g % 5 == 0:      #checks if number is multiple of 5


                #### # digits that have numbers after decimal


                ##menu2

                print("Menu for deposits:")
                print("  'n' - deposit a nickel")
                print("  'd' - deposit a dime")                
                print("  'q' - deposit a quarter")                
                print("  'o' - deposit a one dollar bill")                
                print("  'f' - deposit a five dollar bill")
                print("  'c' - cancel the purchase")

                ## input dollar or cent value 





                total2 = g



                while True:

                    if total2<0:
                        print("Please take the change below.")
                        print(str(abs(float(total2))/100))





                    print("Payment due: " + str(total2) + " cents ")




                    deposit = input("Indicate your deposit:")


                    if deposit == "n":
                        total2 = int(total2) - int(nickel)
                        float(total2)/100

                    elif deposit == "d":
                        total2 = int(total2) - int(dime)
                        float(total2)/100

                    elif deposit == "q":
                        total2 = int(total2) - int(quarter)
                        float(total2)/100

                    elif deposit == "o":
                        total2 = int(total2) - int(onedollar)
                        float(total2)/100

                    elif deposit == "f":
                        total2 = int(total2) - int(fivedollar)
                        float(total2)/100

                    elif deposit == "c":

                        print("Please take the change below.")
      
                        print(total1//25, "quarters")
                        total1 = total1%25
                        print(total1//5, "nickles")
                        total1 = total1%5

                        print(total1//10, "dimes")
                        total1 = total1%10

                        print(total1//1, "pennies")
                        break


                    else:
                        print("Illegal selection: " + deposit)











            else :                
                print("Illegal price: Must be a non-negative multiple of 5 cents.")    





        ###############






        elif c[1].isdigit() == False or c[0].isdigit() == False:        #checks if both sides are not numbers

            print("Invalid purchase price. Try again")  




    ############


    elif k.isdigit() == True:       # only for non decimal numbers
            if float(k) % 5 == 0:       # checks if it is a multiple of 5


                #### # whole digit 

                dollar_value = k

                #menu3

                print("Menu for deposits:")
                print("  'n' - deposit a nickel")
                print("  'd' - deposit a dime")                
                print("  'q' - deposit a quarter")                
                print("  'o' - deposit a one dollar bill")                
                print("  'f' - deposit a five dollar bill")
                print("  'c' - cancel the purchase")

                ## input dollar or cent value 





                total3 = int(k)*100



                while True:

                    if total3<0:
                        print("Please take the change below.")                        
                        print(str(abs(total3)))
                        



                    str4 = str(float(total3)/100)
                    strsplit4 = str4.split(".")
                    strsplitdollar4 = strsplit4[0]
                    strsplitcent4 = strsplit4[1]



                    print("Payment due: " + strsplitdollar4 + " dollars " + strsplitcent4 + " cents")





                    deposit = input("Indicate your deposit:")

                    
                    if deposit == "n":
                        total3 = int(total3) - int(nickel)
                        total3

                    elif deposit == "d":
                        total3 = int(total3) - int(dime)
                        total3

                    elif deposit == "q":
                        total3 = int(total3) - int(quarter)
                        total3

                    elif deposit == "o":
                        total3 = int(total3) - int(onedollar)
                        total3

                    elif deposit == "f":
                        total3 = int(total3) - int(fivedollar)
                        total3

                    elif deposit == "c":

                        print("Please take the change below.")
      
                        print(total1//25, "quarters")
                        total1 = total1%25
                        print(total1//5, "nickles")
                        total1 = total1%5

                        print(total1//10, "dimes")
                        total1 = total1%10

                        print(total1//1, "pennies")
                        break


                    else:
                        print("Illegal selection: " + deposit)



            else :                
                print("Illegal price: Must be a non-negative multiple of 5 cents.")    
           




    elif k.isdigit() == False:      # checks if input is a number at all
        print("Invalid purchase price. Try again") 
        

        
