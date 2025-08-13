Hybrid E-commerce Recommender System
A production-ready REST API that serves advanced, hybrid product recommendations by combining collaborative filtering with NLP-powered content analysis of user reviews.This project demonstrates an end-to-end MLOps workflow, from raw data processing and model training to containerization and API deployment. It's designed to be a robust and scalable solution for providing personalized e-commerce recommendations.
🚀 Key Features
Hybrid Recommendation Model:Collaborative Filtering: Uses user-item interaction data (ratings) to find similar users and recommend items they liked (scikit-learn).
Content-Based Filtering: Employs Natural Language Processing (NLP) to extract key features from product reviews and recommend items with similar praised attributes (scikit-learn TF-IDF).
Production-Ready API: A high-performance, asynchronous API built with FastAPI to serve recommendations with low latency.
Containerized & Portable: Fully containerized with Docker, ensuring consistent and reliable deployment across any environment.
Memory Efficient: Built to handle large datasets by processing data in chunks and using memory-efficient sparse matrices for model training.🛠️ Built WithThis project utilizes a modern data science and MLOps stack:Backend: PythonAPI Framework: FastAPIMachine Learning: Scikit-learnData Manipulation: Pandas, NumPyDeployment: Docker🏁 Getting StartedFollow these instructions to get a local copy up and running for development and testing.PrerequisitesDocker Desktop: You must have Docker Desktop installed and running on your machine. Download it here.Dataset: Download the "Electronics" 5-core dataset from the Amazon Product Data page https://nijianmo.github.io/amazon/index.html.
 
Unzip it and place the Electronics_5.json file inside the data/ folder.

cd recommender-project

Run the Data Processing NotebookOpen and run all the cells in the notebooks/01_process_data.ipynb notebook. This will generate the necessary model files and save them in the saved_models/ directory.Build the Docker ImageFrom the root of the project directory, run the build command:docker build -t recommender-api .

Run the Docker ContainerStart the container in detached mode:docker run -p 8000:80 -d --name my-recommender-app recommender-api

🕹️ Usage
Your recommender API is now live and running on your local machine!Interactive Docs (Swagger UI):Open your web browser and navigate to http://localhost:8000/docs.This is an interactive interface where you can test the API endpoints directly.Making a Request:Expand the /recommend/{user_id} endpoint.Click "Try it out".Enter a user_id from the dataset (you can find valid IDs in the df_sample DataFrame in the notebook).Click "Execute". You will see the JSON response with a list of recommended product IDs.
