from tkinter import W


amountPatat = int(input("Hoeveel patat wilt u bestellen?"))
amountFrikadellen = int(input("Hoeveel frikadellen wilt u bestellen?"))
amountKroketten = int(input("Hoeveel kroketten wilt u bestellen?"))

def calculateTotalCost(): 
    
    totalCostSnacks = totalCostFrikandel + totalCostKroket + totalCostPatat
    return totalCostSnacks

def createTicket(totalCostSnacks):
    allExtras = fullKroketlOrder + fullPatatOrder + fullFrikandelOrder
    if totalCostSnacks == 0:
        print('Bon\n' + 'U heeft niks besteld.')
    elif totalCostSnacks <= 10.00:
        totalCost = totalCostSnacks + 5

        print(allExtras + '\nBon:\nUw totale kosten zijn: ' + str(round(totalCost, 2)))
    elif totalCostSnacks >= 10.00 and totalCostSnacks < 40.00:
        print(allExtras + '\nBon:\nUw totale kosten zijn: ' + str(round(totalCostSnacks, 2)))
    elif totalCostSnacks >= 40 and totalCostSnacks <= 100:
        totalCost = totalCostSnacks * 0.95
        print(allExtras + '\nBon:\nUw totale kosten zijn: ' + str(round(totalCostSnacks * 0.95, 2)))
    elif totalCostSnacks > 100: 
        totalCost = totalCostSnacks * 0.925 
        print(allExtras + '\nBon:\nUw totale kosten zijn: ' + str(round(totalCost, 3)))

totalCostPatat = 0
fullPatatOrder = ''
totalCostFrikandel = 0
fullFrikandelOrder = ''
totalCostKroket = 0
fullKroketlOrder = ''
for i in range(amountPatat):
    whatSauce = int(input('Welke saus wilt u erbij?\nMayonaise(1), Ketchup(2), Pindasaus(3), Geen saus(4)'))
    if whatSauce == 1:
        totalCostPatat += 0.50
        fullPatatOrder += 'Patat met Mayonaise\n'
    elif whatSauce == 2:
        totalCostPatat += 0.40
        fullPatatOrder += 'Patat met Ketchup\n'
    elif whatSauce == 3:
        totalCostPatat += 0.80
        fullPatatOrder += 'Patat met Pindasaus\n'
    elif whatSauce == 4:
        totalCostPatat += 0
        fullPatatOrder += 'Patat zonder saus\n'
    totalCostPatat += 2.95

for i in range(amountFrikadellen):
    whatFrikandel = int(input('Wat voor soort frikandel wilt u?\nNormaal(1), XXL(2), Vega(3)'))
    if whatFrikandel == 1:
        totalCostFrikandel += 0
        fullFrikandelOrder += 'Normale frikandel\n'
    elif whatFrikandel == 2:
        totalCostFrikandel += 1.00
        fullFrikandelOrder += 'XXl frikandel\n'
    elif whatFrikandel == 3:
        totalCostFrikandel += 1.50
        fullFrikandelOrder += 'Vega frikandel\n'
    totalCostFrikandel += 2.80

for i in range(amountKroketten):
    whatKroket = int(input('Wilt u een broodje bij de kroket?\nJa(1), Nee(2)'))
    if whatKroket == 1:
        totalCostKroket += 1.00
        fullKroketlOrder = 'Kroket met broodje\n'
    elif whatFrikandel == 2:
        totalCostKroket += 0
        fullKroketlOrder += 'Kroket zonder broodje\n'
    totalCostKroket += 2.50


totalCostSnacks = calculateTotalCost()
print(totalCostSnacks)
createTicket(totalCostSnacks)
