################################
################################
## Author        : Erik Marquez
## Due           : 9.1.2018
## Class         : comp sci 101 -002 TuTh 5:30-6:45
## program number: 1. Carmack's Bakery
##
## Calculate the amount of ingredients to order 
##      given how much of the product will be sold
##
## Step 1. Prompt amount of ingredients will be sold
## Step 2. Apply the ingredients formulas
## Step 3. Print out the results
################################


## Step 1. Prompt amount of ingredients will be made

print("Welcome to Carmack's Bakery!\n")
print("- Please enter how many items you Need Make.\n")
print("- You can enter any number: 0 - 100\n")

cookies = float(input('How many dozen cookies? => '))

cakes = float(inpu
              ('How many sheet cakes? => '))

donuts = float(input('How many dozen donuts? => '))

## Step 2. Apply the ingredients formulas

butter = (cookies * 2.5) + (cakes *.5) + (donuts * .25)

sugar = (cookies * 2) + (cakes * 1) + (donuts * .5)

eggs = (cookies * 2) + (cakes * 2) + (donuts * 3)

flour = (cookies * 8) + (cakes * 1.5) + (donuts * 5)

## Step 3. Print out the results

print('\nYou will need to order:')
print(butter, 'cups of butter.')
print(sugar, 'cups of sugar.')
print(eggs, 'eggs.')
print(flour, 'cups of flour.')



