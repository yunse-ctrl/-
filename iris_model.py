"""Reproducible Iris model. All preprocessing is fitted on training rows only."""
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

FEATURES = ["꽃받침 길이 (cm)", "꽃받침 너비 (cm)", "꽃잎 길이 (cm)", "꽃잎 너비 (cm)"]


def train_model():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=FEATURES)
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    model = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0, gamma="scale"))
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    names = list(iris.target_names)
    return {
        "model": model, "X": X, "y": y, "names": names,
        "X_train": X_train, "X_test": X_test,
        "accuracy": accuracy_score(y_test, predicted),
        "confusion": confusion_matrix(y_test, predicted, labels=[0, 1, 2]),
        "correct": int((predicted == y_test).sum()),
    }
