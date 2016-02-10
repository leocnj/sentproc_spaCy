"""
using spaCy to generate POS and DP tag sequence
"""
from spacy.en import English
import pandas as pd

def proc_onecsv(csvFile):
    csv = pd.read_csv(csvFile)
    label = csv.label.values
    texts = csv.text.values.tolist()
    for text in texts:
        parsed = parser(text.rstrip())
        wd_seq = []
        pos_seq = []
        dp_seq = []
        for span in parsed.sents:
            sent = [parsed[i] for i in range(span.start, span.end)]
            wd_seq += [tk.orth_ for tk in sent]
            pos_seq += [tk.pos_ for tk in sent]
            dp_seq += ['-'.join([tk.orth_, tk.dep_, tk.head.orth_]) for tk in sent]
            # print('sent:', ' '.join(wd_seq))
            # print('POS: ', ' '.join(pos_seq))
            # print('DP: ', ' '.join(dp_seq))
        print('SENT>> ' + ' '.join(wd_seq))
        print('POS>> ' + ' '.join(pos_seq))

parser = English()
proc_onecsv('test/train1.csv')



