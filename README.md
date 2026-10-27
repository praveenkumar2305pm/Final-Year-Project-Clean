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

The following enhancements are planned to improve the usability, accessibility, and practical value of the Smart Plant Health Monitoring and Management System.

### 1. 🌱 IoT Integration for Real-Time Plant Monitoring
Integrate IoT sensors to collect real-time environmental data, such as soil moisture, temperature, humidity, and soil conditions. Use the collected data to help users monitor plant health and make informed irrigation and plant-care decisions.

### 2. 📩 SMS and Alert Notification System
Introduce SMS notifications and configurable alerts to inform users about detected plant diseases, low soil moisture, unfavorable weather conditions, and important plant-care activities. Notifications would depend on available data and configured alert thresholds.

### 3. 📱 Mobile-Friendly and Responsive Interface
Optimize the application for smartphones, tablets, and desktop computers. Improve navigation, image uploads, dashboard layouts, and readability to provide a smoother experience across different screen sizes.

### 4. 🤖 Improved AI-Based Disease Detection
Explore additional training data, model evaluation techniques, and image preprocessing methods to improve disease classification performance. Provide prediction confidence information where supported by the model.

### 5. 🌦️ Smart Weather-Based Recommendations
Enhance weather integration to provide relevant plant-care suggestions based on temperature, humidity, rainfall forecasts, and other available weather information.

### 6. 💧 Intelligent Irrigation Recommendations
Combine environmental data and, in a future IoT-enabled version, soil moisture readings to recommend when plants may need watering. Automated irrigation could be explored as a later extension.

### 7. 🌐 Multilingual Support
Introduce regional language support, including Telugu, to make the application easier to use for farmers and other users who prefer local-language guidance.

### 8. 🔐 Enhanced Security and User Experience
Strengthen authentication, securely manage API credentials, improve error handling, and introduce appropriate data protection measures.

### 9. 📊 Historical Data and Analytics
Add historical charts and reports to help users understand changes in environmental conditions, plant health observations, and seasonal agricultural trends.

### 10. 🧪 Continuous Testing and Model Evaluation
Establish systematic testing for application features and evaluate the disease detection model using suitable validation datasets and performance metrics.

*These enhancements are proposed future improvements and are not represented as currently implemented features.*


## 🎯 Project Objective

The objective of this project is to demonstrate how machine learning, deep learning, and web application technologies can be combined to create an accessible tool for plant health monitoring and agricultural information.

## 👨‍💻 Author

**Peddamudium Praveen Kumar**

Bachelor of Technology (B.Tech) — Computer Science and Engineering

- **GitHub:** [praveenkumar2305pm](https://github.com/praveenkumar2305pm)
- **Live Project:** [Smart Plant Health Monitoring System](https://praveenkumar2305pm-final-year-project-clean-main-ejokuf.streamlit.app/)

---

⭐ If you find this project useful, consider giving the repository a star!
