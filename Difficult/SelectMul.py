
def SelectMul(N):
    zero = ''
    for i in range(N.count('0')):
        zero += '0'
        N.remove('0')
    
    N = sorted(N, reverse=True)

    f, b = ['0'], ['0']

    for j in range(len(N)-1):
        if j%2 == 0:
            f.append(N[j])
        else:
            b.append(N[j])
    
    for k in range(min(len(f), len(b))):
        if f[k] != b[k]:
            f[k], b[k] = b[k], f[k]
            break
    
    f, b = ''.join(f), ''.join(b)

    if int(f) <= int(b):
        f += N[-1]
    else:
        b += N[-1]
    
    print(int(f+zero)*int(b))

if __name__ == '__main__':
    N = list(input())
    SelectMul(N)
    


