import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My first app')

st.write("DataFrame")

# df =pd.DataFrame({
#     '1列目' : [1, 2, 3, 4],
#     '2列目' : [10, 20, 30, 40]
#     })

# st.write(df)
# st.dataframe(df, width=100, height=100)

# メモ
# code = '''def hello():
#      print("Hello, Streamlit!")'''
# st.code(code, language='python')


df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.28, 136.59],
    columns=['lat', 'lon']
)

#チェックしたら　右コラムに表示
col1, col2 = st.beta_columns(2)
col_check = col1.checkbox('Columnisation   # # チェックしたら、表示する')
if col_check:
    col2.write('ごちそうさま')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('お問い合わせ内容')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('お問い合わせ内容')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('お問い合わせ内容')


# ボタンを押したら表示
# st.button('Hit me')
# if st.checkbox('Check me out'):
#     st.write(df)

# # どれか選んで表示をさせる
# genre = st.radio(
#     "What's your favorite movie genre",
#     ('Comedy', 'Drama', 'Documentary'))
# if genre == 'Comedy':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn't select comedy.")


# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])
# st.text_input('Enter some text')
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.color_picker('Pick a color')


# チャート
# st.map(df)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# タイムチャージ
# st.empty()
# my_placeholder = st.empty()
# with st.empty():
#      for seconds in range(60):
#          st.write(f"⏳ {seconds} seconds have passed")
#          time.sleep(1)
#      st.write("✔️ 1 minute over!")
# my_placeholder.text('Replaced!')


# 式を表示
# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')

# # マジックコマンド
# """
# # 章
# ## 節
# ### 項

# ''' python
# import streamlit as st
# import numpy as np
# import pandas as pd
# import time
# '''
# """

# バルーンがあがる
# st.balloons()

# エラー表示
# st.error('This is an error')

# with st.spinner('Wait for it...'):
#     time.sleep(5)
#     st.success('Done!')