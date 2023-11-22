# Detect-AI-Generated-Text
This repository uses files from the Kaggle Competition 'LLM - Detect AI Generated Text'. This model detects whether a given essay text is AI generated or human written.

**How to use the model:**

Please make sure you have Python programming language installed.
Enter `pip install -r requirements.txt` and then `python -m spacy download en_core_web_md` in a terminal.

You can choose to either input one essay or several essays at once.

  If you wish to test only one essay then save the text in a new .txt file called `test_this.txt` inside the working directory with downloaded repository files. Ensure no extra lines, tabs, and spaces are present before and after the essay text in the file. A sample test file called `sample_test_this.txt` is given for reference. You may choose to replace its contents with your own data. Next, open the terminal in the working folder and enter `python use_model_txt_input.py`. You should see a print message in the terminal.

  Alternatively, if you wish to test several essays at once, then save the essay contents in a new .csv file called `test_this.csv` inside the working directory with downloaded repository files. This file should have two columns called `id` and `text`. The `id` column can have any values such as numbers to later identify the essays. The `text` column needs to have one essay in one row. A sample test file called `sample_test_this.csv` is given for reference. You may choose to replace its contents with your own data. Next, open the terminal in the working folder and enter `python use_model_csv_input.py`. To view your output, look for the `result` column in the newly created file called `result.csv`.

[REQUIREMENTS.TXT]

[EXPLAIN FILES]
