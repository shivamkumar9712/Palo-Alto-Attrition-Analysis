Workforce Attrition Patterns and Risk Hotspot Analysis
📌 Project Overview

Workforce Attrition Patterns and Risk Hotspot Analysis is a data analytics project focused on exploring employee attrition patterns and identifying workforce segments with comparatively higher observed attrition rates.

The project uses a supplied workforce dataset containing 1,470 employee records and 31 attributes. The analysis examines demographic, professional, workload, mobility, satisfaction, and career-related factors associated with employee attrition.

The project follows a complete data analytics workflow:

Dataset → Data Validation → Exploratory Data Analysis → Attrition Hotspot Analysis → Interactive Dashboard → Insights

🎯 Problem Statement

Employee attrition can create challenges related to workforce stability, recruitment costs, productivity, employee workload, and organizational knowledge.

Simply knowing the overall attrition rate is not sufficient to understand which workforce segments experience higher levels of employee exits.

This project analyzes employee-level workforce data to identify patterns in attrition across factors such as:

Age
Department
Job Role
Tenure
Overtime
Business Travel
Distance From Home
Job Satisfaction
Work-Life Balance
Marital Status
Career Progression

The objective is to identify attrition hotspots and present the findings through an interactive dashboard.

🎯 Project Objectives

The main objectives of this project are:

Analyze the overall employee attrition rate.
Validate the quality and structure of the supplied dataset.
Explore attrition across demographic characteristics.
Analyze attrition by department and job role.
Examine the relationship between attrition and employee tenure.
Investigate workload and mobility-related patterns.
Identify workforce segments with comparatively higher observed attrition.
Develop an interactive Streamlit dashboard.
Present analytical findings in a clear and accessible format.
Provide recommendations for further workforce investigation.
📊 Dataset

The project uses the supplied CSV dataset:

Palo Alto Networks.csv

Dataset Summary
Metric	Value
Total Employees	1,470
Total Attributes	31
Employees Exited	237
Employees Retained	1,233
Overall Observed Attrition Rate	16.12%
Missing Values	None identified
Duplicate Records	None identified
Target Variable

The Attrition variable represents employee exit status:

0 → Employee Retained
1 → Employee Exited

Dataset provenance note: Although the supplied file is named Palo Alto Networks.csv, this project does not independently verify that the records represent actual Palo Alto Networks employees. The file is therefore treated as the supplied workforce dataset.

🔍 Key Findings

The exploratory analysis identified several notable patterns.

Overall Attrition

The overall observed attrition rate was approximately 16.12%.

Overtime

Employees working overtime had an observed attrition rate of approximately 30.5%, compared with approximately 10.4% among employees who did not work overtime.

Age

Employees aged 25 or below recorded an observed attrition rate of approximately 35.8%.

Tenure

Employees with 0–2 years at the company recorded an observed attrition rate of approximately 29.8%.

Job Role

Some job roles showed comparatively higher observed attrition:

Job Role	Observed Attrition Rate
Sales Representative	~39.8%
Laboratory Technician	~23.9%
Human Resources	~23.1%
Department
Department	Observed Attrition Rate
Sales	~20.6%
Human Resources	~19.0%
Research & Development	~13.8%
Business Travel

Employees who travelled frequently for business recorded an observed attrition rate of approximately 24.9%, compared with approximately 8.0% among employees who did not travel.

Distance From Home

Employees in the 21+ distance group recorded an observed attrition rate of approximately 22.1%, compared with approximately 13.8% among employees in the 0–5 group.

These findings represent descriptive associations within the supplied dataset and should not be interpreted as evidence that any individual factor directly causes employee attrition.

🛠️ Technologies Used
Programming Language
Python
Data Analysis
Pandas
NumPy
Data Visualization
Matplotlib
Seaborn
Plotly
Dashboard
Streamlit
Development Tools
Jupyter Notebook
Visual Studio Code
Git
GitHub

📁 Project Structure
Palo-Alto-Attrition-Analysis/
│
├── Palo Alto Networks.csv
├── Workforce_Attrition_Analysis.ipynb
├── app.py
├── requirements.txt
├── research_paper.md
└── README.md

