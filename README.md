# Sepsis Classification Machine Learning Project

## Overview

This project focuses on early sepsis detection and classification using machine learning techniques. The goal is to develop a robust model capable of predicting the likelihood of sepsis based on patient health metrics and demographics. The machine learning model is integrated into a FastAPI-based web application, providing real-time sepsis risk predictions for healthcare professionals.

## Table of Contents

- [Business Understanding](#business-understanding)
- [Sepsis Overview](#sepsis-overview)
- [Objectives](#objectives)
- [Methodology](#methodology)
- [Integration and Deployment](#integration-and-deployment)
- [Dataset Exploration and Preparation](#dataset-exploration-and-preparation)
- [Hypotheses and Questions](#framing-the-research-hypotheses-and-questions)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Univariate Analysis](#univariate-analysis)
- [Bivariate Analysis](#bivariate-analysis)
- [Model Development](#model-development)
- [Model Evaluation](#model-evaluation)
- [Web Application Interface](#web-application-interface)


## Business Understanding

Sepsis is a life-threatening condition triggered by the body's extreme response to infection. Early detection is crucial for better patient outcomes. This project aims to provide healthcare professionals with a tool for timely sepsis risk prediction and decision support.

## Sepsis Overview

Sepsis is characterized by widespread inflammation, organ damage, and potential organ failure. Symptoms include fever, rapid heart rate, breathing issues, low blood pressure, and altered mental status. Treatment involves antibiotics, fluids, and supportive care.

## Objectives

1. Understand the data.
2. Develop a precise machine learning model for sepsis prediction.
3. Integrate the model into a FastAPI-based web application.
4. Provide real-time sepsis risk predictions for healthcare professionals.

## Methodology

Follow a structured approach:
- Data Understanding
- Data Preparation
- Model Development
- Model Evaluation
- Integration and Deployment

## Integration and Deployment

5. **FastAPI Integration:**
   - Integrate the trained machine learning model into a FastAPI-based web application.
   - Create a user-friendly interface for healthcare professionals.


## Dataset Exploration and Preparation

- **Loading the Data:**
  - Dataset: `Patients_Files_Train.csv`
  - Records: 599 patients with health metrics and demographic information.
  
- **Understanding the Columns:**
  - Patient Identifiers, Health Metrics, Blood Work Results, Demographic Data, Target Variable (Sepsis).

- **Preliminary Analysis:**
  - Basic statistics to understand data distribution and potential patterns.
  
- **Data Quality Checks:**
  - Confirm no missing values or duplicate entries for data integrity.

## Framing the Research: Hypotheses and Questions

Set clear objectives, hypotheses, and questions to guide the research.

## Exploratory Data Analysis

- **Imbalance in Sepsis Cases:**
  - Identify and address the imbalance in the dataset.

## Univariate Analysis

- Examine each variable individually to understand its distribution and characteristics.

## Bivariate Analysis

- Explore relationships between different factors and the occurrence of sepsis.

## Model Development

- Select and implement a suitable machine learning classification model for sepsis prediction.

## Model Evaluation

- Assess model performance using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.

## Web Application Interface

- User-friendly interface for healthcare professionals to input patient data and obtain real-time sepsis risk predictions.


