import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban=set(banned)
        legal_words=[]
        normal=''.join(char.lower() if char.isalnum() else ' ' for char in paragraph)
        for word in normal.split():
            if word not in ban:
                legal_words.append(word)
        counts=collections.Counter(legal_words)
        return counts.most_common(1)[0][0]   
