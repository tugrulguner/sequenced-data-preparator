# These functions create sequenced data in appropriate format in order to be able to insert them 7
# into GRU or LSTM

def seqcreator(seq, label, seqlength):
    inpx, inpy = list(), list()
    for i in range(len(seq)):
        steprange = i + seqlength
        if steprange > len(seq)-1:
            break
        inp_seq_x, inp_seq_y = seq[i:steprange], label[i]
        inpx.append(inp_seq_x)
        inpy.append(inp_seq_y)
    return np.array(inpx), np.array(inpy)
    
