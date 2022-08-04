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
    
        st.write(
        """
        1.	Gunakan layanan pengamanan internet seperti defender yang dapat melindungi komputer dari malware 
        (sebuah perangkat lunak yang dibuat untuk masuk , sistem computer atau server tanpa di ketahui dengan tujuan 
        untuk menginfeksi dan merusak) dan membantu menjaga data pribadi serta informasi finansial ketika kita sedang online
        2.	Gunakan password yang kuat, megubah password secara berkala dan gunakanlah kombinasi huruf, angka, dan simbol serta panjang
        password yang lebih dari 13 karakter
        3.	Usahakan untuk selalu memperbaharui software atau perangkat lunak karena penting untuk operasi sistem dan keamanan perangkat lunak.
        4.	Mengatur pengaturan media sosial kita, gunakan 2 Factor Authentication dan tetap menjaga infromasi pribadi karena mereka dapat mengambil 
        beberapa informasi pribadi kita di media sosial. Kita harus juga bijak dalam menggunakan media sosial
        5.	Gunakan kata sandi jaringan yang kuat, boleh menggunakan VPN ketika menggunakan jaringan public agar IP address yang kita gunakan tidak terlihat.
        6.	Diksusikan dengan anak-anak ketika mereka menggunakan internet bagaimana cara mereka mematikan saluran yang membuat 
        mereka tidak nyaman, seperti pelecehan, pengungtit, atau bullying (gertakan).
        7.	Jika kamu melaukan bisnis perdagangan dan mengetahui ada yang mencurigakan di akun web penjualanmu segera lakukan pengubahan kata sandi 
        dan segera lakukan pengecekan terhadap semua sistem bisnismu.
        8.	Pencurian identitas terjadi ketika seseornag secara tidak sengaja memperoleh data pribadi kita dan orang akan menggunakan data 
        tersebut untuk penipuan untuk keuntungan ekonomi jadi jangan pernah membuka lampiran di email spam karena 
        dapat diduga itu adalah link untuk serangan sebuah malware
"""
    )

   
def cybercrime_type():
    import streamlit as st
    
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
