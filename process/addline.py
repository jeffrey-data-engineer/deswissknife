import sys

if __name__ == '__main__':
    with open('../data/countsql.txt', 'r') as f,open('../data/outsql.txt', 'w') as outf:
        for l in f:
            outf.write(l)
            outf.write('union all\n')



