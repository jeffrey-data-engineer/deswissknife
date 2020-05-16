import sys

if __name__ == '__main__':
    l = []
    for i in sys.stdin:
        n = i.rstrip()
        if n == 'exit':
            break
        else:
            l.append(n)
    print(l)

