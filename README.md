# Speech-Enabled-Movie-Recommendation-System

The Speech-Enabled Movie Recommendation System is a Python project that provides personalized movie recommendations based on user preferences using speech recognition and natural language processing techniques. With this system, users can simply speak about their movie preferences, and the system will generate tailored recommendations accordingly.

# Features
Convert user's spoken input into text using speech recognition.
Preprocess and tokenize the transcribed text.
Calculate similarity between user preferences and movie descriptions.
Provide top movie recommendations based on the similarity scores.
Requirements
Python 3.7 or above
Install the required libraries by running the command: pip install -r requirements.txt
# Usage
Make sure you have the movie dataset available in a CSV file. The dataset should include movie titles, genres, and descriptions.

Run the recommend() function in the code to start the recommendation process. The system will prompt you to speak about the movies you like.

The system will record your speech and convert it into text using speech recognition.

The transcribed text will be preprocessed, tokenized, and transformed into embeddings.

Cosine similarity will be calculated between your preferences and movie descriptions.

The system will provide you with the top movie recommendations based on the similarity scores.

# Code Explanation
The provided code (recommend.py) performs the following steps:

Imports the necessary libraries for data processing, speech recognition, natural language processing, and recommendation.

Loads the movie dataset from a CSV file.

Defines the recommend() function, which records the user's speech input and performs speech preprocessing.

Uses a pre-trained Wav2Vec2 model and tokenizer to convert the speech into text.

Preprocesses the transcribed text and computes the embedding using a pre-trained SentenceTransformer model.

Calculates the cosine similarity between the user's preferences and the movie descriptions.

Retrieves the top movie recommendations based on the similarity scores.

Displays the recommended movies to the user.

# Acknowledgments
The Speech-Enabled Movie Recommendation System is built using various open-source libraries and models, including:

Hugging Face Transformers: https://huggingface.co/transformers/
scikit-learn: https://scikit-learn.org/
sentence-transformers: https://www.sbert.net/


# Note
The provided code is a basic implementation of a speech-enabled movie recommendation system. It uses speech recognition and natural language processing techniques to convert user preferences into text and calculate similarity scores for movie recommendations.

Please note that the code can be further enhanced and customized based on specific requirements. Additional features, such as user profiles, ratings, and real-time updates, can be implemented to improve the recommendation system's accuracy and personalization.

Feel free to explore and modify the code to suit your needs. Happy recommending!




