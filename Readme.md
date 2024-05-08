# Employee Recruitment with Machine Learning | Job Placement with Python | HR Talent Acquisition System

This repository contains code for modeling employee recruitment using machine learning techniques, detailed in the provided notebook file (`Recursos_Humanos.py`). Additionally, it includes Docker configurations for containerization.

## Modeling Approach

The modeling process involves the following steps:

1. **Data Preprocessing**: Cleaning and preparing the dataset for analysis, including handling missing values, encoding categorical variables, and scaling numerical features.

2. **Model Training**: Training machine learning models using the preprocessed dataset. Models such as k-nearest neighbors, decision trees, support vector machines, random forests, Gaussian naive Bayes, and logistic regression are explored.

3. **Model Evaluation**: Evaluating model performance using techniques such as confusion matrices and heatmap visualizations.

4. **Deployment**: Saving trained models and preprocessing transformers for future use.

The modeling approach is detailed in the provided notebook (`Recursos_Humanos.py`).

## Docker Configuration

The Dockerfile defines the environment and dependencies required to run the modeling code inside a Docker container. The Docker Compose file simplifies the process of running the container.

### Instructions for Building and Running with Docker:

```bash
# Build the Docker image:
docker build -t doby .

# Run the Docker container:
docker run -p 8000:5000 doby
