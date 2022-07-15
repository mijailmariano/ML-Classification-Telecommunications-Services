# importing libraries
import os

import pandas as pd
from skimpy import clean_columns

import numpy as np
from sklearn.model_selection import train_test_split




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
    
    df["churn"] = df["churn"].replace({"No": False, "Yes": True})

    return df


def dummy_columns(df):
    categorical_lst = [
        'internet_service_type', \
        'payment_type', \
        'contract_type', \
        'gender', \
        'partner', \
        'dependents', \
        'phone_service', \
        'multiple_lines', \
        'online_security', \
        'online_backup', \
        'device_protection', \
        'tech_support', \
        'streaming_tv', \
        'streaming_movies', \
        'paperless_billing']

    dummy_df = pd.get_dummies(df[categorical_lst])
    # cleaning column names for uniformity

    dummy_df = clean_columns(dummy_df, case = "snake")
    df = pd.concat([df, dummy_df], axis = 1)

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


def log_features():
    features = [ 
    'internet_service_type_fiber_optic', \
    'internet_service_type_dsl', \
    'internet_service_type_no_internet_service', \
    'payment_type_credit_card_automatic', \
    'payment_type_e_check', \
    'payment_type_mailed_check', \
    'payment_type_bank_transfer_automatic', \
    'streaming_movies_no_internet_service', \
    'streaming_movies_yes', \
    'streaming_movies_no',
    'tech_support_no_internet_service', \
    'tech_support_yes', \
    'tech_support_no']

    return features


'''to be used/explored in future testing'''
def new_model(df):
    df = df[[
    'churn', \
    'internet_service_type_fiber_optic', \
    'internet_service_type_no_internet_service', \
    'payment_type_credit_card_automatic', \
    'payment_type_e_check', \
    'payment_type_mailed_check', \
    'tech_support_no_internet_service', \
    'tech_support_yes', \
    'streaming_tv_no_internet_service', \
    'streaming_tv_yes']]

    return df

