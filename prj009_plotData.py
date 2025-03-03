import matplotlib.pyplot as plt

def plot2D(x, y):
    plt.plot(x, y)
    plt.xlabel('Number of Days')  
    plt.ylabel('Temperature of City')   
    plt.title('Sample Plot for Displaying 2D Data')  
    plt.show()  

days  = [1, 2, 3, 4 , 5]
temps = [25, 18, 40, 36, 29]
 
plot2D(days, temps)