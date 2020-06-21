from difflib import SequenceMatcher

def common_longest(a, b):
    seqMatch = SequenceMatcher(None,a,b)
    match = seqMatch.find_longest_match(0, len(a), 0, len(b))
    if (match.size!=0):
        return a[match.a:match.a+match.size]
    else:
        return ""

def common_start(*strings):
    def _iter():
        for z in zip(*strings):
            if z.count(z[0]) == len(z):  # check all elements in `z` are the same
                yield z[0]
            else:
                return
    return ''.join(_iter())


def common(a, b):
    seqMatch = SequenceMatcher(lambda x: x==' ',a,b)
    matches = seqMatch.get_matching_blocks()
    com = []
    parameters = {}
    previous_a = 0
    previous_b = 0
    r = 0
    for i in matches:
        if i.size>0:
            com.append(a[i.a:i.a+i.size])
            if previous_a>0:
                r += 1
                temp = str(a[previous_a:i.a]).strip()+'|'+str(b[previous_b:i.b]).strip()
                parameters[str(r)] = temp
            previous_a = i.a + i.size
            previous_b = i.b + i.size
    return ' '.join(seqjoin(com)) #+"Parameter list: %s" %str(parameters.values())


def seqjoin(seq):
    r = []
    for i in range(len(seq)-1):
        r.extend([seq[i],'{%s}'%i])
    r.append(seq[-1])
    return r


def parameter(template, text):
    sublist = template.split('{}')
    p = []
    start = 0

    while True:
        flag = 0
        for i in sublist:
            find_loc = text.find(i,start)
            if find_loc>-1:
                if flag > 0:
                    p.append(text[start:find_loc])
                start = find_loc + len(i)
                flag += 1
            else:
                return '\n'.join(p)
