if __name__ == '__main__':
    s = 'YYYZZZZ1987'
    codecs = ['latin_1', 'utf_8', 'utf_16']
    for codec in codecs:
        print(codec, s.encode(codec), sep='\t')

