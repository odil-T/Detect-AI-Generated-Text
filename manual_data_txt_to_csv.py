# This script converts the 50 txt files of both essay topics into one csv file. This give a total of 100 manually
# collected samples.

import pandas as pd
import os

df = pd.DataFrame(columns=['prompt_id', 'text', 'generated'])

for essay_topic in ('car', 'college'):
    essay_topic_to_prompt_id = {'car': 0,
                                'college': 1}

    directory_path = f'data/chatgpt_manual_{essay_topic}'

    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, 'r') as file:
                text_content = file.read()

            df = df._append({'prompt_id': essay_topic_to_prompt_id[essay_topic],
                        'text': text_content, 'generated': 1}, ignore_index=True)

csv_file_path = f'data/train_essays_chatgpt_manual.csv'
df.to_csv(csv_file_path, index=False)
