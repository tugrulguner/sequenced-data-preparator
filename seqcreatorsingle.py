# These functions create sequenced data in appropriate format in order to be able to insert them 7
# into GRU or LSTM

    
def seqcreatorsingle(seq, seqlength):
    inpx = list()
    for i in range(len(seq)):
        steprange = i + seqlength
        if steprange > len(seq)-1:
            break
        inp_seq_x = seq[i:steprange]
        inpx.append(inp_seq_x)
    return np.array(inpx)
