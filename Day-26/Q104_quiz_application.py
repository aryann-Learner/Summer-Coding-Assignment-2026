# Q104 - Quiz application
questions = [
    ("What is the capital of India?", "delhi"),
    ("What is 2 + 2?", "4"),
    ("What language is used for web styling?", "css"),
]
score = 0
for q, ans in questions:
    user_ans = input(q + " ").strip().lower()
    if user_ans == ans:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {ans}")
print(f"Score: {score}/{len(questions)}")