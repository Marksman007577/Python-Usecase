import pickle as pk

D = {'a': 1, 'b': 2}

# write a data to a file using pickle
with open('datafile.pkl', mode='wb') as F:
    pk.dump(D, F)
    F.close()

# Reading content of a file in pickle
with open('datafile.pkl', mode='rb') as dataset:
    result = pk.load(dataset)
    dataset.close()

print(result)
