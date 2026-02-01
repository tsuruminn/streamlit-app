import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('tni2020a.csv',encoding='cp932')
# 検索用に1行目の年以外の項目を取り出す。
options = df.columns.tolist() # 全部の列名リストを取得
options.remove('年')          # リストから「年」だけ削除


st.title('2020年から見た物価の推移')
st.header('2020年基準消費者物価指数(1970~2025年)')
if st.toggle(label='チュートリアルの表示',value=True) == True:
    st.write('''2020年基準消費者物価指数とは、2020年の物価指数の平均を100としたときの数値です。
             \n物価指数の値が100よりも高い場合は2020年頃と比べて物価が高騰しており、低い場合は物価は2020年頃と比べて低かったことが分かります。
             \nこのアプリは1970年から2025年までの物価推移のグラフを表示します。また、品目や時期を選んで検索することが可能です。
             \n検索品目は複数選択できるので、ある品目の物価が上がった時に、別の品目は物価が下がっているといった関係性を見るのにも役に立ちます。
             \n※画面左上の>からサイドバーを展開すると検索ができます。''')

with st.sidebar:
    st.subheader('検索条件')
    category=st.multiselect('検索する品目を選択してください',
                          options,
                            )
    st.subheader('検索する時期')
    
    year1=st.number_input('開始年',
                        min_value=1970,
                        max_value=2026,
                        value=1970,
                        step=1)
    text=st.write('から')
    year2=st.number_input('終了年',
                        min_value=1970,
                        max_value=2026,
                        value=2026,
                        step=1)

filtered_df = df[
    (df['年'] >= year1) &
    (df['年'] <= year2) 
]

df = filtered_df[['年']+category]


# st.dataframe(df,width=600,height=200) #データを正しく取れているか確認

# 折れ線グラフ

with st.spinner("グラフを描画中です"):
    fig = px.line(df,
              x='年',
              y=category,
              markers=True,
              title='消費者物価指数の推移',
              labels={'value': '物価指数', 'variable': '品目'}) # 軸ラベルの変更
    st.plotly_chart(fig)

# 散布図
# 2つ選ばれている時だけ表示する
with st.spinner("グラフを描画中です"):
    if len(category) > 2 or len(category) < 2:
        st.info("散布図を見るには、品目を2つだけに絞ってください。")
    elif len(category) == 2:
        st.subheader('散布図から分かる相関関係')
    
        fig_scatter = px.scatter(
            df,
            x=category[0], # 1つ目の品目
            y=category[1], # 2つ目の品目
            color='年',
            title=f'{category[0]}と{category[1]}の価格相関',
            labels={f'{category[0]}':f'{category[0]}の指数', f'{category[1]}': f'{category[1]} の指数'}
        )
 
        st.plotly_chart(fig_scatter)