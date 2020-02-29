class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = list(alphabet.decode('utf-8'))

    def encode(self, text):
        ret = ''
        for i, c in enumerate(text.decode('utf-8')):
            if c in self.alphabet:
                tindex = self.alphabet.index(c)
                kindex = self.alphabet.index(self.key[i%len(self.key)])
                ret = ret + self.alphabet[(tindex + kindex) % len(self.alphabet)]
            else:
                ret = ret + c
        return ret.encode('utf-8')

    def decode(self, text):
        ret = ''
        for i, c in enumerate(text.decode('utf-8')):
            if c in self.alphabet:
                tindex = self.alphabet.index(c)
                kindex = self.alphabet.index(self.key[i%len(self.key)])
                ret = ret + self.alphabet[(tindex+len(self.alphabet) - kindex) % len(self.alphabet)]
            else:
                ret = ret + c
        return ret.encode('utf-8')