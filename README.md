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

Pipeline: The data is stored in Cloud Storage and using the BigQuery Data Transfer Service it is moved to BigQuery for processing and analysis. DataPrep preprocesses and transforms the data, returning it to a separate table within BigQuery.

Deployment: The source files are stored in Github, pushed to Cloud Source Repositories, and utilizing a trigger the app automatically deploys.

Interface: Python (w/Flask) and HTML comprise the front end. The model is stored in AutoML Tables. When a user inputs data into the required fields to yield a prediction, the data is sent to the model and the model returns a probability of churn. The model used for predictions has an accuracy of 80%.

# Authors

The author of this project is Michael Martley.

