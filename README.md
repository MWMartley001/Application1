# Churn Probability Estimator on GCP

[![CircleCI](https://circleci.com/gh/MWMartley001/Application1.svg?style=svg)](https://circleci.com/gh/MWMartley001/Application1)

# About

The Churn Probability Estimator on GCP is an application that a user can provide inputs to and receive the probability of a customer 
churn for a specific use-case. The probability is the result of GCP's AutoML tool (from a trained model) based on a dataset from 
Kaggle which can be found here: https://www.kaggle.com/blastchar/telco-customer-churn

The idea behind the project is to demonstrate the ability to use GCP's AutoML tool and provide an application for a company (such as Telco) to be able to estimate the risk of losing a customer. 

# About the Data

The dataset includes over 7040 observations, with both categorical and numeric data. A few examples of the attributes include: senior citizen (boolean), tenure (how long they have been a customer, monthly charges (the monthly bill), and there are multiple columns for types of billing (monthly, one-year, two-year). The dependent variable is churn, or whether the customer cancelled their service with the company. 

# System Overview

Pipeline: The pipeline behind the model is simple. The original dataset is stored on Cloud Storage, and on a monthly basis the data is transferred to BigQuery (using Data Transfer) and processed using Dataprep (from BigQuery and back to BigQuery) to prepare the data for modeling in AutoML tables. The Dataprep job transforms and preprocesses the data, also making it available in BigQuery for analysis. This process emulates a batch processing system using a basic ETL pipeline to a warehouse utility.

The application is stored in Github as well as GCP Cloud Repositories. For development, CircleCI is integrated for continuous integration and App Engine enables continuous deployment using a .yaml file. Ultimately, the source code can be modified in Github and the results are immediately applied to the application. The code for the front-end is Python (utilizing Flask) and HTML. 

# Authors

The author of this project is Michael Martley.