File Description
File	Description
Palo Alto Networks.csv	Supplied workforce dataset
Workforce_Attrition_Analysis.ipynb	Jupyter Notebook containing EDA
app.py	Streamlit dashboard application
requirements.txt	Required Python packages
research_paper.md	Complete research paper
README.md	Project documentation
🔬 Exploratory Data Analysis

The Jupyter Notebook performs the following analysis:

Dataset loading
Dataset structure inspection
Data type validation
Missing-value analysis
Duplicate-value analysis
Descriptive statistics
Overall attrition analysis
Department analysis
Job-role analysis
Age analysis
Gender analysis
Marital-status analysis
Education analysis
Tenure analysis
Overtime analysis
Business-travel analysis
Distance analysis
Job-satisfaction analysis
Work-life-balance analysis
Career-progression analysis
Correlation analysis
Attrition hotspot identification
📊 Streamlit Dashboard

The project includes an interactive Streamlit dashboard that allows users to explore workforce attrition patterns dynamically.

Dashboard Features
Total employee KPI
Employees exited KPI
Overall attrition rate
Retained employee KPI
Department filter
Job-role filter
Overtime filter
Business-travel filter
Age filter
Years-at-company filter
Interactive Plotly charts
Department and job-role analysis
Demographic analysis
Tenure analysis
Workload analysis
Risk hotspot analysis
Filtered data download
Running the Dashboard

Install the required packages:

pip install -r requirements.txt

Run the Streamlit application:

python -m streamlit run app.py

The application will normally open at:

http://localhost:8501
📈 Attrition Hotspot Analysis

An attrition hotspot is defined in this project as a workforce segment with a comparatively high observed attrition rate within the supplied dataset.

Hotspots are examined across:

Department
Job Role
Age Group
Tenure Group
Overtime
Business Travel
Marital Status

The analysis considers both the attrition rate and the number of employees in the segment to provide appropriate context.

💡 Recommendations

Based on the observed patterns, the project recommends further investigation into:

Early-tenure employee retention
Overtime and workload management
High-attrition job roles
Business travel requirements
Employees with longer commuting distances
Career development opportunities
Job satisfaction
Work-life balance
Employee feedback and exit interviews
Regular data-driven attrition monitoring

These recommendations are intended as areas for further investigation rather than proof that a particular factor causes attrition.

⚠️ Limitations

The project has several limitations:

The analysis is based on a single supplied dataset.
The dataset contains 1,470 employee records.
The analysis is primarily descriptive.
Observed associations do not establish causality.
Some potentially important organizational factors are not available in the dataset.
The dataset may not represent current workforce conditions.
The project does not predict individual employee attrition.
The original organizational provenance of the supplied file has not been independently verified.

Future work could incorporate larger datasets, employee surveys, exit interviews, statistical significance testing, and machine-learning models.

🚀 Future Scope

Future improvements could include:

Building a machine-learning model for attrition prediction.
Performing statistical significance testing.
Adding employee survey and exit-interview data.
Adding advanced feature engineering.
Implementing model explainability using SHAP.
Adding automated dashboard reporting.
Comparing attrition trends across multiple datasets.
Adding time-based attrition analysis where historical data is available.
Developing automated alerts for changing attrition patterns.
📄 Research Paper

The complete research paper for this project is available in:

research_paper.md

It contains:

Abstract
Introduction
Problem Statement
Dataset
Data Validation and Methodology
Key Results
Demographic and Tenure Results
Workload and Mobility
Recommendations
Limitations
Conclusion
🎓 Project Outcome

This project demonstrates a complete data analytics workflow from raw workforce data to an interactive analytical dashboard.

It combines:

Data Cleaning → Exploratory Data Analysis → Visualization → Hotspot Identification → Dashboard Development → Business Insights

The project demonstrates how Python-based analytics and interactive visualization can be used to explore workforce attrition patterns and provide a structured foundation for further workforce analysis.

👤 Author

Shivam Kumar

Project

Workforce Attrition Patterns and Risk Hotspot Analysis

Tools

Python | Pandas | NumPy | Matplotlib | Seaborn | Plotly | Streamlit | Jupyter Notebook | GitHub

⚖️ Disclaimer

This project is intended for educational and analytical purposes. The findings represent patterns observed in the supplied dataset and should not be interpreted as causal conclusions, individual employee risk assessments, or verified claims about any specific organization.