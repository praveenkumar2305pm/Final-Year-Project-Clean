import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import joblib
from sklearn.ensemble import RandomForestRegressor
user=st.session_state['user']
city=user[3]
import pyowm
from PIL import Image
import torch
owm = pyowm.OWM('11081b639d8ada3e97fc695bcf6ddb20')
import CNN
import os
import torchvision.transforms.functional as TF
disease_info = pd.read_csv('disease_info.csv' , encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv',encoding='cp1252')

model = CNN.CNN(39)    
model.load_state_dict(torch.load("plant_disease_model_1_latest.pt"))
model.eval()

def prediction(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index
import requests
YOUTUBE_API_KEY = "AIzaSyDYEeSTrT7pPpVzpmaJ491gxogVxfWwpvM"

def fetch_youtube_videos(query, max_results=6):
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': max_results
    }
    response = requests.get(url, params=params)
    videos = []
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            videos.append({'video_id': video_id, 'title': video_title})
    return videos

try:
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    humd = weather.humidity
    sky = weather.detailed_status
    rain = weather.rain.get('1h', 0)
except:
    st.write(city)
    temp=25
    humd=50
    sky='Snow'
    rain=100
def seasonal():
    
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/226/390/small_2x/ai-generated-nature-landscapes-background-free-photo.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;  /* Ensure the background covers the whole screen */
            background-color: rgba(255, 255, 255, 0.7); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<h1 style='text-align: center; color:red;'>Seasonal Trend Analysis</h1>", unsafe_allow_html=True)
    st.markdown('---')
    df=pd.read_csv("Crop_recommendation.csv")
    col1, col2 = st.columns([5,5])
    district=col1.selectbox('Select District',df['District'].unique())
    season=col2.selectbox('Select Season',df['Season'].unique())   
    k=season.split('(')[0]
    df=df[(df['District']==district) & (df['Season']==k)]
    crops=df['Crop'].unique()
    k=str(k)
    crop_images=pd.read_csv('Crops.csv')
    crop_images=crop_images.set_index('Crop')
    col1, col2, col3=st.columns([10,5,10])
    if col2.button('Submit',type='primary'):
        st.markdown('---')
        col1,col2,col3=st.columns([5,5,5])
        try:
            for i in range(0,len(crops),3):
                with col1:
                    if i<len(crops):
                        st.image(crop_images.loc[crops[i],'Image'],use_column_width=True)
                        st.markdown(f"<h5 style='text-align: center; color:black;'>{crops[i]}</h5>", unsafe_allow_html=True)
                with col2:
                    if i+1<len(crops):
                        st.image(crop_images.loc[crops[i+1],'Image'],use_column_width=True)
                        st.markdown(f"<h5 style='text-align: center; color:black;'>{crops[i+1]}</h5>", unsafe_allow_html=True)
                with col3:
                    if i+2<len(crops):
                        st.image(crop_images.loc[crops[i+2],'Image'],use_column_width=True)
                        st.markdown(f"<h5 style='text-align: center; color:black;'>{crops[i+2]}</h5>", unsafe_allow_html=True)
        except:
            pass

def fertilizer():
    try:
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area */
            .main {
                background-image: url('https://eos.com/wp-content/uploads/2023/11/components-of-different-types-of-fertilizers.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                min-height: 100vh;  /* Ensure the background covers the whole screen */
                background-color: rgba(255, 255, 255, 0.8); /* Add a semi-transparent overlay */
                background-blend-mode: overlay; /* Blend the image with the overlay */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"<h1 style='text-align: center; color:blue;'>Fertilizer Recommendation System</h1>", unsafe_allow_html=True)
        st.markdown('---')
        fertilizer=['10-10-10','10-26-26','14-14-14','14-35-14','15-15-15','17-17-17','20-20','28-28','DAP','Potassium chloride','Potassium sulfate.','Superphosphate','TSP','Urea']
        soil=['Black','Clayey','Loamy','Red','Sandy']
        crop=['Barley','Cotton','Ground Nuts','Maize','Millets','Oil seeds','Paddy','Pulses','Sugarcane','Tobacco','Wheat','coffee','kidneybeans','orange','pomegranate','rice','watermelon']
        col1, col2,col3= st.columns([5,5,5])
        user=st.session_state['user']
        location=user[3]
        a=temp
        b=humd

        col1,col2,col3= st.columns([5,5,5])
        with col1:
            c=st.number_input('Moisture',min_value=42.8,max_value=100.0)
        with col2:
            d=st.selectbox('Soil Type',('Black','Clayey','Loamy','Red','Sandy'))
        with col3:
            e=st.selectbox('Crop Type',('Barley','Cotton','Ground Nuts','Maize','Millets','Oil seeds','Paddy','Pulses','Sugarcane','Tobacco','Wheat','coffee','kidneybeans','orange','pomegranate','rice','watermelon'))
        col1, col2,col3= st.columns([5,5,5])
        with col1:
            f=st.number_input('Enter N',min_value=0,max_value=126,value=10)
        with col2:
            g=st.number_input('Enter P',min_value=0,max_value=54,value=7)
        with col3:
            h=st.number_input('Enter K',min_value=0,max_value=59,value=8)
        
        col4, col5, col6 = st.columns([12,5,10])
        if col5.button('Predict',type='primary'):
            col1, col2, col3 = st.columns(3)
            data = np.array([[a,b,c,soil.index(d),crop.index(e),f,g,h]])
            model=pickle.load(open('classifier.pkl','rb'))
            res=model.predict(data)
            d1=pd.read_csv('fertilizer.csv')
            #get the image of the fertilizer
            d1=d1.set_index('fertilizer')
            col1,col2,col3=st.columns([5,5,5])
            col2.image(d1.loc[fertilizer[res[0]],'image'],width=300)
    except Exception as e:
        st.write(e)
        st.error('Please enter valid values')
def user_home_page():
    # Navigation menu for user dashboard

    with st.sidebar:
        st.markdown(f"<h1 style='text-align: center; color: black;'><b>🏡Dashboard</b></h1>", unsafe_allow_html=True)
        st.image("https://www.pngkey.com/png/full/913-9135243_img-ploughing-indian-farmer-clipart.png",use_column_width=True)
        user=st.session_state['user']
        location=user[3]
        st.markdown(f"<h1 style='text-align: center; color: blue;'>Location: {location}</h1>", unsafe_allow_html=True)
        col1,col2=st.columns([1,1])
        col1.markdown(f"<h1 style='text-align: center; color:black;'>{temp}🌞</h1>", unsafe_allow_html=True)
        col2.markdown(f"<h1 style='text-align: center; color:black;'>{sky}🌥️</h1>", unsafe_allow_html=True)
        selected_tab = option_menu(
            menu_title=None,
            options=["Seasonal Based Crops", "Fertilizers", 'Disease Detection','Plant Growth Tips','Logout'],
        styles={
        "nav-link-selected": {"background-color": "green", "color": "white", "border-radius": "5px"},
        }
        )
        
        

    if selected_tab == "Seasonal Based Crops":
        seasonal()
    elif selected_tab == "Fertilizers":
        fertilizer()
    elif selected_tab == "Disease Detection":
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area with transparency */
            .main {
                background-image: url('https://media.istockphoto.com/id/1250059761/photo/septoria-of-tomatoes-tomato-leaves-affected-by-septoria-lycopersici-fungus.jpg?s=612x612&w=0&k=20&c=GuJ1uqQjaGryWs8Qp1xmBOMSPdlUho8X8DKKkjYRV44=');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-color: rgba(255, 255, 255, 0.6); /* Add a semi-transparent overlay */
                background-blend-mode: overlay; /* Blend the image with the overlay */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div style="text-align: center; color: white;">
                <h1 style="color: maroon; font-size: 50px; text-align: center;">Crop Disease Detection</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        # File uploader
        image = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        if image:
            col1, col2, col3 = st.columns([3, 6, 1])
            col2.image(image, caption='Uploaded Image',width=250)

            # Save the uploaded image
            filename = image.name
            file_path = os.path.join('uploads', filename)
            with open(file_path, "wb") as f:
                f.write(image.getbuffer())
            try:
                # Perform prediction
                pred = prediction(file_path)

                # Fetch details based on prediction
                title = disease_info['disease_name'][pred]
                description = disease_info['description'][pred]
                prevent = disease_info['Possible Steps'][pred]
                image_url = disease_info['image_url'][pred]
                supplement_name = supplement_info['supplement name'][pred]
                supplement_image_url = supplement_info['supplement image'][pred]
                supplement_buy_link = supplement_info['buy link'][pred]
                if title!='Background Without Leaves':
                    # Display results
                    col1, col2, col3 = st.columns([2, 6, 1])
                    col2.markdown(f"<h2 style='color:red;'>{title}</h2>", unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <div style="text-align: justify; padding: 10px; background-color: #d3e876; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                            <h2 style="color: #111df7; font-size: 20px;"><b>Disease Description:</b></h2>
                            <p style="color: black; font-size: 15px;"><b>{description}</b></p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.write(f"")
                    st.markdown(
                        f"""
                        <div style="text-align: justify; padding: 10px; background-color: #ffa1ef; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                            <h2 style="color: #111df7; font-size: 20px;"><b>Prevntion Steps:</b></h2>
                            <p style="color: black; font-size: 15px;"><b>{prevent}</b></p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.write(f"")
                    st.markdown(
                        f"""
                        <div style="text-align: center; padding: 8px; background-color: #ffd5a1; border-radius: 30px; border: 1.5px solid black; margin-bottom: 10px;">
                            <h2 style="color: #111df7; font-size: 20px;"><b>Recommended Supplement:</b> {supplement_name}</h2>
                            <div style="text-align: center; margin-top: 10px;">
                                <img src="{supplement_image_url}" alt="Supplement Image" style="width: 300px; height: auto; border-radius: 15px; border: 1px solid black;">
                            </div>
                            <div style="margin-top: 15px;">
                                <a href="{supplement_buy_link}" target="_blank" style="text-decoration: none;">
                                    <button style="background-color: red; color: white; font-size: 16px; padding: 10px 20px; border: none; border-radius: 10px; cursor: pointer;">
                                        Buy Supplement Here
                                    </button>
                                </a>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f"<h1 style='text-align: center; color:red;'>No Disease Detected</h1>", unsafe_allow_html=True)
                    st.error('Kindly upload a valid image of a plant leaf')
            except:
                st.error('Invalid Image')
    elif selected_tab == "Plant Growth Tips":
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://static.vecteezy.com/system/resources/thumbnails/029/109/949/small_2x/wild-pristine-evergreen-forest-ai-generated-photo.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;  /* Ensure the background covers the whole screen */
            background-color: rgba(255, 255, 255, 0.6); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
        )
        with st.form('About Us'):
            # Contact Us Form
            st.subheader("Plant Growth Guide")
            class_labels = ['Mango', 'Banana', 'Apple', 'Orange', 'Pomegranate', 'Papaya', 'Guava', 'Grapes', 'Watermelon', 'Pineapple', 'Coconut', 'Lemon', 'Strawberry', 'Kiwi', 'Cherry', 'Peach', 'Plum', 'Pear', 'Lychee', 'Dragon Fruit', 'Avocado', 'Raspberry', 'Blackberry', 'Cranberry', 'Blueberry', 'Apricot', 'Fig', 'Passion Fruit', 'Mandarin', 'Pumpkin', 'Cucumber', 'Tomato', 'Carrot', 'Onion', 'Potato', 'Spinach', 'Cabbage', 'Broccoli', 'Lettuce', 'Capsicum', 'Chili', 'Garlic', 'Ginger', 'Coriander', 'Mint', 'Basil', 'Thyme', 'Rosemary', 'Lavender', 'Aloe Vera', 'Money Plant', 'Snake Plant', 'Spider Plant', 'Peace Lily', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium',
                            'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant',
                            'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos', 'ZZ Plant', 'Fiddle Leaf Fig', 'Monstera', 'Philodendron', 'Calathea', 'Succulents', 'Cactus', 'Bonsai', 'Money Tree', 'Lucky Bamboo', 'Orchid', 'Anthurium', 'Peace Lily', 'Snake Plant', 'Spider Plant', 'Rubber Plant', 'Pothos',
                            'Paddy', 'Wheat', 'Barley', 'Maize', 'Rice', 'Sorghum', 'Pearl millet', 'Finger millet', 'Foxtail millet', 'Proso millet', 'Kodo millet', 'Barnyard millet', 'Little millet', 'Brown top millet', 'Buckwheat', 'Job’s tears', 'Amaranth', 'Quinoa', 'Triticale', 'Oats', 'Rye', 'Canary seed', 'Wild rice', 'Spelt', 'Teff', 'Millet', 'Sesame', 'Sunflower', 'Safflower', 'Flax', 'Chia', 'Poppy', 'Mustard', 'Cotton', 'Jute', 'Hemp', 'Kenaf', 'Ramie', 'Abaca', 'Coir', 'Sisal', 'Henequen']
            #make slecetion
            class_labels = list(set(class_labels))
            #sort the list
            class_labels.sort()
            col1, col2 = st.columns(2)
            plant = col1.selectbox('Select Plant', class_labels, key='plant')
            query = f"{plant} plant care"
            if st.form_submit_button('Search Videos',type='primary'):
                videos = fetch_youtube_videos(query)

                # Display videos in rows of 3
                for i in range(0, len(videos), 2):
                    cols = st.columns(2)  # Create 3 columns
                    for j, video in enumerate(videos[i:i+2]):  # Iterate over videos for the current row
                        with cols[j]:
                            st.video(f"https://www.youtube.com/watch?v={video['video_id']}")
    

    elif selected_tab=='Logout':
        # Logout functionality
        st.session_state.clear()  # Clear session state to "log out"
        st.experimental_rerun()