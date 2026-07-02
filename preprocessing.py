import re

ABBREV_DICT = {
    #Kata ganti
    'yg'             : 'yang',
    'sy'             : 'saya',
    'gua'            : 'saya',
    'gue'            : 'saya',
    'gw'             : 'saya',
    'ane'            : 'saya',
    'sayaa'          : 'saya',
    'lu'             : 'kamu',
    'lo'             : 'kamu',
    'elu'            : 'kamu',
    'km'             : 'kamu',
    'kmu'            : 'kamu',

    #Kata negasi
    'ga'             : 'tidak',
    'gak'            : 'tidak',
    'gk'             : 'tidak',
    'tdk'            : 'tidak',
    'nggak'          : 'tidak',
    'ngga'           : 'tidak',
    'ngak'           : 'tidak',
    'nggk'           : 'tidak',
    'kaga'           : 'tidak',
    'kagak'          : 'tidak',
    'engga'          : 'tidak',
    'g'              : 'tidak',
    'nga'            : 'tidak',
    'gabisa'         : 'tidak bisa',
    'gamau'          : 'tidak mau',
    'gaada'          : 'tidak ada',
    'gada'           : 'tidak ada',
    'gatau'          : 'tidak tahu',
    'gautau'         : 'tidak tahu',
    'gasuka'         : 'tidak suka',
    'gasih'          : 'tidak sih',
    'gaussah'        : 'tidak usah',
    'gausah'         : 'tidak usah',

    #Kata sambung dan partikel
    'tp'             : 'tapi',
    'tpi'            : 'tapi',
    'jg'             : 'juga',
    'jga'            : 'juga',
    'kl'             : 'kalau',
    'klo'            : 'kalau',
    'klu'            : 'kalau',
    'klw'            : 'kalau',
    'kalo'           : 'kalau',
    'aja'            : 'saja',
    'ajah'           : 'saja',
    'aj'             : 'saja',
    'doang'          : 'saja',
    'sm'             : 'sama',
    'dgn'            : 'dengan',
    'dg'             : 'dengan',
    'pd'             : 'pada',
    'pdhl'           : 'padahal',
    'pdahal'         : 'padahal',
    'pdhal'          : 'padahal',
    'n'              : 'dan',

    #Kata sebab
    'krn'  : 'karena', 'karna': 'karena', 'krna' : 'karena',

    #Kata kondisi
    'klo'  : 'kalau',  'klu'  : 'kalau',  'klw'  : 'kalau',
    'kalo' : 'kalau',

    #Kata penekanan
    'bgt'  : 'banget', 'bngt' : 'banget',
    'sgt'  : 'sangat',

    #Kata kerja dan sifat tidak baku
    'pake'           : 'pakai',
    'pke'            : 'pakai',
    'pakek'          : 'pakai',
    'pesen'          : 'pesan',
    'psen'           : 'pesan',
    'mesen'          : 'pesan',
    'mesan'          : 'pesan',
    'nunggu'         : 'menunggu',
    'nungguin'       : 'menunggu',
    'nyari'          : 'mencari',
    'dapet'          : 'dapat',
    'dpet'           : 'dapat',
    'dpt'            : 'dapat',
    'dpat'           : 'dapat',
    'ngerti'         : 'mengerti',
    'ngasih'         : 'memberikan',
    'ngambil'        : 'mengambil',
    'ngeluh'         : 'mengeluh',
    'ngomel'         : 'marah',
    'ngejar'         : 'mengejar',
    'denger'         : 'mendengar',
    'inget'          : 'ingat',
    'liat'           : 'lihat',
    'nyoba'          : 'mencoba',
    'nanya'          : 'bertanya',
    'dateng'         : 'datang',
    'naek'           : 'naik',
    'bilng'          : 'bilang',
    'masi'           : 'masih',
    'nerima'         : 'menerima',
    'nolak'          : 'menolak',
    'batalin'        : 'membatalkan',
    'adain'          : 'mengadakan',
    'naikin'         : 'menaikkan',
    'matiin'         : 'mematikan',
    'mantab'         : 'mantap',
    'mantab'         : 'mantap',
    'nyaaa'          : 'nya',
    'nyaa'           : 'nya',
    'ny'             : 'nya',
    'bgt'            : 'banget',
    'bngt'           : 'banget',
    'bgttt'          : 'banget',
    'bener'          : 'benar',
    'sampe'          : 'sampai',
    'sampek'         : 'sampai',
    'smpe'           : 'sampai',
    'tau'            : 'tahu',
    'deket'          : 'dekat',
    'cepet'          : 'cepat',
    'emang'          : 'memang',
    'emng'           : 'memang',
    'kayak'          : 'seperti',
    'kyk'            : 'seperti',
    'kaya'           : 'seperti',
    'nih'            : 'ini',
    'inii'           : 'ini',
    'tuh'            : 'itu',
    'gitu'           : 'begitu',
    'gini'           : 'begini',
    'gtu'            : 'begitu',
    'gni'            : 'begini',
    'ok'             : 'oke',
    'tetep'          : 'tetap',
    'smua'           : 'semua',
    'slalu'          : 'selalu',
    'skli'           : 'sekali',
    'gede'           : 'besar',
    'dikit'          : 'sedikit',
    'byk'            : 'banyak',
    'lbh'            : 'lebih',
    'cuman'          : 'hanya',
    'cmn'            : 'hanya',
    'cm'             : 'hanya',
    'mnding'         : 'mending',
    'kesel'          : 'kesal',
    'seneng'         : 'senang',
    'pengen'         : 'ingin',
    'mo'             : 'mau',
    'malem'          : 'malam',
    'lelet'          : 'lambat',
    'lemot'          : 'lambat',
    'bs'             : 'bisa',
    'cpt'            : 'cepat',
    'jd'             : 'jadi',
    'knp'            : 'kenapa',
    'knpa'           : 'kenapa',
    'apk'            : 'aplikasi',
    'apknya'         : 'aplikasinya',
    'apl'            : 'aplikasi',
    'apps'           : 'aplikasi',
    'nopol'          : 'nomor polisi',
    'nomer'          : 'nomor',
    'cs'             : 'layanan pelanggan',
    'yah'            : 'ya',
    'lohh'           : 'loh',
    'ehh'            : 'eh',
    'poto'           : 'foto',
    'plis'           : 'tolong',
    'tlg'            : 'tolong',
    'tlong'          : 'tolong',
    'woi'            : 'hei',
    'donk'           : 'dong',
    'ojol'           : 'ojek online',
    'otw'            : 'dalam perjalanan',
    'grabb'          : 'grab',
    'grb'            : 'grab',
    'grap'           : 'grab',
    'maxsim'         : 'maxim',
    'maxin'          : 'maxim',
    'gojk'           : 'gojek',

    #Istilah aplikasi
    'apk'  : 'aplikasi', 'apli': 'aplikasi',

    #Kata perbandingan
    'lbh'  : 'lebih',

    #Keterangan waktu
    'udah'           : 'sudah',
    'udh'            : 'sudah',
    'dah'            : 'sudah',
    'ud'             : 'sudah',
    'uda'            : 'sudah',
    'dh'             : 'sudah',
    'blm'            : 'belum',
    'lg'             : 'lagi',
    'lgi'            : 'lagi',
    'lag'            : 'lagi',
    'dl'             : 'dulu',
    'ntr'            : 'nanti',
    'nnti'           : 'nanti',
    'trus'           : 'terus',
    'trs'            : 'terus',
    'teruss'         : 'terus',
    'skrg'           : 'sekarang',
    'skrng'          : 'sekarang',
    'taun'           : 'tahun',
    'slama'          : 'selama',
    'lgsg'           : 'langsung',
    'stelah'         : 'setelah',


    #Kata depan
    'dr'             : 'dari',
    'dri'            : 'dari',
    'd'              : 'di',    
    'dlm'            : 'dalam',
    'dri'            : 'dari',
    'jln'            : 'jalan',
    'rmh'            : 'rumah',
    'ank'            : 'anak',

    #Jumlah dan kualitas
    'bnyk' : 'banyak', 'bnyak': 'banyak',
    'msh'  : 'masih',  'msih' : 'masih',
    'krg'  : 'kurang',
    'lncar': 'lancar',

    #Kata tanya
    'gmn'  : 'bagaimana', 'gimana': 'bagaimana', 'gmana' : 'bagaimana',
    'knp'  : 'kenapa',    'knpa'  : 'kenapa',

    #Kata untuk
    'utk'  : 'untuk',  'tuk'  : 'untuk',

    #Kata bisa
    'bs'   : 'bisa',

    #Tambahan dari hasil cek dataset
    'mengasih'       : 'memberikan',
    'bnget'          : 'banget',
    'yaampun'        : 'astaga',
    'bnyk'           : 'banyak',
    'bnyak'          : 'banyak',
    'buset'          : 'astaga',
    'gercep'         : 'gerak cepat',
    'enggak'         : 'tidak',
    'apaan'          : 'apa',
    'laknat'         : 'hina',
    'jdi'            : 'jadi',
    'yaa'            : 'ya',
    'yaaa'           : 'ya',
    'yaaaa'          : 'ya',
    'dlu'            : 'dulu',
    'utk'            : 'untuk',
    'ujan'           : 'hujan',
    'jgn'            : 'jangan',
    'jngn'           : 'jangan',
    'jgnan'          : 'jangan',
    'jngnan'         : 'jangan',
    'php'            : 'memberi harapan palsu',
    'org'            : 'orang',
    'umr'            : 'upah minimum regional',
    'sdh'            : 'sudah',
    'krn'            : 'karena',
    'karna'          : 'karena',
    'krna'           : 'karena',
    'fungsifbs'      : 'fungsi tidak bisa',
    'hujanzgak'      : 'hujan tidak',
    'ribukadang'     : 'ribu kadang',
    'ribukami'       : 'ribu kami',
    'hemattidak'     : 'hemat tidak',
    'bpk'            : 'bapak',
    'telfon'         : 'telepon',
    'telpon'         : 'telepon',
    'tlfn'           : 'telepon',
    'nyantai'        : 'santai',
    'sya'            : 'saya',
    'ramahramah'     : 'ramah-ramah',
    'nyantai'        : 'santai',

    #Variasi kata terima kasih
    'makasih'        : 'terima kasih',
    'mksh'           : 'terima kasih',
    'mksih'          : 'terima kasih',
    'trmksh'         : 'terima kasih',
    'trimksh'        : 'terima kasih',
    'trims'          : 'terima kasih',
    'trimakasih'     : 'terima kasih',
    'terimakasih'    : 'terima kasih',
    'ksh'            : 'kasih',
    'dikasi'         : 'dikasih',
    'kasi'           : 'kasih',

    #Ekspresi 
    'donk' : 'dong',
    'woi'  : 'hei',
    'wkwk'           : '',
    'wkwkwk'         : '',
    'hehe'           : '',
    'hehehe'         : '',
    'haha'           : '',

    #Istilah aplikasi
    'maxsim': 'maxim',
    'maxin' : 'maxim',
    'gojk'  : 'gojek',
    'grb'   : 'grab',
    'ojol'  : 'ojek online',
    'goride': 'gojek',
    'grabsemoga'     : 'grab semoga',
    'gojekgocar'     : 'gojek gocar',

    #Typo lain
    'cancle': 'cancel',
    'poto'  : 'foto',
}


