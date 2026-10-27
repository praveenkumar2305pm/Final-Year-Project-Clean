# 🌱 Smart Plant Health Monitoring and Management System

An AI-powered web application designed to help users explore seasonal crop trends, identify plant diseases from images, access fertilizer recommendations, and learn plant growth tips.

🔗 **Live Demo:** [Open the Application](https://praveenkumar2305pm-final-year-project-clean-main-ejokuf.streamlit.app/)

📂 **Source Code:** [GitHub Repository](https://github.com/praveenkumar2305pm/Final-Year-Project-Clean)

---

## 📌 Project Overview

Plant health and crop management are important for improving agricultural productivity. Identifying plant diseases early and choosing suitable crops and fertilizers can help users make better agricultural decisions.

The **Smart Plant Health Monitoring and Management System** is a Python-based application that combines machine learning, image classification, and an interactive web interface to provide useful plant health and crop-related information.

The application is developed using Streamlit and includes multiple features accessible through a dashboard.

## ✨ Key Features

- **🌾 Seasonal Trend Analysis:** Explore crop-related information by selecting a district and season.
- **🦠 Plant Disease Detection:** Upload a plant image to obtain a disease prediction using a CNN-based deep learning model.
- **🧪 Fertilizer Recommendations:** Access fertilizer-related information to support plant care.
- **🌿 Plant Growth Tips:** Explore information related to plant growth and maintenance.
- **🌦️ Weather Information:** View weather conditions for the configured location.
- **👤 User Authentication:** Login and registration interfaces for users.

*Feature availability and recommendations depend on the application's configured data sources and implementation.*

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive web interface |
| PyTorch | Deep learning model loading and inference |
| CNN | Plant disease image classification |
| Pandas | Dataset and CSV processing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning utilities |
| Pillow | Image processing |
| TensorFlow | Machine learning framework dependency |
| Git and GitHub | Version control and source code management |
| Streamlit Community Cloud | Application deployment |

## ⚙️ How It Works

1. The user opens the application and navigates through the dashboard.
2. For seasonal analysis, the user selects a district and season.
3. For disease detection, the user uploads an image of a plant.
4. The application processes the image and passes it to the trained CNN model.
5. The model produces a prediction, which the application displays to the user.
6. Users can explore the other available crop information, fertilizer resources, weather information, and plant growth tips.

## 🧠 Machine Learning Approach

The disease detection component uses a **Convolutional Neural Network (CNN)** for image classification.

CNNs are commonly used in computer vision because they can learn visual patterns such as shapes, textures, and image features.

The trained model is stored in a PyTorch model file:

`plant_disease_model_1_latest.pt`

The application loads the model and uses it to make predictions on uploaded plant images.

**Note:** Model accuracy and performance should be reported only after verification using the project's actual evaluation results.

## 📁 Project Structure

```text
Final-Year-Project-Clean/
│
├── main.py
├── home_page.py
├── login_page.py
├── register_page.py
├── user_home.py
├── CNN.py
├── disease_info.csv
├── supplement_info.csv
├── requirements.txt
├── .gitignore
│
└── Other project assets,
    datasets and supporting files
```

The large trained model file is downloaded when needed by the application and is not required to be committed directly to the Git repository.

## 🚀 Run the Project Locally

### Prerequisites

- Python 3.11
- Git
- Internet connection for required downloads and external services

### 1. Clone the repository

```bash
git clone https://github.com/praveenkumar2305pm/Final-Year-Project-Clean.git
```

### 2. Navigate to the project directory

```bash
cd Final-Year-Project-Clean
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Start the application

```bash
streamlit run main.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

**Important:** The trained model must be accessible through the configured download mechanism, and any required API credentials or external services must be configured correctly.

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud** and connected to the GitHub repository.

Live application: [Smart Plant Health Monitoring System](https://praveenkumar2305pm-final-year-project-clean-main-ejokuf.streamlit.app/)

## 🔮 Future Enhancements

- Improve model performance through further training and evaluation.
- Expand crop and disease coverage.
- Provide more localized crop recommendations.
- Improve prediction explanations and confidence reporting.
- Enhance application security and user account management.
- Add automated testing and more detailed performance evaluation.

## 🎯 Project Objective

The objective of this project is to demonstrate how machine learning, deep learning, and web application technologies can be combined to create an accessible tool for plant health monitoring and agricultural information.

## 👨‍💻 Author

**Peddamudium Praveen Kumar**

Bachelor of Technology (B.Tech) — Computer Science and Engineering

- **GitHub:** [praveenkumar2305pm](https://github.com/praveenkumar2305pm)
- **Live Project:** [Smart Plant Health Monitoring System](https://praveenkumar2305pm-final-year-project-clean-main-ejokuf.streamlit.app/)

---

⭐ If you find this project useful, consider giving the repository a star!
