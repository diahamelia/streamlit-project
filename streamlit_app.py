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
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")   
