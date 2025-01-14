import librosa
import numpy as np
import soundfile as sf

def extract_features(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_maen = np.mean(mfcc, axis=1)

    return mfcc_maen

def detect_ambulance_sound(audio_file, model_features):
    input_features = extract_features( audio_file)
    similarity = np.linalg.norm(input_features - model_features) 
    threshold = 10
    if similarity < threshold:
        return True
    else:
        return False

ambulance_model_features = nparray([ -200.24, 120.11, -245.15, -320.01, 180.13, 140.98, ...])
audio_file = "sample_audio.wav"

if detect_ambulance_sound(audio_file, ambulance_model_features):
    print("偵測到救護車聲音！")
else:
    print("未偵測到救護車聲音。")