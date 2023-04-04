class Words():
    def __init__(self,words):
        self.words = words
    
    def prefix(self):
        shortest = 999
        shortest_word = 0
        for word in self.words:
            if len(word) < shortest:
                shortest = len(word)
                shortest_word = word
        
        chongfu = []
        for i in range (shortest+1):
            for word in self.words:
                if shortest_word[0:i] == word[0:i]:
                    chongfu.append(shortest_word[0:i])
                else:
                    while shortest_word[0:i] in chongfu:
                        chongfu.remove(shortest_word[0:i])
                    break
                        
        longest = 0
        longest_word = 0
        for zuhe in chongfu:
            if len(zuhe) > longest:
                longest = len(zuhe)
                longest_word = zuhe
        return longest_word

x=Words(("flower","flow","flight"))
print(x.prefix())
y=Words(("apple","application","appendix","appointment"))
print(y.prefix())