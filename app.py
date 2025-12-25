import streamlit as st

st.title("Enerji Analiz Portalı - Test Yayını")
st.write("Eğer bu yazıyı görüyorsanız bağlantı başarılıdır!")

uploaded_file = st.file_uploader("Test için bir dosya yükleyin")
if uploaded_file:
    st.success("Dosya başarıyla yüklendi!")