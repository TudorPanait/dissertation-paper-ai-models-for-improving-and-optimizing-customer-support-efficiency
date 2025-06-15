import os
from dotenv import load_dotenv

import streamlit as st
import parselmouth
import tempfile
import numpy as np
from openai import OpenAI
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from datetime import timedelta

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def header():
    st.set_page_config(page_title="Speech Assist", page_icon=":microphone:")
    st.title("Speech Assist")
    st.write("This page is dedicated to analyzing vocal profiles and providing feedback for call-center agents.")
    load_dotenv()

def analyze_audio(wav_path):
    sound = parselmouth.Sound(wav_path)
    duration = sound.duration
    pitch = sound.to_pitch()
    intensity = sound.to_intensity()
    harmonicity = sound.to_harmonicity_cc()
    formant = sound.to_formant_burg()

    pitch_values = pitch.selected_array['frequency']
    voiced_pitch = pitch_values[pitch_values > 0]
    mean_pitch = voiced_pitch.mean() if len(voiced_pitch) > 0 else 0
    min_pitch = voiced_pitch.min() if len(voiced_pitch) > 0 else 0
    max_pitch = voiced_pitch.max() if len(voiced_pitch) > 0 else 0
    pitch_range = max_pitch - min_pitch

    mean_intensity = intensity.values.mean()
    hnr = harmonicity.values[harmonicity.values > 0].mean() if np.any(harmonicity.values > 0) else 0
    voiced_ratio = len(voiced_pitch) / len(pitch_values) if len(pitch_values) > 0 else 0

    pauses = np.where(intensity.values[0] < 25)[0]
    pause_ratio = len(pauses) / len(intensity.values[0])

    return {
        "Duration (s)": duration,
        "Mean Pitch (Hz)": mean_pitch,
        "Pitch Range (Hz)": pitch_range,
        "Mean Intensity (dB)": mean_intensity,
        "HNR (dB)": hnr,
        "Voiced Time (%)": voiced_ratio * 100,
        "Pause Ratio (%)": pause_ratio * 100
    }

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model="gpt-4o-mini-transcribe",
            response_format="text"
        )
    return response

def give_feedback(results, wpm):
    feedback = []

    if results["Mean Pitch (Hz)"] < 120:
        feedback.append("🟡 Try raising your pitch — you may sound flat or monotone.")
    if results["Pitch Range (Hz)"] < 30:
        feedback.append("🟡 Vary your tone more to sound engaging.")
    if wpm > 170:
        feedback.append("🔴 You're speaking too fast — aim for 130–160 wpm.")
    elif wpm < 110:
        feedback.append("🟡 You're speaking slowly — try to pick up the pace.")
    if results["HNR (dB)"] < 10:
        feedback.append("🔴 Low HNR — your voice may sound breathy or unclear.")
    if results["Pause Ratio (%)"] > 20:
        feedback.append("🟡 There are a lot of pauses — try to smooth your delivery.")

    return feedback

def main():
    st.subheader("Analyze Your Speech")
    audio_data = st.audio_input("Record your voice")

    if audio_data:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
            tmp_wav.write(audio_data.getvalue())
            wav_path = tmp_wav.name

        with st.spinner("Analyzing your speech..."):
            results = analyze_audio(wav_path)
            transcript = transcribe_audio(wav_path)
            word_count = len(transcript.split())
            duration_min = results["Duration (s)"] / 60
            wpm = word_count / duration_min if duration_min > 0 else 0
            results["Estimated Speaking Rate (wpm)"] = wpm

        st.subheader("💬 Transcript")
        st.info(transcript)

        st.subheader("📈 Acoustic Metrics")
        for key, value in results.items():
            st.write(f"**{key}:** {round(value, 2)}")

        st.subheader("🧠 Feedback")
        feedback = give_feedback(results, wpm)
        if feedback:
            for tip in feedback:
                st.write(f"{tip}")
        else:
            st.success("✅ Great job! Your vocal delivery and quality look excellent.")

header()
main()