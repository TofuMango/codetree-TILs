class CodeName:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = int(score)

CN = []
for _ in range(5):
    codename, score = (input().split())
    CN.append(CodeName(codename, score))

minScore = 1000000
minCodename = ""
for i in CN:
    if i.score < minScore:
        minScore = i.score
        minCodename = i.codename
print(minCodename, minScore)