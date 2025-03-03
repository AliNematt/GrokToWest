import pandas as pd

def meanCSV(file): return file.Score.mean() 

df = pd.read_csv('students.csv')
print(meanCSV(df))
