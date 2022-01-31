from tkinter import W


amountPatat = int(input("Hoeveel patat wilt u bestellen?"))
amountFrikadellen = int(input("Hoeveel frikadellen wilt u bestellen?"))
amountKroketten = int(input("Hoeveel kroketten wilt u bestellen?"))

def calculateTotalCost():
    totalPatat = amountPatat * 2.95
    totalFrikadellen = amountFrikadellen * 2.80
    totalKroketten = amountKroketten * 2.50
    totalCostSnacks = totalFrikadellen + totalKroketten + totalPatat
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

for i in range(amountPatat):
    totalCostSauce = 0
    totalCostFrikandel = 0
    totalCostKroket = 0
    whatSauce = int(input('Welke saus wilt u erbij?\nMayonaise(1), Ketchup(2), Pindasaus(3)'))
    if whatSauce == 1:
        totalCostSauce += 0.50
    elif whatSauce == 2:
        totalCostSauce += 0.40
    elif whatSauce == 3:
        totalCostSauce += 0,80



print(totalCostSnacks)
createTicket(totalCostSnacks)
