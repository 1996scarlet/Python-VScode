def INVERT(token_stream):
    putput_file = NewFile()
    dictionary = NewHash()
    while(free memory available):
        token <- next(token_stream)
        if term(token) not in dictionary:
            postings_list = AddToDictionary(dictionary, term(token))
        else:
            postings_list = GetPostingsList(dictionary, term(token))
        
        if full(postings_list):
            postings_list = DoublePostingsList(dictionary, term(token))
            AddToPostingsList(postings_list, docID(token))
        sorted_terms <- SortTerms(dictionary)
    WriteBlockToDisk(sorted_terms, dictionary, output_file)
    return output_file

def INVERT(A, B):
    I <- (); ka <- 1; kb <- 1;
    AFirst <- RandomBit()
    while( ka<=A && kb<=B):
        if( ka < kb || ka == kb || AFirst ==1 ):
            if A(ka) not in I: 
                I <- I + A(ka)
            ka <- ka + 1
        else:
            if B(kb) not in I:
                I <- I + B(kb)
            kb <- kb + 1
    return I

    

def encode(fwd_rnn, bwd_rnn, word_vectors):
    fwd_out = ndarray((len(word_vectors), fwd_rnn.nr_hidden), dtype = 'float32')
    bwd_out = ndarray((len(word_vectors), bwd_rnn.nr_hidden), dtype = 'float32')
    fwd_state = fwd_rnn.initial_state()
    bwd_state = bwd_rnn.initial_state()
    for i in range(len(word_vectors)):
        fwd_state = fwd_rnn(word_vectors[i], fwd_state)
        bwd_state = bwd_rnn(word_vectors[-i-1], bwd_state)
        fwd_out[i] = fwd_state
        bwd_out[-i-1] = bwd_state
    return concatenate([fwd_state, bwd_state])

List<KeyInfo> list = keyService.getAll();
foreach key in list:
    r.hset("key_info", key.getId(), key.getSig()+","+key.getStatus()+","+key.getUrl())
return

var res = from x in conMal.Concat(conSer)
            group x by x into g
            select new { key = g.Key, v = g.Count() };

var res = from x in conMal.Concat(conSer)
            group x by x into g
            select new { key = g.Key, v = g.Count() };


