import streamlit as st
import pandas as pd

# df=pd.read_csv('./zni2020a.csv')

st.header('2020年基準消費者物価指数(1970~2025年)')
if st.toggle(label='チュートリアルの表示',value=False) == True:
    st.write('''2020年基準消費者物価指数とは、2020年の物価指数の平均を100としたときの数値です。
             \n物価指数の値が100よりも高い場合は2020年頃と比べて物価が高騰しており、低い場合は物価は2020年頃と比べて低かったことが分かります。
             \nこのアプリは1970年から2025年までの物価推移のグラフを表示します。また、品目ごとの物価指数の推移を検索することが可能で、検索品目は一つまでですが。''')

with st.sidebar:
    st.subheader('検索条件')
    category=st.text_input('検索する品目を入力してください',value='総合')
    st.subheader('検索する時期')
    # time=st.