import gensim.downloader as api

# load pretrained model (takes time first time)
model = api.load("word2vec-google-news-300")

# analogy function
def analogy(a, b, c):
    try:
        result = model.most_similar(positive=[a, c], negative=[b], topn=1)
        return result[0][0]
    except:
        return "Not found"

# test examples
tests = [
    ('king','man','woman'),
    ('paris','france','italy'),
    ('good','better','bad'),
    ('boy','girl','man'),
    ('father','man','woman'),
    ('walk','walking','run'),
    ('big','bigger','small'),
    ('strong','stronger','weak'),
    ('fast','faster','slow'),
    ('love','happy','sad')
]

print("Word Analogy Results:\n")

for a,b,c in tests:
    print(f"{a} - {b} + {c} = {analogy(a,b,c)}")