# COVID
# 🦠 COVID-19 Prediction Web App (Flask + ML)

A simple and clean **Machine Learning web application** built using **Flask** that predicts COVID-19 recovered cases based on user inputs.

---

## 🚀 Features

* 📊 Predict recovered cases using ML model
* 🌐 Web interface using Flask
* 🎨 Clean and responsive UI
* ⚡ Fast deployment on Render
* 📁 Uses real dataset

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* HTML & CSS
* Gunicorn (for deployment)

---

## 📁 Project Structure

```
COVID/
│
├── app.py
├── ada_model.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

## ⚙️ Installation & Run Locally

### 1. Clone the repository

```
git clone https://github.com/BaddelaVenkatesh/COVID.git
cd COVID
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## ☁️ Deployment (Render)

* Add `Procfile`:

```
web: gunicorn app:app
```

* Add `runtime.txt`:

```
python-3.10.0
```

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
gunicorn app:app
```

---

## ⚠️ Important Notes

* Ensure model file (`ada_model.pkl`) is in root directory
* Input features must match training features
* Use Python 3.10 for compatibility

---

## 📸 Output

* User enters confirmed cases & deaths
* App predicts recovered cases

---

## 📌 Future Improvements

* Add graphs and dashboards
* Improve UI with Bootstrap
* Add multiple ML models
* Deploy with database

---

## 👨‍💻 Author

**Baddela Venkatesh**

---

⭐ If you like this project, give it a star on GitHub!
