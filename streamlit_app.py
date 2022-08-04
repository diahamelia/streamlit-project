import streamlit as st

def intro():
    import streamlit as st

    st.write("# Hai, mari mengenal Cybercrime lebih dekat!👋")
    st.header("Apa sih Cybercrime itu?")
    st.sidebar.success("Silakan pilih salah satu artikel dari dropdown diatas")

    st.markdown(
        """
        Cybercrime adalah penggunaan komputer sebagai alat untuk meraih tujuan ilegal, seperti penipuan, 
        perdagangan konten pornografi anak, pencurian identitas, serta pelanggaran privasi. 
        Perbedaan utama kejahatan siber dengan tindakan kriminal konvensional adalah kehadiran 
        peran teknologi yang seolah-olah mempermudah tindakan buruk tersebut.
    """
    )

def cybercrime_protection():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data.
"""
    )

   
def cybercrime_type():
    import streamlit as st
    import time
    import numpy as np

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )
   
page_names_to_funcs = {
    "Home": intro,
    "Tipe-tipe Cybercrime": cybercrime_type,
    "Cara memproteksi diri dari Cybercrime": cybercrime_protection,
}

demo_name = st.sidebar.selectbox("Pilih artikel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
