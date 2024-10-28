import requests
from googlesearch import search
import fitz
import docx


def cari_dan_unduh_materi(query, jumlah_hasil=5):
    hasil_pencarian = []
    for hasil in search(query, num_results=jumlah_hasil):
        if hasil.endswith(".pdf") or hasil.endswith(".docx"):
            print(f"Mengunduh: {hasil}")
            try:
                # mengunduh file(pdf/docx)
                response = requests.get(hasil)
                if hasil.endswith(".pdf"):
                    nama_file = "materi.pdf"
                    with open(nama_file, "wb") as f:
                        f.write(response.content)
                    print('Konten PDF: ')
                elif hasil.endswith('.docx'):
                    nama_file = "materi.docx"
                    with open(nama_file, "wb") as f:
                        f.write(response.content)
                    print('Konten DOCX: ')
                    baca_docx(nama_file)
            except Exception as e:
                print(f"Terjadi kesalahan saat mengunduh hasil: {e}")
    return hasil_pencarian


def baca_pdf(nama_file):
    with fitz.open(nama_file) as pdf:
        for halaman in pdf:
            print(halaman.get_text())


def baca_docx(nama_file):
    dokumen = docx.Document(nama_file)
    for paragraf in dokumen.paragraphs:
        print(paragraf.text)

query = input("Masukkan materi yang ingin Anda cari (misal: 'materi belajar Python'): ")
query += " filetype:pdf OR filetype:docx"
cari_dan_unduh_materi(query)