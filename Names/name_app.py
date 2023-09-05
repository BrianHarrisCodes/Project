import streamlit as st
import pandas as pd
import numpy as np

boy_names = pd.read_csv(r'C:\Users\brian\Project\Project\Names\boys.csv')
girl_names = pd.read_csv(r'C:\Users\brian\Project\Project\Names\girls.csv')
all_names = pd.read_csv(r'C:\Users\brian\Project\Project\Names\all-names.csv')


st.title('Popularity of Baby Names in the United States Over Time')
