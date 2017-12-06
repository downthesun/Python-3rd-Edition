def read():
    file = input( 'Enter a file name with its extension: ')
    user_file = open(file, 'r')
    unique_Words = set()

    for lin in user_file:
        line = lin.rstrip()
        words = lin.split()

        for w in words:
            punctuation = (".,!?")

            for char in punctuation:
                w = w.replace(char,"")

            if w not in unique_Words:
                unique_Words.add(w)

        print('\n'.join(unique_Words))

read()
