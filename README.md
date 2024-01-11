# Detect-AI-Generated-Text
This repository stores the files used to get the best personal score for the `LLM - Detect AI Generated Text` Kaggle Competition.
A concept app was made with available data that tries to detect if essays are AI generated. Predictions are not accurate and are biased towards being `AI Generated`. To try it out, go to [link].

# Data
The `train_essays_chatgpt_manual.csv` file contains data that was manually collected by me from ChatGPT-3.5.

The `train_v2_drcat_02.csv` file contains data compiled from various sources. This dataset is called DAIGT-V2 was obtained from the following Kaggle User: https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset.

The `Mistral7B_CME_v7.csv` file contains data obtained from MISTRAL-7B from the following Kaggle User: https://www.kaggle.com/datasets/carlmcbrideellis/llm-mistral-7b-instruct-texts.

# Models
The `model_w2v_vc_all_data.joblib` file stores the parameters of a model that was trained on the DAIGT-V2, MISTRAL-7B, and the manually collected data. The `model_best.ipynb` file was used to build this model. The three datasets were combined, the essay text was preprocessed by removing punctuation, stop words, whitespaces, newlines, by correcting typos, and by lemmatizing the remaining tokens. Word2vec text representation was used from `spaCy` library to convert the preprocessed text to numbers. This produced a new DataFrame of shape (n_samples, 300). Note that the submission for the Kaggle Competition was 

# Other Files
