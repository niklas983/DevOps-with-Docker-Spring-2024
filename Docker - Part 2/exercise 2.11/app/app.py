import streamlit as st
import pandas as pd
import plotly.express as px

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Set Streamlit page configuration
st.set_page_config(
    page_title='Real Estate Dashboard',
    page_icon=':house:',
    layout='wide'
)

# Load the dataset
df = pd.read_csv('cleaned_real.csv', sep=',')

# Sidebar
st.sidebar.header('Apartments in Albania')


# City filter
city = st.sidebar.multiselect('Choose city', df['City'].unique())
df2 = df[df['City'].isin(city)] if city else df.copy()

# Category filter
status = st.sidebar.multiselect('Choose category', df['Category'].unique())
df3 = df2[df2['Category'].isin(status)] if status else df2.copy()

# Data filtering logic could be simplified further, if needed.

# Calculate average price per m2
category_df = df3.groupby(by=['Category'], as_index=False)['Price/m2'].mean()

# Main content
st.title(':house: Real Estate Dashboard: Apartments in Albania')
st.markdown('<style>div.block-container{padding-top:2rem;}<style>', unsafe_allow_html=True)


# columns in dashboard
col1, col2 = st.columns((2))


st.subheader('Average price per m2')
fig = px.bar(category_df, x='Category', y='Price/m2', text=[f'${x:,.2f}' for x in category_df['Price/m2']], template='seaborn')
st.plotly_chart(fig, use_container_width=True, height=200)





#HISTOGRAM
# Calculate the count of apartments by city
filtered_df = df[df['City'].isin(city)] if city else df.copy()
city_counts = filtered_df['City'].value_counts().reset_index()
city_counts.columns = ['City', 'Apartment Count']

# Create a Plotly bar chart
fig = px.bar(city_counts, x='City', y='Apartment Count')
fig.update_xaxes(title_text='City')
fig.update_yaxes(title_text='Apartment Count')

st.subheader('Distribution of Apartments by City')
st.plotly_chart(fig, use_container_width=True)



# BOX PLOTS
fig_general = px.box(df, x='Category', y='Price', title='Price Distribution (General)')

# Main content
st.subheader('Price Distribution (General)')
st.plotly_chart(fig_general, use_container_width=True)

# Create a Plotly box plot for price distribution by chosen city
if city:
    fig_by_city = px.box(filtered_df, x='Category', y='Price', color='City', title='Price Distribution by City')
    st.subheader(f'Price Distribution by City ({", ".join(city)})')
    st.plotly_chart(fig_by_city, use_container_width=True)

# Create a Plotly box plot for price distribution by chosen category
if status:
    fig_by_category = px.box(filtered_df, x='City', y='Price', color='Category', title='Price Distribution by Category')
    st.subheader(f'Price Distribution by Category ({", ".join(status)})')
    st.plotly_chart(fig_by_category, use_container_width=True)

category_df = filtered_df.groupby(by= ['Category'],as_index= False)['Price'].median()
city_df = filtered_df.groupby(by= ['City'],as_index= False)['Price'].median()

with col1:
    st.subheader('Price by category')
    fig = px.bar(category_df, x= 'Category', y= 'Price', template='seaborn')
    st.plotly_chart(fig, use_container_width=True, height = 200)

with col2:
    st.subheader('Price by city')
    fig = px.line(city_df, values= 'Price', names= 'City')
    fig.update_traces(text=city_df['City'], textposition='outside')
    st.plotly_chart(fig, use_container_width= True)
