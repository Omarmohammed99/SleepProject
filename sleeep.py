import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st

df = pd.read_csv('clean_data.csv')

st.sidebar.header("Sleep Dashbord")
st.sidebar.image("sunflower.jpg")
st.sidebar.write("the purpose of dashboard is is to show the reason of sleep disorder")

cat_filter = st.sidebar.selectbox('Filters',['Gender','Occupation','BMI Category',None,'Sleep Disorder'])

a1, a2, a3, a4 = st.columns(4)
a1.metric("Avg Age", round(df['Age'].mean(), 2))
a2.metric("Count of ID", round(df['Person ID'].count(), 0))
a3.metric("Max Daily Steps", round(df['Daily Steps'].max(), 0))
a4.metric("Avg Sleep Duration", round(df['Sleep Duration'].mean(), 0))
st.subheader("Sleep Quality Vs Stress Level")

fig = px.scatter(
    data_frame=df, 
    x='Stress Level', 
    y='Quality of Sleep', 
    color=cat_filter, 
    size='Quality of Sleep'
)
st.plotly_chart(fig, use_container_width=True)

c1,c2 = st.columns([4,3])
with c1:
 st.text("Occupation vs avg sleep duration (sorted)")
 avg_sleep_by_occ = df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False).reset_index()
 fig1 = px.bar(data_frame=avg_sleep_by_occ, x='Occupation', y='Sleep Duration')
 st.plotly_chart(fig1 , use_container_width=True)

 with c2:
  
  st.text("Gender Vs Quality of sleep")
  gender_sleep = df.groupby('Gender')['Quality of Sleep'].mean().reset_index()
  fig2 = px.pie(gender_sleep, names='Gender',values = 'Quality of Sleep')
  st.plotly_chart(fig2,use_container_width=True)
 st.subheader("Par plot & heatmap for numerical features")

 num_cols = ['Physical Activity Level' , 'Stress Level' , 'Daily Steps' , 'Quality of Sleep']
 df_num = df[num_cols] 

st.text ("Pair Plot")
fig_pair = sns.pairplot(df_num)
st.pyplot(fig_pair)

st.text ("corrleation heatmap")

selected_col = ['Sleep Duration' , 'Quality of Sleep' , 'Physical Activity Level', 'Stress Level' , 'Heart Rate' , 'Daily Steps']

df_selected = df[selected_col]

fig_heat , ax = plt.subplots(figsize=(10,6))
sns.heatmap(df_selected.corr(), annot=True,cmap='coolwarm',fmt =".2f",ax=ax)
st.pyplot(fig_heat)