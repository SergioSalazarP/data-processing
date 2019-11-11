import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./principal.csv")

fig = plt.figure(figsize=(30,10))

plt.subplot2grid((2,3),(0,0))
data.SEXO.value_counts().plot(kind='bar', alpha=0.5)
plt.title('Sobrevivieron - cuenta total -')

plt.subplot2grid((2,3),(0,1))
data.SEXO.value_counts(normalize = True).plot(kind='bar', alpha=0.5)
plt.title('Sobrevivieron - porcentaje total -')

plt.show()