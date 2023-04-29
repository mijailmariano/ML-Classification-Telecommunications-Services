## Machine Learning Classification Modeling - Predicting and Preventing Customer Attrition in Telecommunication Services

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

2.  Given a set number of conditions, churn is also defined as predictions of customers who may potentially end services with the telco company at some future date (future-tense)

<br>

Given the insights from exploring the telco dataset I design a machine learning (ML) model using classification techniques with a goal of predicting customer churn with greater accuracy than that of a baseline accuracy rate (~74% accuracy). 

----
<u>**Key Findings, Takeaways, and Recommendations:**</u>

<center>
<table>
  <thead>
    <tr>
      <th>Data Feature</th>
      <th>Statistical Test</th>
      <th>Degrees of Freedom</th>
      <th>P-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>internet_type</td>
      <td>ChiSquared</td>
      <td>6</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>tech_support</td>
      <td>ChiSquared</td>
      <td>6</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>streaming_movies</td>
      <td>ChiSquared</td>
      <td>6</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>payment_type</td>
      <td>ChiSquared</td>
      <td>8</td>
      <td>0.00</td>
  </tbody>
</table>
</center>


**<u>Takeaways</u>**

I conclude that there is a statistical association between the features studied in this analysis and customer churn. 

Hypothesis testing with features such as internet_type, tech_support, streaming_movies, and payment_type produced $\chi^2$ results of ~398, ~448, ~205, and ~373 respectively. This indicated to me that there is significant variability (difference) in the observed frequency vs. expected frequency also infering a dependency among customer churn and features tested.

**<u>Recommendations</u>**

1. Work to improve internet speeds and reliability - specifically across Telco's Fiber Optic infrastructure as this option appears to have a stronger statistical relationship to customer churn than the DSL option.
   
2. Encourage internet service customers to opt for the tech_support option in order to help remedy real-time internet issues, and/or provide customers an alternative internet option such as DSL in critical moments.

3. Eliminate Electronic Check ("E-Check") as a monthly payment option as this appears to have a relatively strong statistical association to customer churn. This is possibly due to customers taking additional steps such as login into a third-party website to pay their monthly bill and paying an additional fee for clearing the electronic check. 

4. Although streaming movies is very closely associated with whether or not a customer has internet with the company, it's still worth noting that more than 1/3 of all customers have chosen this option. Of which, these customers also churn at less rates than customers who do not chose to stream movies. 

    - My recommendation here would be to partner with leading film / streaming platforms to create selective releases only with the telco company and adverstise to non-movie streaming customers. By diversifying the movie streaming options, you potentially appeal to more customers. 

----
**<u>Repository Roadmap:</u>**

Below is a file breakdown on how to best navigate this GitHub repository and the subsequent analysis. All code, data synthesis, and models can be found here for future reproduction or improvements:

1. **final_report.ipynb**

   Data Science pipeline overview document. Project artifact of the hypothesis tests conducted, classification techniques used for machine learning models, key analysis takeaways, and recommendations.

2. **data_exploration.ipynb**

   Jupyter Notebook used as the data science pipeline file which walks-through the process for creating the necessary data acquisition and cleaning functions.

3. **acquire.py** 

    Python file that imports the neccessary telco dataset and subsequent features and outputs for modeling phase in the analysis. **Note:** you must first import the initial telco dataset from MySQL. When passed in the "acquire.get_telco_data()" function, the data is then stored locally as a .csv file and then referenced as a pd.Dataframe thereafter. 

4. **prepare.py**

   Python file with created functions needed to clean, and manipulate the telco dataset used in this analysis.


----
**<u>Initial Questions for Hypothesis Testing:</u>**

*Is there a relationship between ```internet``` options and whether or not a customer churns?*

*Is there a relationship between the ```streaming movies``` option and whether or not a customer churns?*

*Is there a relationship between the ```tech support``` option and whether or not a customer churns?*

*Is there a relationship between ```monthly payment``` options and whether or not a customer churns?*


----
## <center> **Data Dictionary** </center>

<br>

<u>Customer Demographic Information</u>

* **customer_id:** unique customer ID

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

* **contract_type:** A customer's contract terms 
  
  (Month-to-Month, One Year, Two Year)

* **paperless_billing:** Whether the customer has opted for paperless billing 
  
  (Yes, No)

* **payment_type:** A customer’s monthly bill payment method 
  
  * Electronic Check ("E-check") 
  * Mailed Check
  * Bank Transfer (automatic)
  * Credit Card (automatic)

<br>

* **monthly_charges:** The monthly service amount charged to the customer

* **total_charges:** The total amount charged to the customer to date

<br>

<u>Account Services</u>

* **phone_service:** Whether the customer has phone service
  
  (Yes, No)

* **multiple_lines:** Whether the customer has multiple lines on their account
  
  (Yes, No, No phone service)

* **internet_service_type:** The customer's internet service option
  
  (DSL, Fiber Optic, No internet service)

* **online_security:** Whether the customer has opted for the online security option
  
  (Yes, No, No internet service)

* **online_backup:** Whether the customer has opted for the online backup option
  
  (Yes, No, No internet service)

* **device_protection:** Whether the customer has device protection 
  
  (Yes, No, No internet service)

* **tech_support:** Whether the customer has tech support 
  
  (Yes, No, No internet service)

* **streaming_tv:** Whether the customer has streaming TV option on their account
  
  (Yes, No, No internet service)

* **streaming_movie:** Whether the customer has streaming movies option on their account
  
  (Yes, No, No internet service)

