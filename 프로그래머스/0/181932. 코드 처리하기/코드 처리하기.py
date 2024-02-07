def solution(code): 
    mode = int(0)
    ret =  ''
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = (mode+1)% 2
        else:
            if mode == 0:
                if idx%2 == 0:
                    ret = ret+ code[idx]
            elif mode == 1:
                if idx%2 == 1:
                    ret = ret+code[idx]
                
    if ret == '':
        return "EMPTY"
    else:
        return ret
    