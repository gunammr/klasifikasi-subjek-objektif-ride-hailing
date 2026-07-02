import re

ABBREV_DICT = {

    'yg'   : 'yang',
    'sy'   : 'saya',   'sya'  : 'saya',
    'gue'  : 'saya',   'gw'   : 'saya',   'ane': 'saya',
    'lo'   : 'kamu',   'lu'   : 'kamu',   'elu': 'kamu',

    # ── Negasi ──────────────────────────────────
    'ga'   : 'tidak',  'gak'  : 'tidak',  'gk' : 'tidak',
    'tdk'  : 'tidak',  'nggak': 'tidak',  'ngga': 'tidak',
    'engga': 'tidak',  'enggak': 'tidak', 'g'  : 'tidak',
    'gada' : 'tidak ada',
    'gabisa': 'tidak bisa',
    'kagak': 'tidak',  'kaga' : 'tidak',

    # ── Konjungsi/Partikel ───────────────────────
    'tp'   : 'tapi',   'tpi'  : 'tapi',
    'jg'   : 'juga',
    'jgn'  : 'jangan', 'jngan': 'jangan', 'jgnan': 'jangan',

    # ── Kausal ──────────────────────────────────
    'krn'  : 'karena', 'karna': 'karena', 'krna' : 'karena',

    # ── Kondisional ─────────────────────────────
    'klo'  : 'kalau',  'klu'  : 'kalau',  'klw'  : 'kalau',
    'kalo' : 'kalau',

    # ── Intensifier ─────────────────────────────
    'bgt'  : 'banget', 'bngt' : 'banget',
    'sgt'  : 'sangat',

    # ── Kata Kerja/Sifat Tidak Baku ─────────────
    'pake' : 'pakai',  'pke'  : 'pakai',
    'pesen': 'pesan',
    'poto' : 'foto',
    'dapet': 'dapat',  'dpat' : 'dapat',  'dpt'  : 'dapat',
    'nyari': 'mencari',
    'nunggu': 'menunggu', 'nungguin': 'menunggu',
    'bener': 'benar',
    'kyak' : 'seperti','kayak': 'seperti',
    'cancle': 'cancel',
    'sampe': 'sampai', 'ampe' : 'sampai',
    'tau'  : 'tahu',
    'nih'  : 'ini',    'neh'  : 'ini',
    'tuh'  : 'itu',
    'ngomong': 'bicara',
    'ngomel' : 'marah',
    'ngasih' : 'memberi',
    'ngambil': 'mengambil',

    # ── Aplikasi ────────────────────────────────
    'apk'  : 'aplikasi', 'apli': 'aplikasi',

    # ── Komparatif ──────────────────────────────
    'lbh'  : 'lebih',

    # ── Waktu/Aspek ─────────────────────────────
    'sdh'  : 'sudah',  'udah' : 'sudah',  'udh'  : 'sudah',
    'blm'  : 'belum',
    'lg'   : 'lagi',
    'dl'   : 'dulu',
    'skrg' : 'sekarang', 'skrang': 'sekarang',
    'ntr'  : 'nanti',  'nnti' : 'nanti',

    # ── Preposisi ───────────────────────────────
    'dr'   : 'dari',   'dri'  : 'dari',
    'd'    : 'di',
    'dg'   : 'dengan', 'dgn'  : 'dengan',
    'pd'   : 'pada',

    # ── Kuantitas/Kualitas ──────────────────────
    'bnyk' : 'banyak', 'bnyak': 'banyak',
    'msh'  : 'masih',  'msih' : 'masih',
    'krg'  : 'kurang',
    'lncar': 'lancar',

    # ── Pertanyaan ──────────────────────────────
    'gmn'  : 'bagaimana', 'gimana': 'bagaimana',
    'knp'  : 'kenapa',    'knpa'  : 'kenapa',

    # ── Untuk ───────────────────────────────────
    'utk'  : 'untuk',  'tuk'  : 'untuk',

    # ── Bisa ────────────────────────────────────
    'bs'   : 'bisa',

    # ── Lain-lain ───────────────────────────────
    "mengasih": "memberikan",
    "yaampun": "astaga",
    "bnyk": "banyak",
    "buset": "astaga",
    "yq": "beberapa",
    "gercep": "cekatan",
    "enggak": "tidak",
    "apaan": "apa",
    "laknat": "hina",
    "jdi": "jadi",
    "yaa": "ya",
    "dlu": "dulu",
    "lEk": "",
    "bin": "dan",
    "utk": "untuk",
    "ujan": "hujan",
    "apakah": "aplikasi",
    "jgn": "jangan",
    "php": "memberi harapan",
    "org": "orang",
    "umr": "upah minimum regional",
    "sdh": "sudah",
    "krn": "karena",
    "fungsifbs": "fungsi tidak bisa",
    "hujanzgak": "hujan tidak",
    "nyantai": "santai",
    "kendarijangan": "kendari jangan",
    "ribukadang": "ribu kadang",
    "ribukami": "ribu kami",
    "bpk": "bapak",
    "hemattidak": "hemat tidak",
    "telfon": "telepon",
    "gmn": "gimana",
    "ramahramah": "ramah-ramah",
    "sya": "saya",
    "pacar": "gocar",
    "grabsemoga": "grab",
    'sm'   : 'sama',
    'aja'  : 'saja',
    'org'  : 'orang',
    'bln'  : 'bulan',
    'thn'  : 'tahun',
    'mnt'  : 'menit',
    'pdahal': 'padahal', 'pdhl' : 'padahal',
    'jmpt' : 'jemput',
    'ny'   : 'nya',
    'dtg'  : 'datang',
    'bkn'  : 'bukan',
    'trs'  : 'terus',  'truss': 'terus',
    'tlong': 'tolong', 'tlg'  : 'tolong',
    'mnta' : 'minta',
    'smg'  : 'semoga',
    'ckp'  : 'cukup',
    'hrus' : 'harus',  'haruss': 'harus',
    'cmn'  : 'cuma',   'cman' : 'cuma',
    'ok'   : 'oke',
    'yaa'  : 'ya',     'yaaa' : 'ya',
    'ky'   : 'seperti', 'kayaknya': 'sepertinya',
    'kntong': 'kantong', 'brsaing': 'bersaing',
    'sb'   : 'sebab',
    'jkt'  : 'jakarta',

    # ── Terima Kasih (berbagai variasi) ─────────
    'makasih'     : 'terima kasih',
    'mksh'        : 'terima kasih',
    'mksih'       : 'terima kasih',
    'trmksh'      : 'terima kasih',
    'trimksh'     : 'terima kasih',
    'trims'       : 'terima kasih',
    'trimakasih'  : 'terima kasih',
    'terimakasih' : 'terima kasih',

    # ── Ekspresi/Slang ──────────────────────────
    'donk' : 'dong',
    'woi'  : 'hei',

    # ── Nama Aplikasi (typo) ─────────────────────
    'maxsim': 'maxim',
    'maxin' : 'maxim',
    'gojk'  : 'gojek',
    'grb'   : 'grab',
    'ojol'  : 'ojek online',
    'goride': 'gojek',

    # ── Typo lainnya ─────────────────────────────
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


def normalize_text(text: str):

    text = str(text)

    # ===================================================
    # Lowercase
    # ===================================================
    text = text.lower().strip()

    # ===================================================
    # Hapus URL
    # ===================================================
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # ===================================================
    # Hapus Email
    # ===================================================
    text = re.sub(r'\S+@\S+', ' ', text)

    # ===================================================
    # Pisahkan kata sambung yang menempel
    # contoh:
    # baiktapi -> baik tapi
    # ===================================================
    for conj in CONJUNCTIONS_TO_SPLIT:

        text = re.sub(
            r'([a-z]{3,})(' + conj + r')(?=[a-z]{2,}|\s|$)',
            r'\1 \2',
            text
        )

    # ===================================================
    # driver2 -> driver driver
    # ===================================================
    text = re.sub(
        r'\b([a-z]{2,})(2)\b',
        lambda m: m.group(1) + " " + m.group(1),
        text
    )

    # ===================================================
    # Normalisasi angka
    # ===================================================
    text = re.sub(r'(\d+)\s*rb\b', r'\1 ribu', text)
    text = re.sub(r'(\d+)\s*jt\b', r'\1 juta', text)
    text = re.sub(r'(\d+)\s*k\b', r'\1 ribu', text)
    text = re.sub(r'(\d+)x\b', r'\1 kali', text)
    text = re.sub(r'(\d+)\s*mnt\b', r'\1 menit', text)
    text = re.sub(r'(\d+)\s*an\b', r'\1 an', text)

    # ===================================================
    # Pisahkan angka dan huruf
    # ===================================================
    text = re.sub(r'(\d)([a-z])', r'\1 \2', text)
    text = re.sub(r'([a-z])(\d)', r'\1 \2', text)

    # ===================================================
    # Hapus karakter selain huruf dan angka
    # ===================================================
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # ===================================================
    # Reduksi huruf berulang
    # contoh:
    # baguuuusss -> bagus
    # cepettt -> cepet
    # makasiiihhh -> makasih
    # ===================================================
    text = re.sub(r'(.)\1{2,}', r'\1', text)

    # ===================================================
    # Rapikan spasi
    # ===================================================
    text = re.sub(r'\s+', ' ', text).strip()

    # ===================================================
    # Normalisasi berdasarkan kamus
    # ===================================================
    words = []

    for word in text.split():

        word = ABBREV_DICT.get(word, word)

        words.append(word)

    text = " ".join(words)

    # ===================================================
    # Rapikan kembali spasi
    # ===================================================
    text = re.sub(r'\s+', ' ', text).strip()

    return text