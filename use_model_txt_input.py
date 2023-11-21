# The .txt file should contain one essay. The output is a print statement.

your_file_name = 'test_this.txt'  # change your input .txt file name here

import joblib
import spacy
import pandas as pd

nlp = spacy.load('en_core_web_md')

def word2vec_data_pipeline(text):
    '''Inputs raw text and returns x_test DataFrame as word2vec representation.'''

    x_test = pd.DataFrame([nlp(text).vector])
    x_test.columns = [str(i) for i in range(300)]
    return x_test

with open(your_file_name, 'r') as file:
    test_data = file.read()

model = joblib.load('models/model_word2vec_GB_no_promptid.joblib')
x_test = word2vec_data_pipeline(test_data)

y_pred = 'AI Generated' if model.predict(x_test) == 1 else 'Human Written'
print(y_pred)
