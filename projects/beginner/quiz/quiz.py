QUESTIONS = {
    "Python uses indentation for code blocks": "true",
    "List is immutable": "false",
}


def score_answers(answers: dict[str, str]) -> tuple[int, int]:
    score = 0
    for question, correct in QUESTIONS.items():
        if answers.get(question, "").strip().lower() == correct:
            score += 1
    return score, len(QUESTIONS)


if __name__ == "__main__":
    sample = {
        "Python uses indentation for code blocks": "true",
        "List is immutable": "false",
    }
    print(score_answers(sample))
