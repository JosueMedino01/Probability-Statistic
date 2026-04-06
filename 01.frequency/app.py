import pandas as pd

# How read a CSV
dataset = pd.read_csv('bookTable.csv', sep=';')
dataset.columns = dataset.columns.str.strip()
dataFrame = pd.DataFrame(dataset)

# How create a frequency table to Discrete variable
education = dataFrame['Instrucao']

freqEducationTable = pd.DataFrame({
    'Ni': education.value_counts(),
    'Fi': education.value_counts(normalize=True),
    '100Fi': education.value_counts(normalize=True) * 100,
})

freqEducationTable.loc['Total'] = [
    freqEducationTable['Ni'].sum(),
    freqEducationTable['Fi'].sum(),
    freqEducationTable['100Fi'].sum()
]

print(freqEducationTable)

# How create a frequency table to Continuous Variable
salary = dataFrame['Salario']

bins = pd.cut(salary, bins=5)

ni = bins.value_counts().sort_index()
fi = bins.value_counts(normalize=True).sort_index()

freqSalarytable = pd.DataFrame({
    'Ni': ni,
    'Fi': fi,
    '100Fi': fi * 100
})

freqSalarytable.loc['Total'] = [
    freqSalarytable['Ni'].sum(),
    freqSalarytable['Fi'].sum(),
    freqSalarytable['100Fi'].sum()
]

print(freqSalarytable)