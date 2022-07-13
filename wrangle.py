# required modules:
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import env 
from env import user, password, host


def get_telco_data():
    # editing for "caching" exercise
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=[0])
    else:
        db_url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
        query = ''' 
        SELECT *
        FROM customers
        RIGHT JOIN contract_types using (contract_type_id)
        RIGHT JOIN payment_types using (payment_type_id)
        RIGHT JOIN internet_service_types using (internet_service_type_id)
        '''
        df = pd.read_sql(query, db_url)
        df.to_csv(filename)
        return df


def clean_telco_data(df):
    # converting columns to proper type 
    df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")
    df["senior_citizen"] = df["senior_citizen"].astype("bool")

    # replacing null values in total charges column
    filling_values = df[df.isnull().any(axis=1)].monthly_charges
    df["total_charges"] = df["total_charges"].fillna(df["monthly_charges"])

    # dropping unneeded columns
    df = df.drop(columns=['internet_service_type_id', 'payment_type_id', 'contract_type_id'])

    # renaming feature/column values for clarity
    df["payment_type"] = df["payment_type"].replace({
        'Mailed check': "Mailed Check", \
        'Credit card (automatic)': "Credit Card (automatic)", \
        'Electronic check': "E-Check", \
       'Bank transfer (automatic)': "Bank Transfer (automatic"}) 

    df["contract_type"] = df["contract_type"].replace({
        "Month-to-month": "Month-to-Month", "One year": "One Year", "Two year": "Two Year"})

    df["internet_service_type"] = df["internet_service_type"].replace({
        "Fiber optic": "Fiber Optic", "None": "No internet service"})
    
    return df


def train_validate_test_split(df):
    train_and_validate, test = train_test_split(
    df, test_size=0.2, random_state=123, stratify=df.churn)
    
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=123,
        stratify=train_and_validate.churn)

    return train, validate, test