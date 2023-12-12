# Heart Disease Prediction

This program has used logistic regression, decision tree classifier and artificial intelligence algorithms with cross-validation to develop and train the models that could estimate the likelihood of heart disease based on important indicators associated with the condition. The models are then evaluated for its accuracy, precision, recall and auc scores. Logistic Model, which exhibits the highest scores in evaluation metrics, is selected for integration into the application for predicting heart disease.

- Sex (Male or Female)
- Age Category
- Body Mass Index (BMI)
- General health condition (Poor, Fair, Good, Very Good or Excellent)
- Hours of sleep (on average)
- Smoker 
    - Never smoked
    - Former smoker
    - Current smoker
- Alcohol drinker
  - For adult men: having more than 14 drinks per week
  - For adult women: having more than 7 drinks per week
- Have/had a stroke
- Have/had a diabetes
- Have/had an asthma
- Have/had a skin cancer
- Have/had a kidney disease (excluding kidney stones, bladder infection or incontinence)
- Doing physical activity or exercise during the past 30 days other than the regular job
- Difficulty walking or climbing stairs


## General info

The dataset selected for this project is obtained from the Behavioral Risk Factor Surveillance System (BRFSS) by the CDC. This health survey, operational since 1984, annually surveys more than 400,000 adults across all U.S. states and territories. The dataset includes information for 2022 and comprises vital factors associated with heart disease, such as diabetes, obesity, lack of physical activity, and excessive alcohol consumption.

Link of the dataset: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following Python packages.

For Jupyter file:
```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
pip install imblearn
pip install tensorflow
```

For web application:
```bash
pip install numpy
pip install pandas
pip install flask
pip install scikit-learn
pip install gunicorn (for Render)
```

## Program Execution

The project was deployed in Render to make it publicly available to the users. 

Link of the application: https://cardio-insight.onrender.com

To launch the heart disease application in the local machine:
```bash
python app.py
```

Note: Make sure to install all necessary Python libraries before executing the program

## Members
- Auradee Castro
- Bhumika Rajendra Babu  
- Miraj Sinya
- Olivia Deguit
- Roger Mais
