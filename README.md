## Classification Modeling

#### Telecommunications ("TELCO") Dataset Analysis
----

##### Mijail Q. Mariano
##### github.com/mijailmariano

<br>

**<u>Project Description & Goals:</u>**

The purpose of this analysis was to explore the telco dataset through visualizations and statistical tests to identify potential influencers of customer churn.

**The term "churn"** in this analysis is defined as both:

<br>

1. Customers who have elected to end their service commitments with the telco company - as indicated in the "telco" dataset (past-tense) 
    
and...

2.  Given a set number of conditions, churn is also defined as predictions of customers who may potentially end services with the telco company at some future date (future-tense)

<br>

Given the insights from exploring the telco dataset I design a machine learning (ML) model using classification techniques with a goal of predicting customer churn with greater accuracy than that of a baseline accuracy rate (~74% accuracy). 

----
<u>**Key findings, takeaways, and recommendations:**</u>



----
**<u>Repository Roadmap:</u>**

Below is a file breakdown on how to best navigate this GitHub repository and the subsequent analysis. All code, data synthesis, and models can be found here for future reproduction or improvements:

1. **final_report.ipynb**

   Data Science pipeline overview document. Acts as an artifact of the statistical tests conducted, classification techniques used for machine learning models, key analysis takeaways, and recommendations.

2. **wrangle.ipynb**

   Jupyter Notebook used as the initial data acquisition file  which walks-through the process for creating the necessary data acquisition and cleaning functions.

3. **wrangle.py**

   Python file with functions needed to import, clean, and manipulate the telco dataset used in this analysis.

----
**<u>Initial Questions and Hypothesis:</u>**



----
### **Data Dictionary**

<br>

<u>Customer Demographic Information</u>

* **customer_id:** Customer ID

* **gender:** Customer gender 
  
  (male, female)

* **senior_citizen:** Whether the customer is a senior citizen or not
  
  (False, True)

* **partner:** Whether the customer has a partner or not 
  
  (Yes, No)

* **dependents:** Whether the customer has dependents or not 
  
  (Yes, No)

<br>

<u>Customer Account Information</u>

* **tenure (rounded):** Number of months the customer has been with the company

* **contract_type:** The contract term of the customer 
  
  (Month-to-Month, One Year, Two Year)

* **paperless_billing:** Whether the customer has paperless billing 
  
  (Yes, No)

* **payment_type:** The customer’s payment method 
  
  * Electronic Check ("E-check") 
  * Mailed Check
  * Bank Transfer (automatic)
  * Credit Card (automatic)

<br>

* **monthly_charges:** The amount charged to the customer monthly

* **total_charges:** The total amount charged to the customer to date

<br>

<u>Account Services</u>

* **phone_service:** Whether the customer has a phone service 
  
  (Yes, No)

* **multiple_lines:** Whether the customer has multiple lines 
  
  (Yes, No, No phone service)

* **internet_service_type:** Customer’s internet service provider 
  
  (DSL, Fiber Optic, No internet service)

* **online_security:** Whether the customer has online security 
  
  (Yes, No, No internet service)

* **online_backup:** Whether the customer has online backup 
  
  (Yes, No, No internet service)

* **device_protection:** Whether the customer has device protection 
  
  (Yes, No, No internet service)

* **tech_support:** Whether the customer has tech support 
  
  (Yes, No, No internet service)

* **streaming_tv:** Whether the customer has streaming TV 
  
  (Yes, No, No internet service)

* **streaming_movie:** Whether the customer has streaming movies 
  
  (Yes, No, No internet service)

