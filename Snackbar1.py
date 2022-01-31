from tkinter import W


amountPatat = int(input("Hoeveel patat wilt u bestellen?"))
amountFrikadellen = int(input("Hoeveel frikadellen wilt u bestellen?"))
amountKroketten = int(input("Hoeveel kroketten wilt u bestellen?"))

def calculateTotalCost(): 
    totalKroketten = amountKroketten * 2.50
    totalCostSnacks = totalCostFrikandel+ totalKroketten + totalCostPatat
    return totalCostSnacks

def createTicket(totalCostSnacks):
    if totalCostSnacks == 0:
        print('Bon\n' + 'U heeft niks besteld.')
    elif totalCostSnacks <= 10.00:
        totalCost = totalCostSnacks + 5
        print('Bon:\nUw totale kosten zijn: ' + str(round(totalCost, 2)))
    elif totalCostSnacks >= 10.00 and totalCostSnacks < 40.00:
        print('Bon:\nUw totale kosten zijn: ' + str(round(totalCostSnacks, 2)))
    elif totalCostSnacks >= 40 and totalCostSnacks <= 100:
        totalCost = totalCostSnacks * 0.95
        print('Bon:\nUw totale kosten zijn: ' + str(round(totalCostSnacks * 0.95, 2)))
    elif totalCostSnacks > 100: 
        totalCost = totalCostSnacks * 0.925 
        print('Bon:\nUw totale kosten zijn: ' + str(round(totalCost, 2)))

totalCostPatat = 0
totalCostFrikandel = 0
totalCostKroket = 0
for i in range(amountPatat):
    whatSauce = int(input('Welke saus wilt u erbij?\nMayonaise(1), Ketchup(2), Pindasaus(3)'))
    if whatSauce == 1:
        totalCostPatat += 0.50
    elif whatSauce == 2:
        totalCostPatat += 0.40
    elif whatSauce == 3:
        totalCostPatat += 0.80
    totalCostPatat += 2.95
    print(totalCostPatat)

for i in range(amountFrikadellen):
    whatFrikandel = int(input('Wat voor soort frikandel wilt u?\nNormaal(1), XXL(2), Vega(3)'))
    if whatFrikandel == 1:
        totalCostFrikandel += 0
    elif whatFrikandel == 2:
        totalCostFrikandel += 1.00
    elif whatFrikandel == 3:
        totalCostFrikandel += 1.50
    totalCostFrikandel += 2.80

for i in range(totalCostKroket):
    

totalCostSnacks = calculateTotalCost()
print(totalCostSnacks)
createTicket(totalCostSnacks)
