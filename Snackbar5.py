import random
totalCostSauce = 0
fullPatatOrder = ''
totalCostFrikandel = 0
fullFrikandelOrder = ''
totalCostKroket = 0
fullKroketOrder = ''



def calculateTotalCost(): 
    
    totalCostSnacks = totalCostFrikandel + totalCostKroket + totalCostSauce + totalCostBittergarnituur
    return totalCostSnacks

def createTicket(totalCostSnacks, fullPatatOrder, fullKroketlOrder, fullFrikandelOrder):
    allExtras = fullKroketlOrder + fullPatatOrder + fullFrikandelOrder + bittergarnituurlijst
    if totalCostSnacks == 0:
        print('Bon\n' + 'U heeft niks besteld.')
    elif totalCostSnacks <= 10.00:
        totalCost = totalCostSnacks + 5
        print(allExtras + '\nBon:\nUw totale kosten zijn: €' + str(round(totalCost, 2)))
    elif totalCostSnacks >= 10.00 and totalCostSnacks < 40.00:
        print(allExtras + '\nBon:\nUw totale kosten zijn: €' + str(round(totalCostSnacks, 2)))
    elif totalCostSnacks >= 40 and totalCostSnacks <= 100:
        totalCost = totalCostSnacks * 0.95
        print(allExtras + '\nBon:\nUw totale kosten zijn: €' + str(round(totalCostSnacks * 0.95, 2)))
    elif totalCostSnacks > 100: 
        totalCost = totalCostSnacks * 0.925 
        print(allExtras + '\nBon:\nUw totale kosten zijn: €' + str(round(totalCost, 3)))

def chooseSauce(whatSauce, Snack):
    totalCostSauce = 0
    fullOrder = ''
    if whatSauce == 1:
        totalCostSauce += 0.50
        fullOrder += Snack + ' met Mayonaise'
    elif whatSauce == 2:
        totalCostSauce += 0.40
        fullOrder += Snack + ' met Ketchup'
    elif whatSauce == 3:
        totalCostSauce += 0.80
        fullOrder += Snack + ' met Pindasaus'
    elif whatSauce == 4:
        totalCostSauce += 0
        fullOrder += Snack + ' zonder saus'
    return fullOrder, totalCostSauce

def makeSnackList():
    bitterGarnituurLijst = ''
    Bittergarnituur = ['bitterbal ', 'kaasvlammetje ', 'kroketje ', 'frikandel ']
    size = input('Wilt u mini, normaal of groot?')
    if size == 'mini':
        for i in range(6):
            bitterGarnituurLijst = bitterGarnituurLijst + random.choice(Bittergarnituur)
            totalCostBittergarnituur = 3.00
    elif size == 'normaal':
        for i in range(12):
            bitterGarnituurLijst = bitterGarnituurLijst + random.choice(Bittergarnituur)
            totalCostBittergarnituur = 5.50          
    if size == 'groot':
        for i in range(18):
            bitterGarnituurLijst = bitterGarnituurLijst + random.choice(Bittergarnituur)
            totalCostBittergarnituur = 10
    return totalCostBittergarnituur, bitterGarnituurLijst

def makeDictionary(whatOrder, amount):
    wholeOrder = {'Patat' : 0, 'Frikandel' : 0, 'Kroket' : 0}
    wholeOrder[whatOrder] = amount
    print(wholeOrder)
       
while True:
    whatOrder = input('Wat wilt u bestellen?')
    if whatOrder == 'Patat':
        amount = int(input('Hoeveel wilt u daar van bestellen?'))
        makeDictionary(whatOrder, amount)

        for i in range(amount):
            whatSauce = int(input('Welke saus wilt u erbij?\nMayonaise(1), Ketchup(2), Pindasaus(3), Geen saus(4)'))
            fullPatatOrder, totalCostSaucePatat = chooseSauce(whatSauce, whatOrder)
            totalCostSauce += totalCostSaucePatat
            totalCostSauce += 2.95
    if whatOrder == 'Frikandel':
        amount = int(input('Hoeveel wilt u daar van bestellen?'))
        makeDictionary(whatOrder, amount)
    
        for i in range(amount):
            whatFrikandel = int(input('Wat voor soort frikandel wilt u?\nNormaal(1), XXL(2), Vega(3)'))
            whatOrder = 'Frikandel'
            whatSauce = int(input('Welke saus wilt u erbij?\nMayonaise(1), Ketchup(2), Pindasaus(3), Geen saus(4)'))
            fullFrikandelOrder, totalCostSauceFrikandel = chooseSauce(whatSauce, whatOrder)
            totalCostSauce += totalCostSauceFrikandel
            totalCostSauce += 2.95
            if whatFrikandel == 1:
                totalCostFrikandel += 0
                fullFrikandelOrder = '\n'+ 'Normale ' + fullFrikandelOrder + '\n'
            elif whatFrikandel == 2:
                totalCostFrikandel += 1.00
                fullFrikandelOrder = '\n'+ 'XXl ' + fullFrikandelOrder + '\n'
            elif whatFrikandel == 3:
                totalCostFrikandel += 1.50
                fullFrikandelOrder = '\n'+ 'Vega ' + fullFrikandelOrder + '\n'
            totalCostFrikandel += 2.80

    if whatOrder == 'Kroket':
            amount = int(input('Hoeveel wilt u daar van bestellen?'))
            makeDictionary(whatOrder, amount)

        for i in range(amount):
            whatKroket = int(input('Wilt u een broodje bij de kroket?\nJa(1), Nee(2)'))
            whatOrder = 'Kroket'
            whatSauce = int(input('Welke saus wilt u erbij?\nMayonaise(1), Ketchup(2), Pindasaus(3), Geen saus(4)'))
            fullKroketOrder, totalCostSauceKroket = chooseSauce(whatSauce, whatOrder)
            totalCostSauce += totalCostSauceKroket
            totalCostSauce += 2.95
            if whatKroket == 1:
                totalCostKroket += 1.00
                fullKroketOrder = '\n'+ fullKroketOrder + ' en met broodje\n'
            elif whatFrikandel == 2:
                totalCostKroket += 0
                fullKroketOrder = '\n'+ fullKroketOrder + ' en zonder broodje\n'
            totalCostKroket += 2.50
    surpise = input('Wilt u een surpise bittergarnituur')
    if surpise == 'ja':
        totalCostBittergarnituur, bittergarnituurlijst = makeSnackList()
    opnieuw = int(input('Wilt u meer bestellen?\nJa(1), Nee(2)'))
    if opnieuw == 2:

        break



    
        
totalCostSnacks = calculateTotalCost()
print(totalCostSnacks)
createTicket(totalCostSnacks, fullPatatOrder, fullKroketOrder, fullFrikandelOrder)
