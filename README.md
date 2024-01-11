# Detect-AI-Generated-Text
This repository stores the files used to get the personal best score for the `LLM - Detect AI Generated Text` Kaggle Competition.
A concept app was made with available data that tries to detect if essays are AI generated. Predictions are not accurate and are biased towards being `AI Generated`. To try it out, go to [link].

# Personal Best Score Files
The `train_essays_chatgpt_manual.csv` file contains data that was manually collected by me from ChatGPT-3.5.
The `train_v2_drcat_02.csv` file contains data compiled from various sources. This dataset is called DAIGT-V2 was obtained from the following Kaggle User: https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset.
The `Mistral7B_CME_v7.csv` file contains data obtained from MISTRAL-7B from the following Kaggle User: https://www.kaggle.com/datasets/carlmcbrideellis/llm-mistral-7b-instruct-texts.

The `best_submission.ipynb` notebook contains the code used to submit to the Kaggle Competition. The score obtained was 0.794. The three datasets were combined by only including the `text` and `generated` features. The `RDizzl3_seven` feature was filtered for `True` values. This only includes essays with prompts that were present in the hidden test set that was used to evaluate the score. This allows for more representative data, potentially increasing the score. The text from the essay samples was preprocessed by removing punctuation and stop words and by lemmatizing the remaining tokens to produce cleaner data. Next, word2vec text representation was used to convert the text to numbers. This produced a new DataFrame of shape (n_samples, 300). The `VotingClassifier` class was used to collectively include several models for prediction. This allows for more robust results. The following models were included in `VotingClassifier`: `LogisticRegression`, `RandomForestClassifier`, `KNeighborsClassifier`, `GradientBoostingClassifier`, `XGBClassifier`, `LGBMClassifier`, and `CatBoostClassifier`. The voting mode was set to `soft`.

# Concept App Files
[INCLUDE DATA USED FOR THIS PART]

The `model_w2v_vc_all_data.joblib` file stores the parameters of a model that was trained on the DAIGT-V2, MISTRAL-7B, and the manually collected data. The `model_best_all_data.ipynb` file was used to build this model. The three datasets were combined, the essay text was preprocessed by removing punctuation, stop words, whitespaces, newlines, by correcting typos, and by lemmatizing the remaining tokens. Word2vec text representation was used from `spaCy` library to convert the preprocessed text to numbers. This produced a new DataFrame of shape (n_samples, 300). Note that the submission for the Kaggle Competition was 
