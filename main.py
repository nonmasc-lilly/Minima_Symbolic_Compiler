import sys


debug = False;

if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} <file path>");
    exit(1);
if len(sys.argv) > 2:
    for i in sys.argv[2:]:
        if i == '-d': debug = True;
file = open(sys.argv[1], "r");
content = file.read();
file.close();

states = [];
atstate = False;
atcomp  = False
state_name = "";
ret = 0;
pointer = 0;

def apex(x):
    global ret
    global pointer
    global debug
    ret = x << (pointer*3) | ret;
    pointer += 1;
    if debug: print(f"{x}: {ret:b}");

for idx, i in enumerate(content):
    if atstate:
        if ord(i) == 0xA or ord(i) == 0xD or ord(i) == 0x20 or ord(i) == 0x9 or ord(i) == 0xB:
            atstate = False;
            states.append(state_name);
            x = len(states);
            while x != 0:
                apex(x & 7);
                x = x >> 3;
            apex(7);
            state_name = "";
            continue;
        state_name += i;
    if atcomp:
        if ord(i) == 0xA or ord(i) == 0xD or ord(i) == 0x20 or ord(i) == 0x9 or ord(i) == 0xB:
            atcomp = False;
            x = states.index(state_name)+1;
            while x != 0:
                apex(x & 7)
                x = x >> 3;
            apex(7);
            state_name = "";
            continue;
        state_name += i
    if i == '@':
        apex(6);
        atstate = True;
    if i == '~': apex(0);
    if i == '0': apex(1);
    if i == '1': apex(2);
    if i == '<': apex(3);
    if i == '>': apex(4);
    if i == '?':
        apex(5);
        atcomp = True


print(f"final: {ret:b}");
