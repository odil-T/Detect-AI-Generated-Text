# The .csv file must have 'id' and 'text' column names where 'id' can contain anything for identification and 'text' should contain the essay. The output is a file called 'result.csv' with an additional column 'result'.

your_file_name = 'test_this.csv'  # change your input .csv file here

import joblib
import pandas as pd
import spacy

nlp = spacy.load('en_core_web_md')

def word2vec_data_pipeline(raw_test_data):
    '''Inputs test dataset as a DataFrame and returns X_test as word2vec representation.'''
    test_data['word2vec_doc'] = test_data['text'].apply(lambda text: nlp(text).vector)
    X_test = test_data['word2vec_doc'].apply(pd.Series)
    X_test.columns = X_test.columns.astype(str)
    return X_test

test_data = pd.read_csv(your_file_name)
model = joblib.load('models/model_word2vec_GB_no_promptid.joblib')
X_test = word2vec_data_pipeline(test_data)

y_pred = model.predict(X_test)
output_df = test_data[['id', 'text']].copy()
output_df['result'] = pd.Series(y_pred).map({1: 'AI Generated', 0: 'Human Written'})
output_df.to_csv('result.csv', index=False)
