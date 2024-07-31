import streamlit as st

st.title('Title -> GeeksForGeeks')                  #Title
st.header('Header -> GeeksForGeeks')                #Header
st.subheader('Subheader -> GeeksForGeeks')          #SubHeader
st.text('Text -> GeeksForGeeks')                    #Text


st.markdown('# Hi')                                 #Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

st.success('Success!')                              #Success
st.info('Information!')                             #Info
st.warning('Warning')                               #Warning
st.error('Error')                                   #Error
st.exception(ZeroDivisionError('Division not possible')) #Exception
st.help(ZeroDivisionError)                                  #Help

st.write("range(1,10)")                                     #Wrtie
st.write(range(1,10))

st.write("1+2+3")
st.write(1+2+3)

st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

st.checkbox('Male')                                         #CheckBox
st.checkbox('Female')

if(st.checkbox('Adult')):                                   #CheckBox with validation
    st.write("You're an adult")

radioButton = st.radio('Select :', ('Male', 'Female', 'Other'))
if(radioButton == 'Male'):
    st.write("You're a male")
elif(radioButton == 'Female'):
    st.write("You're a female")
elif(radioButton == 'Other'):
    st.write("You're an other gender")
    
st.subheader('Select Box')                                  #SelectBox
selectBox = st.selectbox("Data Science :", ['Data Analysis', 'Web Scraping', 'Machine Learning', 
                                'Deep Learning', 'Natural Language Proceesing', 
                                'Computer Vision', 'Image Processing'])
st.write("You've selected: ", selectBox)


st.subheader('MultiSelect Box')
multiSelBox = st.multiselect("Data Science :", ['Data Analysis', 'Web Scraping', 'Machine Learning', 
                                'Deep Learning', 'Natural Language Proceesing', 
                                'Computer Vision', 'Image Processing'])
st.write("You've selected: ", len(multiSelBox), 'courses')


st.subheader("Button")
if(st.button('Click me')):
    st.write('Thanks for clicking me')


st.subheader("Slider")
vol = st.slider('Select the volume', 0,100,step = 1)
st.write('Volume is: ', vol)


st.subheader("Text Input")
username = st.text_input('Username: ')
password = st.text_input('Password :', type = 'password')


st.subheader("Text Area")
textArea = st.text_area('Write something interesting about yourself in 500 words')
st.write(textArea)

st.subheader("Input Number")
st.number_input('Select your age',18,110)

st.subheader("Input Date")
st.date_input('Date')

st.subheader("Input Time")
st.time_input('Time')
