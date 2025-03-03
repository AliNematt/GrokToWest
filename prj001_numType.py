def evenPrinter(lastNum):
    for i in range(lastNum+1):
        print(f"{i} is an Even Number") if i % 2 == 0 else False
        
evenPrinter(100)
