class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted = []

        for i in s:
            if i == '#':
                l = ord(decrypted.pop()) - 96
                r = ord(decrypted.pop()) - 96
                num = int(str(r) + str(l))
            else:
                num = int(i)
            decrypted.append(chr(96 + num))
        return ''.join(decrypted)
