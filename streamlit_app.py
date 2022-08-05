import streamlit as st

def intro():
    import streamlit as st

    st.write("# Mari mengenal Cybercrime lebih dekat🕵️")
    st.sidebar.success("Silakan pilih artikel dari dropdown berikut.")

    st.markdown(
        """
        Teknologi yang terus berkembang, tak lantas membebaskan kita dari berbagai jenis kejahatan di dunia maya atau cybercrime. 
        Pengertian cybercrime adalah sebuah kejahatan menggunakan komputer, Internet, dan sebagainya.
        Umumnya, jenis kejahatan ini dimanfaatkan oleh para pelakunya untuk mendapatkan informasi secara ilegal, memanipulasi data, 
        dan berbagai tindakan kejahatan virtual lainnya guna mendapatkan keuntungan. 
        Terus, apa sih yang dimaksud dengan cybercrime?.
        Oke, jadi Cybercrime adalah uatu bentuk kejahatan virtual dengan memanfaatkan perangkat komputer yang terhubung dengan jaringan Internet. 
        Tindakan tersebut tentunya melanggar hukum, sebab dapat menimbulkan kerugian bagi orang lain.
        Menyadur dari buku Etika Profesi Informatika oleh Muhammad Ridha Albaar, kejahatan siber pertama kali ditemukan pada 1988 dengan istilah cyber attack. 
        Saat itu, seorang mahasiswa berhasil menciptakan sebuah worm atau virus yang dapat menyerang program komputer dan dapat mematikan sekitar 10 persen 
        dari seluruh jumlah komputer di dunia yang terhubung di Internet.
    """
    )

def cybercrime_prevention():
    import streamlit as st
    st.write("# Bagaimana ya cara melindungi diri dari Cybercrime?")
    st.markdown(
        """
        Teknologi yang terus berkembang, tak lantas membebaskan kita dari berbagai jenis kejahatan di dunia maya atau cybercrime. 
        Pengertian cybercrime adalah sebuah kejahatan menggunakan komputer, Internet, dan sebagainya.
        Umumnya, jenis kejahatan ini dimanfaatkan oleh para pelakunya untuk mendapatkan informasi secara ilegal, memanipulasi data, 
        dan berbagai tindakan kejahatan virtual lainnya guna mendapatkan keuntungan. 
        Terus, apa sih yang dimaksud dengan cybercrime?.
        Oke, jadi Cybercrime adalah uatu bentuk kejahatan virtual dengan memanfaatkan perangkat komputer yang terhubung dengan jaringan Internet. 
        Tindakan tersebut tentunya melanggar hukum, sebab dapat menimbulkan kerugian bagi orang lain.
        Menyadur dari buku Etika Profesi Informatika oleh Muhammad Ridha Albaar, kejahatan siber pertama kali ditemukan pada 1988 dengan istilah cyber attack. 
        Saat itu, seorang mahasiswa berhasil menciptakan sebuah worm atau virus yang dapat menyerang program komputer dan dapat mematikan sekitar 10 persen 
        dari seluruh jumlah komputer di dunia yang terhubung di Internet.
    """
    )

def cybercrime_type():
    import streamlit as st
    
    st.write("# Apa aja sih tipe-tipe Cybercrime?")
    st.markdown(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )

def case_study():
    import streamlit as st
    
    st.write("# Contoh kasus Cybercrime")
    st.markdown(
        """
        Teknologi yang terus berkembang, tak lantas membebaskan kita dari berbagai jenis kejahatan di dunia maya atau cybercrime. 
        Pengertian cybercrime adalah sebuah kejahatan menggunakan komputer, Internet, dan sebagainya.
        Umumnya, jenis kejahatan ini dimanfaatkan oleh para pelakunya untuk mendapatkan informasi secara ilegal, memanipulasi data, 
        dan berbagai tindakan kejahatan virtual lainnya guna mendapatkan keuntungan. 
        Terus, apa sih yang dimaksud dengan cybercrime?.
        Oke, jadi Cybercrime adalah uatu bentuk kejahatan virtual dengan memanfaatkan perangkat komputer yang terhubung dengan jaringan Internet. 
        Tindakan tersebut tentunya melanggar hukum, sebab dapat menimbulkan kerugian bagi orang lain.
        Menyadur dari buku Etika Profesi Informatika oleh Muhammad Ridha Albaar, kejahatan siber pertama kali ditemukan pada 1988 dengan istilah cyber attack. 
        Saat itu, seorang mahasiswa berhasil menciptakan sebuah worm atau virus yang dapat menyerang program komputer dan dapat mematikan sekitar 10 persen 
        dari seluruh jumlah komputer di dunia yang terhubung di Internet.
    """
    )

page_names_to_funcs = {
    "Home": intro,
    "Tipe-tipe Cybercrime": cybercrime_type,
    "Cara menghindari Cybercrime": cybercrime_prevention,
    "Contoh kasus Cybercrime": case_study
}

demo_name = st.sidebar.selectbox("Pilih artikel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
