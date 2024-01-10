import re
import io
import spacy
import joblib
import streamlit as st
import pandas as pd
from spellchecker import SpellChecker

nlp = spacy.load('en_core_web_md')
spell = SpellChecker()

def preprocess_text(text):
    '''Removes punctuation, stop words, whitespaces, newlines, corrects typos, and lemmatizes the tokens.'''

    text = re.sub(r'[\n\r]+', ' ', text)
    doc = nlp(text.strip())
    filtered_tokens = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_stop]
    misspelled = spell.unknown(filtered_tokens)

    for word in misspelled:
        corrected_word = spell.correction(word)  # problem was here
        if corrected_word != None:
            filtered_tokens[filtered_tokens.index(word)] = corrected_word

    return ' '.join(filtered_tokens)

def data_pipeline(text_or_df):
    '''Input: DataFrame with a single column containing string. Or a single string text.
       Output: 'word2vec_doc' Series with word2vec representation of shape (n_samples, 300) or (300,) depending on input.'''

    if isinstance(text_or_df, pd.DataFrame):
        text_or_df['processed_text'] = text_or_df['text'].apply(preprocess_text)
        text_or_df['word2vec_doc'] = text_or_df['processed_text'].apply(lambda text: nlp(text).vector)
        text_or_df.drop('processed_text', axis=1, inplace=True)
        X = text_or_df['word2vec_doc'].apply(pd.Series)
        text_or_df.drop('word2vec_doc', axis=1, inplace=True)
        return X

    elif isinstance(text_or_df, str):
        text_or_df = preprocess_text(text_or_df)
        return nlp(text_or_df).vector

st.title('Detect AI Generated Essays')

# description
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

description = """Use this app to check whether a given essay has been written by AI. Note 
that predictions are not 100% accurate. To use the app, write the essay you wish to test below in the space provided. You
will receive a message below the text box indicating the prediction of your essay. Alternatively, you may upload 
xlsx or csv files to check multiple essays at once. Enter the contents of the essay in a column called 
`text`, one essay per row. You may optionally add an id column for your reference. Check the image below for a sample file. 
Note that you can only upload one file at a time. Larger files may take longer to output. This app was developed from the
`LLM - Detect AI Generated Text` Kaggle Competition."""

st.markdown(f'<p class="big-font">{description}</p>', unsafe_allow_html=True)

show_image = st.checkbox('Show Image')
if show_image:
    st.image('sample_files/sample.png')

# loading model
model = joblib.load('models/model_w2v_vc_all_data')
output_mapping = {0: 'Human Written',
                  1: 'AI Generated'}

# text input
st.write('#')
input_text = st.text_area('Enter the essay to be tested here. Press Ctrl+Enter to apply.', value=None)

if input_text:
    x_test = data_pipeline(input_text).reshape(1, -1)
    y_hat = model.predict(x_test)[0]
    response = output_mapping[y_hat]
    st.text(response)
else:
    st.empty()

# xlsx or csv input
st.write('#')
input_file = st.file_uploader(label='Upload xlsx or csv files to be tested here.',
                 accept_multiple_files=False,
                 type=['csv', 'xlsx'])

if input_file is not None:
    def add_pred_to_df(df):
        X_test = data_pipeline(df)
        df['predictions'] = model.predict(X_test)
        df['predictions'] = df['predictions'].replace(output_mapping)

    if input_file.name.endswith('.csv'):  # if csv
        df = pd.read_csv(input_file)
        add_pred_to_df(df)

        @st.cache_data
        def convert_df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df_to_csv(df)

        download_csv = st.download_button(
            label="Download csv file",
            data=csv,
            file_name=input_file.name,
            mime='text/csv',
        )

        st.dataframe(df)

    else:  # if xlsx
        df = pd.read_excel(input_file)
        add_pred_to_df(df)

        buffer = io.BytesIO()

        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.close()

            download_xlsx = st.download_button(
                label="Download excel file",
                data=buffer,
                file_name=input_file.name,
                mime='application/vnd.ms-excel'
            )

            st.dataframe(df)
