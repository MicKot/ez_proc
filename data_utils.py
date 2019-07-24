import pandas as pd
import numpy as np


def adversarial_test(training_data, test_data, model, metrics):
    features = training_data.columns
    training_data["target"] = 1
    test_data["target"] = 0
    concatenated_train_test = pd.concat([training_data, test_data], axis=0)
    target = concatenated_train_test["target"]

    if hasattr(model, "fit"):
        model.fit(concatenated_train_test[features], target)
    elif hasattr(model, "train"):
        model.train(concatenated_train_test[features], target)
    else:
        raise TypeError("Unknown model type")

    predictions = model.predict(concatenated_train_test)
    print(metrics(target, predictions))
