from pydub import AudioSegment
from textblob import TextBlob


def count_words(text):
    return len(text.split())


def get_audio_duration(audio_file):
    audio = AudioSegment.from_file(audio_file)
    return len(audio) / 1000


def calculate_wpm(word_count, duration):
    if duration == 0:
        return 0

    return word_count / (duration / 60)


def speaking_speed_feedback(wpm):

    if wpm < 100:
        return (
            "🐢 Too Slow",
            "Try speaking a little faster."
        )

    elif wpm <= 160:
        return (
            "✅ Good",
            "Excellent speaking speed!"
        )

    else:
        return (
            "🚀 Too Fast",
            "Try slowing down slightly."
        )


def detect_filler_words(text):

    fillers = [
        "um",
        "uh",
        "like",
        "you know",
        "actually",
        "basically",
        "so",
        "well"
    ]

    text = text.lower()

    result = {}

    for word in fillers:
        result[word] = text.count(word)

    return result


def analyze_sentiment(text):

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "😊 Positive"

    elif polarity < 0:
        sentiment = "😞 Negative"

    else:
        sentiment = "😐 Neutral"

    confidence = abs(polarity) * 100

    return sentiment, confidence