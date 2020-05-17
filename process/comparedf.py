import pandas as pd

def dfcompare(df1, key1, df2, key2):
    dff1=df1.fillna(0).copy()
    dff2=df2.fillna(0).copy()
    for i, j in zip(dff1.columns, dff2.columns):
        dff1[i]=dff1[i].astype(str(dff2.dtypes[j]))
    dff1['comb'] = dff1.astype(str).values.sum(axis=1)
    dff2['comb'] = dff2.astype(str).values.sum(axis=1)
    dff1 = dff1[[key1, 'comb']]
    dff2 = dff2[[key2, 'comb']]
    diff = pd.merge(dff1, dff2, left_on=key1, right_on=key2, how='inner')
    print("intersection length: %s" % len(diff))
    dff = diff[~(diff['comb_x'] == diff['comb_y'])]
    print("updated length: %s" % len(dff))
    if len(dff)>0:
        return dff[key2].tolist()
    else:
        return []

def detail_list(src_list, tgt_list, key):
    for i, j in zip(src_list.columns, tgt_list.columns):
        if (str(tgt_list.dtypes[j])=='int64' or str(tgt_list.dtypes[j])=='float64'):
            src_list[i] = pd.to_numeric(src_list[i])
        else:
            src_list[i] = src_list[i].astype(str(tgt_list.dtypes[j]))
    dfoutcome = pd.DataFrame()
    src_list.sort_values(src_list.columns[0], inplace=True)
    tgt_list.sort_values(tgt_list.columns[0], inplace=True)
    updatestatement = []
    for i in range(len(src_list)):
        dic = {}
        updates = []
        keycondition = ''
        for m, n, k, t in zip(src_list.iloc[i, :], tgt_list.iloc[i, :], tgt_list.columns, tgt_list.dtypes):
            if key == k:
                dic[k] = n
                keycondition = k + '=' + str(n) + ';'
            else:
                if ((m or '') == (n or '')) or str(m).lower() == str(n).lower():
                    dic[k] = '-'
                else:
                    dic[k] = '%s|%s' %(m, n)
                    if m is None:
                        updates.append(k + '=null')
                    elif str(t)!='int64' and str(t)!='float64':
                        updates.append(k + "='" + str(m).replace("'", "''") + "'")
                    else:
                        updates.append(k + '=' + str(m))

        tempdf = pd.DataFrame([dic], columns=dic.keys())
        dfoutcome = pd.concat([dfoutcome, tempdf], axis =0)

    return dfoutcome


if __name__ == '__main__':

    odf=pd.read_csv("../data/old.csv")
    ndf=pd.read_csv("../data/new.csv")
    odflist=odf['user_id'].tolist()
    ndflist=ndf['user_id'].tolist()
    print("old users count: %s" %len(odflist))
    print("new users count: %s" %len(ndflist))
    newuserids=set(ndflist)-set(odflist)
    print("new users found: %s" %len(newuserids))
    olduserids=set(odflist)-set(ndflist)
    print("old users missed: %s" %len(olduserids))
    comm=set(odflist).intersection(set(ndflist))
    print(len(comm))

    a=odf.dtypes
    b=ndf.dtypes
    c=pd.concat([a,b],axis=1)
    print(c)

    diffcontent=dfcompare(odf, 'user_id', ndf, 'user_id')
    print("Different content count: %s" %len(diffcontent))


    from random import sample
    comlist=sample(diffcontent,9)
    comlist

    src=odf[odf['user_id'].isin(comlist)]
    tgt=ndf[ndf['user_id'].isin(comlist)]

    output=detail_list(src, tgt, 'user_id')
    print(output)

    #output.to_csv("new_mem_details.csv", index=False)
