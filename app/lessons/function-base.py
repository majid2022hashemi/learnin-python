def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

intersect("HACK", "CHOK")
intersect([1, 2, 3], (1, 4))
intersect({'a':1, 'b':2}, {'b':9})
