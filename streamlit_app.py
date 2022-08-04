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
   
