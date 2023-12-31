import numpy as np
import pandas as pd
import tracemalloc
import librosa
import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from transformers import Wav2Vec2Processor
import datetime
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
import tkinter as tk

df = pd.read_csv('C:\\Users\\User\\Downloads\\transformers-main\\filter_data.csv', index_col=0)

# Defining record function
def recommend():
    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 7
    x = str(input("number of input"))
    print("Speak about the movies you like ")
    recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)
    sd.wait()
    write(f"record_{x}.wav", freq, recording)
    tokenizer = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    # Speech pre-processing
    speech, fs = sf.read(f"record_{x}.wav")
    if len(speech.shape) > 1:
        print(speech)
        speech = speech[:, 0] + speech[:, 1]
        print(sf)
    if fs != 16000:
        speech = librosa.resample(speech, fs, 16000)

    # Inference
    input_values = tokenizer(speech, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)

    tracemalloc.start()
    start = datetime.datetime.now()
    transcription = tokenizer.decode(predicted_ids[0])
    end = datetime.datetime.now()
    time_cons = end - start
    memory_consm = tracemalloc.get_traced_memory()
    current, peak = memory_consm
    tracemalloc.stop()

    bert = SentenceTransformer('distilbert-base-nli-mean-tokens')
    sentence_embeddings = np.load("embeddings_movies_Dataset.npy")
    print("\nThis is the transcribed text from your speech input : \n",transcription)
    # Compute similarity
    embed = bert.encode([transcription.lower()])
    cosine_scores = cosine_similarity(embed, sentence_embeddings)
    cosine_scores = torch.tensor(cosine_scores)  # Convert to torch.Tensor
    top5_matches = torch.argsort(cosine_scores, dim=-1, descending=True).tolist()[0][1:6]
    
    # Retrieve recommended movies
    recommended_movies = df.iloc[top5_matches,0:5]
    print("\nHere are the list of movie suggestions for you to watch according to your interest: \n",recommended_movies)
    # Return the recommended movies
    #return recommended_movies

def main():
    recommend()


if __name__ == "__main__":
    main()
