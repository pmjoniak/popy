print(sorted('123 222 332'.split(), key=lambda x: (len(x), len(set(x))/len(x))))
