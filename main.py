# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import joblib
import streamlit as st

# ======================
#  Fungsi pendukung sama seperti waktu training
# ======================

def clean_sequence(seq: str) -> str:
    seq = str(seq).upper().strip()
    # buang tanda < > kalau masih ada
    seq = seq.replace("<", "").replace(">", "")
    return seq

def get_kmers(seq, k=3):
    seq = clean_sequence(seq)
    if len(seq) < k:
        return []
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def kmer_analyzer(seq):
    return get_kmers(seq, k=3)  # k harus sama dengan saat training


# ======================
#  Load model
# ======================

@st.cache_resource
def load_model():
    model = joblib.load("dna_classifier_pipeline.joblib")
    return model

model = load_model()


# ======================
#  UI Streamlit
# ======================

st.title("🧬 DNA Sequence Classification")
st.write("The DNA sequence classification model uses the classical model (k-mer + TF-IDF + classifier).")

st.subheader("Input DNA Sequence")

seq_input = st.text_area(
    "Enter the DNA sequence (A, C, G, T). It can be one sequence or several separated by newlines:",
    height=150,
    placeholder="Example:\nAGCTTAGCAAGTCCGATC"
)

predict_button = st.button("Predict")

if predict_button:
    if not seq_input.strip():
        st.warning("Please enter at least one DNA sequence.")
    else:
        # pisahkan tiap baris sebagai satu sequence
        seq_list = [s for s in seq_input.splitlines() if s.strip()]

        # lakukan prediksi
        try:
            preds = model.predict(seq_list)
        except Exception as e:
            st.error(f"An error occurred while predicting: {e}")
        else:
            st.subheader("Prediction Results")
            for i, (s, p) in enumerate(zip(seq_list, preds), start=1):
                st.markdown(f"**Sequence {i}:** `{clean_sequence(s)}`")
                st.write(f"→ Predicted class: **{p}**")
                st.write("---")
