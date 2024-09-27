import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('https://linked.aub.edu.lb/pkgcube/data/df6527f0de0990b7237dbcef186a3d52_20240904_215117.csv')


st.title("Tourism Analysis in Lebanese Towns")
st.write("""
Welcome to our interactive tourism analysis page! This app provides a look into the tourism infrastructure in Lebanese towns.
You can now explore the nature of tourism in lebanon and gain a better understanding of its landscape.
""")


st.header("Insights into Tourism Infrastructure")
st.write("""
The visualizations below explore the distribution of tourism infrastructure such as hotels and guest houses across different towns. 
You can use the dropdown menus and multi-select options to filter data based on specific towns or governorates, and see how different towns compare in terms of tourism performance.
""")


st.subheader("Total Number of Hotels vs Tourism Index")
st.write("""
This scatter plot shows the relationship between the number of hotels in each town and its Tourism Index. 
Use the dropdown below to choose one or more towns to compare.
""")


selected_towns = st.multiselect("Select Town(s)", options=data['Town'].unique(), default=[])


if selected_towns:
    filtered_data = data[data['Town'].isin(selected_towns)]
else:
    filtered_data = data  


fig1 = px.scatter(filtered_data, 
                 x='Total number of hotels', 
                 y='Tourism Index', 
                 size='Total number of guest houses', 
                 title=f'Total Number of Hotels vs Tourism Index for Selected Towns',
                 color='Town')
st.plotly_chart(fig1)


st.subheader("Distribution of the Tourism Index Across Governorates")
st.write("""
This box plot shows the distribution of the Tourism Index across different governorates. It highlights the variation in tourism performance within and between governorates.
Select a governorate to see the distribution of the Tourism Index in that region.
""")


selected_governorate = st.selectbox("Select a Governorate", data['refArea'].unique(), key="governorate_selector")


min_index, max_index = st.slider("Select Range of Tourism Index", 
                                 float(data['Tourism Index'].min()), 
                                 float(data['Tourism Index'].max()), 
                                 (float(data['Tourism Index'].min()), float(data['Tourism Index'].max())), 
                                 key="index_slider")


filtered_data_2 = data[(data['refArea'].str.contains(selected_governorate)) & 
                       (data['Tourism Index'] >= min_index) & 
                       (data['Tourism Index'] <= max_index)]


fig2 = px.box(filtered_data_2, 
              y='Tourism Index', 
              title=f'Distribution of the Tourism Index in {selected_governorate}')
st.plotly_chart(fig2)



