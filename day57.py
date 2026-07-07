import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

print("Model Loaded Successfully!")

import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

print(model["king"])

print(model.most_similar("computer", topn=5))