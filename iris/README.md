# Iris Species Classification - ML Pipeline & Deployment

A complete end-to-end machine learning project that classifies Iris flower species using Decision Tree and Logistic Regression models, deployed with FastAPI and a modern web frontend.

## 🚀 Features

- **Complete ML Pipeline**: Data cleaning, EDA, preprocessing, training, and evaluation
- **Two Models**: Logistic Regression and Decision Tree Classifier
- **FastAPI Backend**: RESTful API for real-time predictions
- **Modern Frontend**: Clean, responsive web interface
- **Deployment Ready**: Configured for easy deployment on Render, Railway, or similar platforms

## 📁 Project Structure

```
iris/
├── notebooks/
│   └── iris_pipeline.ipynb      # Complete ML pipeline notebook
├── models/
│   ├── logistic_model.pkl       # Trained Logistic Regression model
│   ├── decision_tree_model.pkl  # Trained Decision Tree model
│   └── scaler.pkl                # Feature scaler
├── static/
│   └── index.html               # Frontend interface
├── main.py                      # FastAPI backend application
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd iris
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebook** (optional - models are already included)
   - Open `notebooks/iris_pipeline.ipynb` in Jupyter/Google Colab
   - Run all cells to regenerate models

## 🚀 Running Locally

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The application will be available at:
- **Frontend**: http://localhost:8000/
- **API Docs**: http://localhost:8000/docs
- **API Endpoint**: http://localhost:8000/predict

## 📊 ML Pipeline

The notebook (`notebooks/iris_pipeline.ipynb`) includes:

1. **Data Loading**: Load Iris dataset from scikit-learn
2. **Data Cleaning**: Check for missing values, duplicates, and outliers
3. **Exploratory Data Analysis**: Visualizations, correlations, pair plots
4. **Data Preprocessing**: Train/test split, feature scaling
5. **Model Training**: Train Logistic Regression and Decision Tree
6. **Model Evaluation**: Accuracy, classification reports, confusion matrices
7. **Model Export**: Save models using joblib

## 🔌 API Usage

### Predict Endpoint

**POST** `/predict`

**Request Body:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2,
  "model_choice": "logistic"
}
```

**Response:**
```json
{
  "prediction": "Setosa"
}
```

**Model Choices:**
- `"logistic"` - Logistic Regression
- `"decision_tree"` - Decision Tree Classifier

### Example using cURL:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "model_choice": "logistic"
  }'
```

## 🌐 Deployment

### Deploy to Render

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variable `PORT` (Render sets this automatically)

### Deploy to Railway

1. Push your code to GitHub
2. Create a new project on Railway
3. Connect your GitHub repository
4. Railway will auto-detect FastAPI and deploy

### Update Frontend URL

After deployment, update the API URL in `static/index.html`:
```javascript
const api_url = "https://your-app-url.onrender.com/predict";
```

## 📦 Dependencies

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `scikit-learn` - Machine learning library
- `joblib` - Model serialization
- `numpy` - Numerical computing
- `pandas` - Data manipulation (for notebook)
- `matplotlib` - Visualization (for notebook)
- `seaborn` - Statistical visualization (for notebook)

## 📝 Model Performance

Both models achieve excellent performance on the Iris dataset:
- **Logistic Regression**: ~100% accuracy
- **Decision Tree**: ~100% accuracy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Your Name

## 🔗 Links

- **GitHub Repository**: [Your Repo Link]
- **Deployed Application**: [Your Deployed App Link]


