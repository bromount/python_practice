def ask_conf(prompt, retries=4, complaint='Yes or No alone!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'): return True
        if ok in ('n', 'no'): return False
        retries = retries - 1
        if retries < 0: raise IOError, 'refusenik user'
        print complaint


ask_conf('Do you really want to quit?')


def f(a, L=[]):
    L.append(a)
    return L


print f(1)
print f('anna')
print f('malai')