import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import streamlit.components.v1 as components
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="Jumlah RT/RW Prov.DKI Jakarta",
                   page_icon="bar_chart:",
                   layout="wide"
)
st.title('VISUALISASI DATA RT/RW PROVINSI DKI JAKARTA!')    


# add a sidebar
st.sidebar.header("Data Setting")

with st.sidebar:
    choose = option_menu("Menu", ["About", "Project Planning"],
                         icons=['house', 'kanban'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#778899"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#E0FFFF"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
if choose =="About":
    st.markdown("Data jumlah RT/RW di Provinsi Jakarta menunjukkan adanya struktur administratif yang berlaku dalam pengorganisasian masyarakat setempat. Saat ini, daerah ini memiliki sejumlah total RT/RW yang mencerminkan tingkat kepadatan penduduk dan ukuran wilayahnya.")
    #image
    img=Image.open('gambar/peta_jakarta.png')
    st.image(img,width=300)
    st.markdown("Jumlah RT/RW di Provinsi Jakarta ini sangat bervariasi. Terdapat beberapa RT/RW dengan jumlah yang lebih besar, menandakan adanya kepadatan penduduk yang tinggi dan tingginya kebutuhan akan pengelolaan dan pelayanan publik di daerah tersebut. Sementara itu, terdapat juga RT/RW dengan jumlah yang lebih kecil, menandakan adanya wilayah yang kurang padat atau wilayah dengan jumlah penduduk yang lebih sedikit.")

#setup file uploud
if choose =="Project Planning":
    uploaded_file = st.sidebar.file_uploader(label="Unggah file CSV atau Excel anda.", type=['csv', 'xlsx'])
    print(uploaded_file)

    try:
        de = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        de = pd.read_excel(uploaded_file)

global numeric_columns

#chart
try:
    
    
    #widget filter

    city_filter = st.sidebar.selectbox("Filter by kabupaten", options=de['nama_kabupaten_kota'].unique())
    all_filter = st.sidebar.checkbox("Tampilkan seluruh data!")
    if all_filter:
        st.dataframe(de)
    
    
    # Apply filters
    filtered_de = de[
        (de['nama_kabupaten_kota'] == city_filter)
        
    ]
    if not all_filter:
        st.dataframe(filtered_de)

    st.write('line chart')
    st.line_chart(
       filtered_de,
        x=['nama_kecamatan'], 
        y='jumlah_rt'
    )
#plotly chart
   

   
except Exception as e:
    print(e)



