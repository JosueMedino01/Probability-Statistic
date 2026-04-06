import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('bookTable.csv', sep=';')
dataset.columns = dataset.columns.str.strip()
dataFrame = pd.DataFrame(dataset)

education = dataFrame['Instrucao']

ni = education.value_counts()
ni.plot(kind='bar')
plt.title('Distribuição de Escolaridade')
plt.xlabel('Escolaridade')
plt.ylabel('Frequencia')

plt.xticks(rotation=0)
plt.show()