import streamlit as st

st.set_page_config(
    page_title="Cybercime?",
    page_icon="🕵",
)

st.write("# Mari mengenal Cybercrime lebih dekat! 👋")

st.sidebar.success("Pilih salah satu artikel dari dropdown berikut.")

st.markdown(
    """
    Secara umum, arti dari cybercrime adalah suatu bentuk kejahatan virtual dengan memanfaatkan perangkat 
    komputer yang terhubung dengan jaringan Internet. Tindakan tersebut tentunya melanggar hukum, sebab dapat menimbulkan kerugian bagi orang lain.
    Menyadur dari buku Etika Profesi Informatika oleh Muhammad Ridha Albaar, kejahatan siber pertama kali ditemukan 
    pada 1988 dengan istilah cyber attack. Saat itu, seorang mahasiswa berhasil menciptakan sebuah worm atau virus 
    yang dapat menyerang program komputer dan dapat mematikan sekitar 10 persen dari seluruh jumlah komputer di dunia yang terhubung di Internet.
"""
)

import streamlit as st

st.set_page_config(page_title="Tipe-tipe Cybercrime", page_icon="⚠️")

st.markdown("# Tipe-tipe Cybercrime")
st.sidebar.header("Tipe-tipe Cybercrime")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

  
page_names_to_funcs = {
    "Home": intro,
    "Tipe-tipe Cybercrime": cybercrime_type,
}

demo_name = st.sidebar.selectbox("Pilih salah satu artikel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
