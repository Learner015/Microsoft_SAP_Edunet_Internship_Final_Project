import streamlit as st

st.title('Welcome to Introduction to Streamlit')
st.header('Machine Learning')
st.subheader('Linear Regression')
st.info('Information of user')
st.warning('This is a warning')
# for emojis printing -> see below line
st.markdown(":smile: :books: :gift: :heart:")

# for image printing

from PIL import Image
img = Image.open("ML_Image.jpg")
st.image(img, width=300, caption='Machine Learning')

# for audio playing
st.audio("sample.mp3", start_time=10, format="audio/mp3", autoplay=True,end_time=20)

st.latex(r'''a + b x ^3 - y = 8 \\ sqrt(4) = y''')

# for wiget
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.checkbox('I agree')
st.radio('RADIO', [1,2,3])
st.selectbox('SELECT', [1,2,3])
st.multiselect('MULTI', ["AI Developer","Fashion Designer","Data Scientist"])
st.file_uploader('File uploader')
st.color_picker('Pick A Color')
st.date_input('Date input')


# for progress bar
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)


# for sidebar
st.sidebar.write('This is a sidebar')
st.sidebar.write('This is a sidebar')
st.sidebar.button("Resigter")
st.sidebar.button("Login")
st.sidebar.button("Logout")
st.sidebar.button("Profile")

# for table
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.table(df)



