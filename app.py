import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time



st.set_page_config(
    page_title="House Rent Prediction"
)

st.title("House Price Prediction")

# load the model
model = joblib.load("house_rent_model.pkl")
scaler = joblib.load("scaler.pkl")




st.write("Using this Web App, You can get House rent estimation of Indian Cities")

st.divider()


bhk = st.number_input("Enter the no. of BHK",min_value=1,step=1)
size = st.number_input("Enter the size of House(sq.ft):")

area_type_dict = {
    "Super Area":1,
    "Carpet Area":2,
    "Built Area":3

}



area_type_label = st.selectbox(
    "Area Type",
    ["Area Type"]+list(area_type_dict.keys())
)

if area_type_label == "Area Type":
    area_type = None

else:
    area_type = area_type_dict[area_type_label]


city_dict = {
    "Mumbai":1,
    "Chennai":2,
    "Bangalore":3,
    "Hyderabad":4,
    "Delhi":5,
    "Kolkata":6
}

city_label = st.selectbox(
    "City",
    ["City"]+list(city_dict.keys())
)

if city_label == "City":
    city = None

else:
    city = city_dict[city_label]



furnishing_dict = {
    "Unfurnished":1,
    "Semi-Furnished":2,
    "Furnished":3
}


furnished_label = st.selectbox(
    "Furnished Status",
    ["Furnished"]+list(furnishing_dict.keys())
)

if furnished_label == "Furnished Status":
    furnished = None

else:
    furnished = furnishing_dict[furnished_label]



tenant_dict = {
    "Bachelors/Family":2,
    "Bachelors":1,
    "Family":3
}


tenant_label = st.selectbox(
    "Tenant Preferred",
    ["Tenant Preferred"]+list(tenant_dict.keys())
)


if tenant_label == "Tenant Preferred":
    tenant = None

else:
    tenant = tenant_dict[tenant_label]


bathroom = st.number_input("Enter the no. of Bathrooms",min_value=1,step=1)

X = [bhk,size,area_type,city,furnished,tenant,bathroom]

st.divider()

predict = st.button("Press this Button to predict the salary")


if predict:
    with st.spinner("Wait for model to predict"):
        time.sleep(2.5)


        X1 = np.array([X])
        scaled_data = scaler.transform(X1)
        predicted_data = model.predict(scaled_data)

        st.metric(
        label="💰 Estimated Monthly Rent",
        value=f"₹ {int(predicted_data[0]):,}"
    )


else:
    "Please press the Predict Button for Prediction"
