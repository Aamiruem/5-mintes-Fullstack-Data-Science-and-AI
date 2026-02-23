import mlflow.pyfunc
import numpy as np

model = mlflow.pyfunc.load_model(
    "models:/IrisRandomForest@production"
)

sample = np.array([[5.1, 3.5, 1.4, 0.2]])
print("Prediction:", model.predict(sample))

