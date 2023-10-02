# Movie Recommender System

This project implements a content-based movie recommender system using a Kaggle dataset. The user interface (UI) is developed using Streamlit, and the recommendation model is based on cosine similarity.

## Project Structure

```
├── data
│   └── movies.csv               # Kaggle dataset containing movie information
├── notebooks
│   └── Movie Recommender.ipynb   # Colab notebook for data exploration
│   └── movies.pkl and model.pkl  # picke file for model implementation
├── app.py                        # Streamlit application for UI
└── README.md                     # Project documentation
```

## Setup and Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/content-based-movie-recommender.git
    cd content-based-movie-recommender
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

4. Open the application in your browser: [http://localhost:8501](http://localhost:8501)

## Usage

1. Launch the Streamlit application following the setup instructions.
2. Enter the movie name in the provided input box and click "Recommend" to get a list of recommended movies based on content similarity.

## Model Training

The model uses cosine similarity to recommend movies based on their content. The training process involves:

1. **Data Preparation**: Loading and preprocessing the movie dataset (`movies.csv`).
2. **Feature Engineering**: Extracting relevant features such as genres, director, actors, and keywords.
3. **Cosine Similarity Calculation**: Computing cosine similarity between feature vectors.
4. **Model Persistence**: Saving the preprocessed data and model for future recommendations.

Refer to the `notebooks` directory for detailed steps in the `model_training.ipynb` notebook.

## Dataset

The dataset used in this project is the Kaggle Movies Dataset, which contains information about movies, including movieId, title, genres, director, actors, and keywords.

- Dataset: [Kaggle Movies Dataset](data/movies.csv)

## Acknowledgments

- Kaggle for providing the movies dataset used in this project.
- Streamlit for enabling rapid development of the user interface.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
