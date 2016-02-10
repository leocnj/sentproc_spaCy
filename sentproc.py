"""
using spaCy to generate POS and DP tag sequence
"""
import os
from spacy.en import English
import pandas as pd


def proc_onecsv(csvFile):
    csv = pd.read_csv(csvFile)
    label = csv.label.values

    pos_col = []
    dp_col = []
    texts = csv.text.values.tolist()
    for text in texts:
        parsed = parser(text.rstrip())
        wd_seq = []
        pos_seq = []
        dp_seq = []
        for span in parsed.sents:  # corresponding to natural sentences in each response
            sent = [parsed[i] for i in range(span.start, span.end)]
            wd_seq += [tk.orth_ for tk in sent]
            pos_seq += [tk.pos_ for tk in sent]
            dp_seq += ['-'.join([tk.orth_.lower(), tk.dep_, tk.head.orth_.lower()]) for tk in sent]
        pos_col.append(' '.join(pos_seq))
        dp_col.append(' '.join(dp_seq))
    (path, ext) = os.path.splitext(csvFile)
    pos_csv = path + '_pos' + '.csv'
    dp_csv = path + '_dp' + '.csv'

    pos_df = pd.DataFrame({'label': label, 'text': pos_col})
    pos_df.to_csv(pos_csv, index=False)

    dp_df = pd.DataFrame({'label': label, 'text': dp_col})
    dp_df.to_csv(dp_csv, index=False)


def proc_onedir(dir_path):
    for f in os.listdir(dir_path):
        print('proc...', f)
        if f.endswith('.csv'):
            proc_onecsv(dir_path+'/'+f)


parser = English()
proc_onedir('test')




