import streamlit as st


st.success('Witaj w aplikacji!')

st.title('Tłumacz angielsko-niemiecki 🇬🇧 🇩🇪')

st.header('Informacje')
st.write('To aplikacja, która pozwala na przetłumaczenie dowolnego zdania lub wyrazu z języka angielskiego na język niemiecki.')
st.write('Wpisz żądaną frazę w pole poniżej, a następnie kliknij kombinację klawiszy, która widnieje w prawym dolnym rogu pola tekstowego')


st.header('Tłumaczenie języka naturalnego')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Tłumaczenie z języka angielskiego na niemiecki"
    ],
)


if option == "Tłumaczenie z języka angielskiego na niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner("Proszę czekać, trwa tłumaczenie..."):
            translator = pipeline("translation_en_to_de")
            answer = translator(text)
            st.success(answer[0].get('translation_text'))


st.subheader('s19086, Jacek Ziółkowski')