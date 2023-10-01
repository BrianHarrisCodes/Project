import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Popularity of Baby Names in the United States 1880-2022')


df = pd.read_csv(r'C:\Users\brian\Project\Project\Portfolio_Projects\1_Popular_Names\Names\big_list.csv')
df2=pd.read_csv(r'C:\Users\brian\Project\Project\Portfolio_Projects\1_Popular_Names\Names\girls.csv')
df3=pd.read_csv(r'C:\Users\brian\Project\Project\Portfolio_Projects\1_Popular_Names\Names\boys.csv')
baby_name = st.text_input("Baby name", placeholder="Enter a baby name")
gender = st.radio("Gender of the baby", ("M", "F"))
baby_name = baby_name.strip().capitalize()

if baby_name != "":
    name_df = df[(df.name == baby_name) & (df.sex == gender)]
    name_df = name_df.sort_values("year")
    rank_df = df2[(df2.name == baby_name) & (df2.sex == gender)]
    rank_df2 = df3[(df3.name == baby_name) & (df3.sex == gender)]
        
    fig = plt.figure(figsize = (10, 5))
    plt.plot(name_df['year'], name_df['count'])
    plt.xlabel("Years")
    plt.ylabel("No. of babies")
    plt.title(f"Trend of the name {baby_name} in USA from 1880 to 2020")

    st.pyplot(fig)

    col1, col2= st.columns(2,gap="small")

    with col1:
        st.header("Information By Year")
        st.dataframe(name_df.style.format(thousands=''), hide_index= True)

    with col2:
        st.header("Female or Male Ranking and Stats")
        st.dataframe(
            rank_df.style.format(thousands=''),
            column_config={
                "rank": "Overall Rank",
                "name": "Name",
                "year_min": "First Year",
                "year_max": "Latest Year",
                "n_percent": "Percentile",
                "n_sum": "Total",
                "year_pop": "Most Popular Year"
    },
            hide_index=True,
)
        st.dataframe(
            rank_df2.style.format(thousands=''),
            column_config={
                "rank": "Overall Rank",
                "name": "Name",
                "year_min": "First Year",
                "year_max": "Latest Year",
                "n_percent": "Percentile",
                "n_sum": "Total",
                "year_pop": "Most Popular Year"
    },
            hide_index=True,
)