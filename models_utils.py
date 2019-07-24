import pickle
import os


def model_dump(model, path):
    pickle.dump(model, open(path, "wb"))


def model_load(path):
    model = pickle.load(open(os.path.expanduser(path)))
    return model
