import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

def test_model():
    # Load the iris dataset
    iris = load_iris()
    X_test = iris.data
    y_test = iris.target

    # Load the trained model
    model = joblib.load('model.pkl')

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    test_model()
