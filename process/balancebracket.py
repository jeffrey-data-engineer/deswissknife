def balance_bracket(n):
    # Your code here!
    s="()"*n
    e="("*n+")"*n
    r=[]
    if n<=1:
        r.append(s)
        return r
    else:
        r.append(s)
        s=list(s)
        e=list(e)
        while s.index(')')<n:
            for j in range(s.index(')'),n*2-1):
                if s[j]!=s[j+1]:
                    s[j],s[j+1]=s[j+1],s[j]
                    r.append(''.join(s))
        return r

print(balance_bracket(3))