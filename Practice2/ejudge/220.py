n = int(input())
d = {}
for i in range(0, n):
    inp = input().split()
    cmd = inp[0]
    name = inp[1]
    if cmd == 'set':
        d[name] = inp[2]
    elif cmd == 'get':
        if (name in d):
            print(d[name])
        else:
            print(f"KE: no key {name} found in the document")            
    