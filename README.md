# Detect-AI-Generated-Text
This repository stores some of the files used for the `LLM - Detect AI Generated Text` Kaggle Competition.
A concept app was made with available data that tries to detect if essays are AI generated. Predictions are not accurate and are biased towards being `AI Generated`. To try it out, go to [link].

# Data
The `train_essays_chatgpt_manual.csv` file contains data that was manually collected by me from ChatGPT-3.5.

The `train_v2_drcat_02.csv` file contains data compiled from various sources. This dataset is called DAIGT-V2 was obtained from the following Kaggle User: https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset. The `augmented-typos-introduced-ds5.csv` file contains the samples from DAIGT-V2 but typos were introduced to 15% of the human-written essays. This was obtained from the following Kaggle User: https://www.kaggle.com/competitions/llm-detect-ai-generated-text/discussion/458343.

The `Mistral7B_CME_v7.csv` file contains data obtained from MISTRAL-7B from the following Kaggle User: https://www.kaggle.com/datasets/carlmcbrideellis/llm-mistral-7b-instruct-texts. The `Mistral7B_CME_v7_15_percent_corruption.csv` file contains AI-generated essays where typos were introduced to 15% of the samples.

# Models


# Other Files
