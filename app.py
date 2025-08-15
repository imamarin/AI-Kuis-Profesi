import streamlit as st
from streamlit_sortables import sort_items

st.set_page_config(page_title="Kuis Drag-and-Drop Profesi", layout="centered")


st.title("Kenan AI - Kuis Profesi: Urutkan Preferensimu!")

st.write("Fun Project: Geser dan urutkan preferensimu dari **paling kamu suka** ke **paling tidak suka**.")

# Pertanyaan dan opsi
questions = [
    {
        "question": "Aktivitas favoritmu?",
        "options": ["Menulis kode", "Membuat desain", "Menganalisis data"],
    },
    {
        "question": "Software favorit?",
        "options": ["VS Code", "Figma", "Excel / Jupyter"],
    },
    {
        "question": "Cara menyelesaikan masalah?",
        "options": ["Buat script", "Visualisasi solusi", "Analisis data"],
    }
]

# Bobot per profesi (dapat dikustom)
profession_map = {
    "Menulis kode": "Programmer",
    "VS Code": "Programmer",
    "Buat script": "Programmer",
    "Membuat desain": "Designer",
    "Figma": "Designer",
    "Visualisasi solusi": "Designer",
    "Menganalisis data": "Data Scientist",
    "Excel / Jupyter": "Data Scientist",
    "Analisis data": "Data Scientist"
}

# Inisialisasi skor
scores = {
    "Programmer": 0,
    "Designer": 0,
    "Data Scientist": 0
}

# Loop drag and drop
for idx, q in enumerate(questions):
    st.subheader(f"{idx+1}. {q['question']}")
    sorted_list = sort_items(
        q["options"], 
        key=f"q_{idx}",
    )
    if sorted_list:
        for rank, item in enumerate(sorted_list):
            profesi = profession_map.get(item)
            if profesi:
                scores[profesi] += 3 - rank  # Skor 3 untuk rank 0, 2 untuk rank 1, dst

@st.dialog("Hasil Kuis")
def vote(result, reason, scores):
    st.success(f"Profesi yang cocok untukmu adalah: **{result}**, {reason}")

    # Menjumlahkan semua skor
    total_score = sum(scores.values())

    #menampilkan persentase skor per profesi
    for profesi, score in scores.items():
        percent = (score / total_score * 100) if total_score > 0 else 0
        st.progress(percent / 100, text=f"{profesi}: {percent:.1f}%")

# Tombol hasil
if st.button("Lihat Hasil"):
    
    # mendapatkan hasil tertinggi
    result = max(scores, key=scores.get)

    # Tambahan pesan
    messages = {
        "Programmer": "Kamu menyukai logika, sistem, dan solusi berbasis teknologi.",
        "Designer": "Kamu memiliki kepekaan estetika dan suka menyampaikan pesan secara visual.",
        "Data Scientist": "Kamu senang menemukan makna dari data dan pola tersembunyi."
    }

    # Menampilkan dialog hasil
    vote(result, messages[result], scores)

        

