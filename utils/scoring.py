# ==========================================
# Overall Interview Score
# ==========================================

def calculate_score(wpm, filler_count):
    """
    Calculate the overall interview score out of 100.
    """

    score = 100

    # ----------------------------------
    # Speaking Speed Score
    # ----------------------------------

    if wpm < 120:
        score -= 20

    elif wpm > 160:
        score -= 20

    # ----------------------------------
    # Filler Word Penalty
    # ----------------------------------

    score -= filler_count * 2

    # ----------------------------------
    # Minimum Score = 0
    # ----------------------------------

    if score < 0:
        score = 0

    return score


# ==========================================
# Score Feedback
# ==========================================

def score_feedback(score):
    """
    Returns performance status and feedback
    based on the interview score.
    """

    if score >= 90:
        status = "🟢 Excellent"
        feedback = (
            "Outstanding interview performance! "
            "Keep maintaining this level."
        )

    elif score >= 75:
        status = "🔵 Very Good"
        feedback = (
            "Good job! A little more practice can "
            "make your interview even better."
        )

    elif score >= 60:
        status = "🟡 Good"
        feedback = (
            "Your performance is decent, but there "
            "is room for improvement."
        )

    elif score >= 40:
        status = "🟠 Average"
        feedback = (
            "Practice speaking more confidently and "
            "reduce filler words."
        )

    else:
        status = "🔴 Needs Improvement"
        feedback = (
            "Keep practicing your interview skills. "
            "Focus on speaking speed, clarity, and confidence."
        )

    return status, feedback