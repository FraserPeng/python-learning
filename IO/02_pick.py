# 序列化

import pickle

d = dict(name="Faser", age=32, score=100)

print(pickle.dumps(d))

with open("./IO/dump.txt", 'wb') as f:
    pickle.dump(d, f)

with open("./IO/dump.txt", 'rb') as f:
    d = pickle.load(f)
    print(d)
