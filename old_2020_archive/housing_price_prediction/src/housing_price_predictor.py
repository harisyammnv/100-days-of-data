import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pathlib
import streamlit as st
plt.style.use('ggplot')

HOUSING_PATH = pathlib.Path.home()/'PycharmProjects'/'ML_WS'/'housing_price_prediction'/'data'


@st.cache
def loading_housing_data(housing_path: pathlib.Path) -> pd.DataFrame:
    data_path = pathlib.Path.joinpath(housing_path, 'housing.csv')
    return pd.read_csv(str(data_path))


st.title("California Housing Prices")

st.write("""
# Data Exploration
""")

data = loading_housing_data(HOUSING_PATH)
st.subheader("Peek into Raw Data")
st.write(data)
st.write("""
**Observations:** 
- The dataset contains one column `ocean_proximity` as a categorical column
- Latitude and Longitude for geo-spatial information
- The target variable is `median_house_value`
- Since the target variable is a continuous numeric value this a - `Regression task`  
""")

st.subheader("Stats")
st.write("Dataset shape: ", data.shape)
st.write(data.describe())

fig, ax = plt.subplots(3, 3, figsize=(18, 12))
i, j = (0, 0)
for col in data.columns:
    if col != 'ocean_proximity':
        sns.histplot(data[col], color='orange',
                     hist_kws={'alpha':1,"linewidth": 4},
                     kde_kws={"color": "black", "lw": 2}, ax=ax[i][j])
        j = j+1
        if j % 3 == 0:
            i, j = (i+1, 0)

st.pyplot(fig, dpi=600)

st.subheader("Geo Spatial Information")
st.map(data)