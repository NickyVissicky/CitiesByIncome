import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/CT-towns-income-census-2020.csv")
df.head(5)

df['Per capita income'] = df['Per capita income'].str.replace('$', '').str.replace(',', '').astype(int)
df['Median household income'] = df['Median household income'].str.replace('$', '').str.replace(',', '').astype(int)
df['Median family income'] = df['Median family income'].str.replace('$', '').str.replace(',', '').astype(int)

st.markdown("# Team Members")
st.markdown("Just Nicholas Vissicchio")

county = st.selectbox("Select a County", df['County'].unique())
selectedCounty = df[df['County'] == county]
st.dataframe(selectedCounty[['Place', 'Median household income']], width=800, height=200)

minIncome = st.number_input(
    "Select the minimum median household income...",
    min_value=int(df['Median household income'].min()),
    max_value=int(df['Median household income'].max()),
    value=int(df['Median household income'].min())
)

maxIncome = st.number_input(
    "Select the maximum median household income...",
    min_value=int(df['Median household income'].min()),
    max_value=int(df['Median household income'].max()),
    value=int(df['Median household income'].max()) 
)

#could not find a better way to do this ^

dfRange = selectedCounty[(selectedCounty['Median household income'] >= minIncome) &
                         (selectedCounty['Median household income'] <= maxIncome)]

st.dataframe(dfRange[['Place', 'Median household income']], width=800, height=200)

bestCities = df.nlargest(5, 'Median household income')[['Place', 'Median household income']]
worstCities = df.nsmallest(5, 'Median household income')[['Place', 'Median household income']]

citiesData = pd.concat([bestCities, worstCities])

plt.figure(figsize=(10, 8))
plt.bar(citiesData['Place'], citiesData['Median household income'])
plt.xlabel('City')
plt.ylabel('Median Income')
plt.title('Best and Worst CT Cities by Income')

st.pyplot(plt)
