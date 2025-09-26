# Python_Cord-19_Analysis

A Python project that explores the CORD-19 dataset through data cleaning, analysis, and visualization, with an interactive Streamlit app for insights on COVID-19 research papers.

## Overview

This project analyzes the **CORD-19 dataset** (`metadata.csv` only) to explore COVID-19 related research papers.

It follows a step-by-step data science workflow:

1. Data loading and exploration
2. Data cleaning and preparation
3. Analysis and visualization
4. Streamlit application for interactive exploration

## Project Structure

```
Python_Cord-19_Analysis/
│
├── metadata.csv          # Dataset file
├── cord19_analysis.py    # Main Python script (analysis + Streamlit app)
├── requirements.txt      # Required Python libraries
├── outputs/              # Folder for generated plots and word clouds
│   ├── publications_by_year.png
│   ├── top_journals.png
│   ├── wordcloud.png
│   └── distribution_by_source.png
└── README.md             # Project documentation
```

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/NJAU-NICKSON/Python_Cord-19_Analysis.git

cd Python_Cord-19_Analysis

pip install -r requirements.txt
```

## Running the Script (Static Analysis)

Run the Python script for analysis:

```bash
python cord19_analysis.py
```

This will generate plots and save them in the `outputs/` folder.

## Running the Streamlit App (Interactive Dashboard)

Launch the Streamlit application for interactive exploration:

```bash
streamlit run cord19_analysis.py
```


This will open a local web app in your browser where you can:

* Explore publications by year
* View top journals publishing COVID-19 research
* Generate a word cloud of paper titles
* Analyze the distribution of paper counts by source
You can download the dataset from Kaggle:  
[CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)


### Required Tools

* Python 3.7+  
* pandas (data manipulation)  
* matplotlib / seaborn (visualization)  
* Streamlit (web application)  
* Jupyter Notebook (optional, for exploration)  


Install the required packages:

```bash
pip install pandas matplotlib seaborn streamlit

## Expected Outputs

* Publications by Year (bar chart)
* Top Journals Publishing COVID-19 Research (bar chart)
* Word Cloud of Paper Titles
* Distribution of Paper Counts by Source

## Reflection

This project demonstrates:

* Basic data wrangling with **Pandas**
* Handling missing data
* Visualization with **Matplotlib**, **Seaborn**, and **WordCloud**
* Building an interactive app with **Streamlit**

