Here, you can find two functions, which can help you for data preparation of any kind of RNN architecture.  
First function, seqcreator(seq, label, seqlength) in seqcreator.py, takes sequenced data as seq, labeled data as label and the number of sequence or sequence length as seqlength and produces arrays equal to seqlength in size and puts corresponding label, which RNN architecture will try to fit.

In other words, RNN architecture will take each sequence as input from seq with the size of seqlength, and will try to train it using corresponding label.

Second function, seqcreatorsingle(seq, seqlength), is exactly works same like above but without containing label. This function can help you to prepare just input data for RNN in case if you don't need or have labels.
