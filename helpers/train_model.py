from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from models.response.trained_model import TrainResponse
    
def train_model(x, y) -> TrainResponse:
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_val)
    acc = accuracy_score(y_val, y_pred)
    model_path = "ML/models/model.pkl"
    joblib.dump(model, model_path)
    return model, acc