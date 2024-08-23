import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
import argparse
import os

np.random.seed(0)


def load_data(args):
    data_df = pd.read_csv(os.path.join(args.data_dir, "driving_log.csv"))
    X = data_df[["center", "left", "right"]].values
    y = data_df["steering"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=args.test_size, random_state=0
    )
    return X_train, X_test, y_train, y_test


def build_model():
    model = Sequential()
    model.add(Lambda(lambda x: x / 127.5 - 1.0, input_shape=INPUT_SHAPE))
    model.add(Conv2D(24, 5, 5, activation="elu"))
