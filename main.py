def in_autotests_we_trust(a, b):
    if a == b:
        print('Passou2')
    else:
        print('Falhou2')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(1, False)
