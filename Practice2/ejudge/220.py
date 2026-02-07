n = int(input())
d = {}
for i in range(0, n):
    inp = input().split()
    cmd = inp[0]
    names = inp[1:]
    
    if cmd == 'set':
        for name in names:
            d[name] = name
    elif cmd == 'get':
        for name in names:
            if (name in d):
                print(name)
            else:
                print(f"KE: no key {name} found in the document")            
    