CONJUNCTIONS_TO_SPLIT = [
    "tapi",
    "sehingga",
    "dengan",
    "karena",
    "namun",
    "ingin"
]


CONJUNCTIONS_TO_SPLIT = [
    "tapi",
    "sehingga",
    "dengan",
    "karena",
    "namun",
    "ingin"
]

def normalize_text(text: str) -> str:
    """
    Normalisasi teks ulasan.

    Tahapan:
    1. Lowercase
    2. Hapus URL
    3. Hapus Email
    4. Pisah kata sambung
    5. Ekspansi reduplikasi (driver2 -> driver driver)
    6. Normalisasi angka
    7. Pisahkan angka dan huruf
    8. Normalisasi singkatan/slang
    9. Reduksi huruf berulang
    10. Hapus karakter non alfanumerik
    """

    if not isinstance(text, str):
        return ""

    text = text.lower().strip()

    if text == "":
        return ""

    # ======================================================
    # Hapus URL
    # ======================================================
    text = re.sub(
        r'https?://\S+|www\.\S+',
        ' ',
        text
    )

    # ======================================================
    # Hapus Email
    # ======================================================
    text = re.sub(
        r'\S+@\S+',
        ' ',
        text
    )

    # ======================================================
    # Pisahkan kata sambung
    # ======================================================
    for conj in CONJUNCTIONS_TO_SPLIT:

        text = re.sub(
            r'([a-z]{3,})(' + conj + r')(?=[a-z]{2,}|\s|$)',
            r'\1 \2',
            text
        )

    # ======================================================
    # driver2 -> driver driver
    # ======================================================
    def expand_redup(match):

        kata = match.group(1)

        if kata.isdigit():
            return match.group(0)

        return kata + " " + kata

    text = re.sub(
        r'\b([a-z]{2,})(2)\b',
        expand_redup,
        text
    )

    # ======================================================
    # Normalisasi angka
    # ======================================================
    text = re.sub(r'(\d+)\s*rb\b', r'\1 ribu', text)
    text = re.sub(r'(\d+)\s*jt\b', r'\1 juta', text)
    text = re.sub(r'(\d+)\s*k\b', r'\1 ribu', text)
    text = re.sub(r'(\d+)x\b', r'\1 kali', text)
    text = re.sub(r'(\d+)\s*mnt\b', r'\1 menit', text)
    text = re.sub(r'(\d+)\s*an\b', r'\1 an', text)

    # ======================================================
    # Pisahkan angka dan huruf
    # ======================================================
    text = re.sub(
        r'(\d)([a-z])',
        r'\1 \2',
        text
    )

    text = re.sub(
        r'([a-z])(\d)',
        r'\1 \2',
        text
    )

    # ======================================================
    # Normalisasi kamus
    # ======================================================
    hasil = []

    for token in text.split():

        clean = re.sub(
            r'[^a-z0-9]',
            '',
            token
        )

        if clean in ABBREV_DICT:
            hasil.append(
                ABBREV_DICT[clean]
            )
        else:
            hasil.append(token)

    text = " ".join(hasil)

    # ======================================================
    # Reduksi huruf berulang
    # ======================================================
    text = re.sub(
        r'([a-z])\1{2,}',
        r'\1',
        text
    )

    # ======================================================
    # Hapus karakter selain huruf, angka dan spasi
    # ======================================================
    text = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        text
    )

    # ======================================================
    # Rapikan spasi
    # ======================================================
    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()

    return text


def preprocess_review(text: str) -> str:
    """
    Pipeline preprocessing yang sama dengan notebook.
    """

    if text is None:
        return ""

    text = str(text)

    text = text.strip()

    if text == "":
        return ""

    # Sama seperti notebook
    text = normalize_text(text)

    text = text.strip()

    return text