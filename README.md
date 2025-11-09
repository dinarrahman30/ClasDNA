# ClasDNA 🧬
#### **About This Project**

This project focuses on DNA sequence classification using classical machine learning methods.
Given a DNA sequence (a string of nucleotides A, C, G, and T), the model predicts its gene type based on patterns learned from labeled training data.

The main steps in this project are:
- Data preprocessing
  - Cleaning raw nucleotide sequences
  - Converting sequences into k-mers (subsequences of length k)
  - Treating k-mers as “tokens” similar to words in NLP
- Feature extraction
  - Using CountVectorizer and TF-IDF to transform k-mer tokens into numerical feature vectors
- Modeling
  - Training a classic machine learning model, Random Forest.
  - Evaluating performance using accuracy and classification metrics on validation and test sets
- Deployment
  - Serving the trained model through a Streamlit web application
  - Allowing users to input one or multiple DNA sequences and see the predicted gene type, along with additional information

This project demonstrates an end-to-end ML pipeline for biological sequence data, from preprocessing and feature engineering, through model training and evaluation, to deployment in a simple, interactive web app using Streamlit.

#### **Link Project**: https://clasdna.streamlit.app/

#### **Source**
Gunasekaran, H., Ramalakshmi, K., Rex Macedo Arokiaraj, A., Deepa Kanmani, S., Venkatesan, C., & Suresh Gnana Dhas, C. (2021). Analysis of DNA sequence classification using CNN and hybrid models. _Computational and Mathematical Methods in Medicine_, 2021(1), 1835056. https://pmc.ncbi.nlm.nih.gov/articles/PMC8285202/
