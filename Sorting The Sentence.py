class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_sentence = sorted(s.split(" "), key=lambda word: word[len(word)-1])
        return " ".join(map(lambda word: word[:-1], sorted_sentence))
        
