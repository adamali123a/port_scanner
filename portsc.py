import socket
moscow = r"""
 __  __
|  \/  | ___  ___  ___ _____      __
| |\/| |/ _ \/ __|/ __/ _ \ \ /\ / /
| |  | | (_) \__ \ (_| (_) \ V  V /
|_|  |_|\___/|___/\___\___/ \_/\_/
"""
print("\033[0;32m",moscow)
print("\n")
print("script by moscow")
print("\n")
l = input("Lyera ipka banwsa:  ")
try:
    for p in range(1,10000):
        a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        e = a.connect_ex((l,p))
        if e == 0:
            ss = socket.getservbyport(p)
            print("porte {} joaraky ({}) krawya".format(p,ss))

except:
    print("aw shta bony nya")
