class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sug=[]
        products.sort()
        for i,c in enumerate(searchWord):
            temp=[]
            for p in products:
                if i<len(p) and c==p[i]:
                    temp.append(p)
            sug.append(temp[:3])
            products=temp
        return sug
