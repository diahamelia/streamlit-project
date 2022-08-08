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
        Seperti yang kita ketahui bahwa serangan Cybercrime bisa saja masuk kedalam perangkat kita, juga dari diri kita sendiri
        Maka, langkah preventif yang dapat dilakukan adalah diantaranya:
        1. Selalu menginstall software terbaru, hal ini dilakukan agar tidak ada celah untuk serangan yang masuk kedalam sistem kita
        2. Menggunakan defender bawaan dari operating system
        3. Tidak sembarangan membuka tautan dari email, karena bisa saja di dalam lampiran email tersebut terdapat file malware
        4. Tidak sembarangan meng-klik link yang ada dari email, pastikan nama pengirim, domain email, apakah ada tulisan yang typo telah dicek
        karena kalau sampai ada salah satunya, maka wajib berhati-hati
        5. Menggunakan password yang kuat, indikator password yang kuat adalah password dengan panjang karakter lebih dari 12 dan terdiri
        dari huruf kapital, huruf kecil, angka dan symbol
        6. Baca syarat dan ketentuan data privasi ketika mendaftar dalam layanan web
    """
    )

def cybercrime_type():
    import streamlit as st
    
    st.write("# Apa aja sih tipe-tipe Cybercrime?")
    st.markdown(
        """
        1. Phishing
        Phising adalah contoh cyber crime yang bertujuan untuk mencuri informasi dan data pribadi dari email, telepon, pesan teks atau link palsu 
        yang mengaku sebagai instansi atau pihak-pihak tertentu. Cara kerja phishing yaitu mengelabui target dengan tipuan yang seolah terlihat normal
        padahal mereka tidak sadar bahwa data pribadi miliknya sedang dicuri. Pelaku phishing mengincar data-data sensitif korban, seperti kata sandi, 
        informasi kartu kredit, alamat email, dan one-time password (OTP). Data yang dicuri digunakan untuk tindak kejahatan seperti pencurian, 
        penyalahgunaan identitas pribadi, hingga pemerasan uang.
        
        2. Spoofing
        Spoofing adalah penyamaran informasi seakan-akan berperan sebagai pihak berwenang, seperti dari bank atau pemerintah untuk tujuan kejahatan siber.
        Mirip seperti phising yang mencoba mencuri data korban, bedanya, spoofing tak hanya mencuri data, tapi dalam beberapa kasus juga mengirimkan malware 
        berbahaya ke perangkat atau website korban. Ada berbagai jenis spooofing, mulai dari identity spoofing, IP spoofing, DNS spoofing, hingga website spoofing.
        
        3. Cracking
        Cracking adalah percobaan memasuki sistem komputer secara paksa dengan meretas sistem keamanan software atau komputer untuk tujuan ilegal yang mengarah 
        ke kriminalisme. Pelaku cracking melakukan aksinya untuk mencuri, melihat, memanipulasi data hingga penanaman malware. Ada berbagai jenis cracking 
        yang sering terjadi, misalnya password cracking, software cracking, dan network cracking. Berbagai jenis serangan cracking bisa kamu hindari misalnya dengan 
        membuat kombinasi password unik, menggunakan VPN, mengunjungi situs yang sudah menggunakan HTTPS, dan menghindari klik tautan atau iklan di internet 
        Jika kamu memiliki website bisnis, terutama yang menyimpan data pelanggan, sebaiknya kamu melakukan penetration testing untuk menguji tingkat keamanan dari 
        kejahatan cracking.
        
        4. Serangan Ransomware
        Ransomware adalah tipe malware yang menargetkan perangkat keras untuk mengambil informasi berharga dari targetnya kemudian mengenkripsi dan mengunci file 
        tersebut. Jika ingin membuka atau mengakses kembali data-data tersebut, pelaku akan meminta uang tebusan ke korban. Apabila korban tidak mengabulkan permintaan
        tersebut, pelaku tak segan mengancam akan membuat data tidak bisa digunakan lagi. Jenis cyber crime ini sering mengincar pengguna teknologi rumahan 
        dengan tingkat melek teknologi yang masih kurang. Tujuan akhir serangan ransomware adalah untuk memeras korban untuk membayar sejumlah uang untuk dapat 
        mengakses file yang telah dienkripsi.
        
        5. Serangan DDoS
        Distributed Denial of Service (DDoS) adalah contoh cybercrime dengan membuat lalu lintas server berjalan dengan beban berat hingga tidak bisa menampung koneksi 
        dari user lain/overload. Serangan yang populer dilakukan oleh hacker ini dibuat dengan cara mengirimkan request ke server secara terus menerus dengan transaksi 
        data yang besar. Teknik penyerangan DDoS biasanya dilaksanakan dengan banyak cara, seperti virus dan kumpulan bot yang disisipkan pada malware yang disebut botnet.
        
        6. Injeksi SQL
        Injeksi SQL adalah teknik serangan injeksi kode dengan memanfaatkan celah keamanan yang terjadi pada layer basis data sebuah aplikasi. 
        Contoh cybercrime ini merupakan ancaman nomor satu terhadap keamanan aplikasi web. Hal ini umumnya terjadi akibat pengembang aplikasi tidak mengimplementasikan 
        filter terhadap beberapa metakarakter yang digunakan dalam sintaks SQL, sehingga penyerang dapat menginput metakarakter tersebut menjadi instruksi pada aplikasi 
        untuk mengakses database. Serangan SQL juga dapat terjadi jika backend tidak melakukan setting Web Application Firewall (WAF) atau Intrusion Prevention System (IPS)
        di arsitektur jaringan dengan baik, sehingga database bisa diakses langsung dari celah kerawanan yang ditemukan.
        
        7. Carding
        Carding adalah kejahatan melakukan pencurian data informasi kartu kredit milik orang lain. Data tersebut kemudian digunakan oleh pelaku untuk melakukan transaksi 
        atau mencairkan saldo limit kartu ke rekening mereka. Ada dua kategori carding, pertama adalah Card Present, yaitu proses pencurian data dilakukan menggunakan card 
        skimmer mesin EDC yang ada di kasir/tempat komersial. Kedua adalah Card not Present, yaitu pencurian data menggunakan akses internet, biasanya menggunakan email 
        phising atau hacking untuk mendapatkan data-data pemilik kartu kredit.
        
        8. Peretasan Situs dan Email
        Sesuai dengan namanya, kejahatan siber yang paling populer ini dilakukan dengan meretas sebuah situs atau email korban serta mengubah tampilannya. 
        Ya, tanda yang bisa kamu lihat bila sebuah website diretas adalah tampilannya yang mendadak berubah. Misalnya halaman situs yang tidak biasanya, muncul iklan tidak jelas, 
        bahkan data situs bisa dicuri tanpa disadari. Beberapa cara untuk menghindari peretasan website, misalnya melakukan backup secara berkala, menggunakan SSL, 
        dan memilih layanan cloud hosting terpercaya seperti Dewaweb yang telah tersertifikasi keamanan internasional ISO 270001.
        
        9. Penipuan OTP
        OTP atau One Time-Password adalah kode yang bersifat sementara sebagai password sekali pakai untuk melakukan proses verifikasi di aplikasi smartphone.
        Karena kepopulerannya makin meningkat, ancaman pelaku kejahatan siber yang mencoba mencuri OTP juga kian merebak. Penipuan OTP dimanfaatkan untuk berbagai tindak kejahatan 
        seperti membahayakan akun dan melakukan transaksi keuangan yang tidak sah. Agar kamu terhindar dari penipuan OTP, jangan pernah membagikan kode OTP kepada siapapun, 
        baik orang yang dikenal atau tidak dikenal. Selain itu, aktifkan fitur two factor authentication dan selalu waspadai link/tautan yang tidak jelas.
        
        10. Data Forgery atau Pemalsuan Data
        Data forgery adalah tindakan memalsukan data dokumen penting yang tersimpan sebagai scriptless document melalui internet. Dokumen-dokumen ini biasanya dimiliki oleh institusi 
        atau lembaga yang memiliki situs berbasis web database. Pemalsuan data biasanya ditujukan pada dokumen-dokumen e-commerce dengan cara membuat seolah-olah terjadi “salah ketik”, 
        yang pada akhirnya akan menguntungkan pelaku karena korban akan memasukkan data pribadi dan nomor kartu kredit yang dapat disalahgunakan
        
        11. Cyber Espionage
        Cyber espionage adalah kejahatan siber yang memanfaatkan internet dengan memasuki sistem jaringan komputer untuk memata-matai target tertentu. Kejahatan ini biasanya ditujukan 
        kepada kompetitor, lawan politik, atau pejabat negara yang dokumen dan data-data pentingnya tersimpan dalam suatu sistem yang terkomputerisasi. Cyber espionage biasa dilakukan 
        dengan memanfaatkan spyware, yaitu software yang diinstal secara diam-diam oleh hacker untuk memantau perilaku online korban. Dengan begitu, semua aktivitas dan data penting 
        bisa diakses tanpa disadari.
        
        12. Pemalsuan Identitas
        Pemalsuan identitas termasuk salah satu contoh cybercrime yang harus diwaspadai. Pelaku memanfaatkan identitas palsu secara ilegal untuk melakukan tujuan kriminal.
                
        13. Cyber Terrorism
        Cyber terrorism adalah jenis kejahatan siber yang merugikan negara, bahkan mengancam keselamatan warga dan stakeholder yang mengatur jalannya pemerintahan. 
        Aktivitas terorisme siber merujuk pada serangan terhadap komputer, jaringan, dan sistem informasi dengan tujuan mengintimidasi, menekan pemerintah, atau untuk kepentingan politik tertentu.
    """
    )
    
def case_study():
    import streamlit as st
    
    st.write("# Contoh kasus Cybercrime")
    st.markdown(
        """
        Kalian tau gak sih .
    """
    )

page_names_to_funcs = {
    "Home": intro,
    "Tipe-tipe Cybercrime": cybercrime_type,
    "Cara menghindari Cybercrime": cybercrime_prevention,
    "Contoh kasus Cybercrime": case_study,
    
}

demo_name = st.sidebar.selectbox("Pilih artikel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
