Commands : 
conda create -n mlflow-env python=3.10
conda activate mlflow-env
pip install mlflow scikit-learn pandas numpy
mlflow --version
2nd Terminnal(mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns \
  --host 127.0.0.1 \
  --port 5000
)
mlflow ui
http://127.0.0.1:5000
python train.py
python predict.py
