import tkinter as tk

questions = [
    "What is the capital of France?",
    "What does CPU stand for?",
    "What is 5 + 7?",
    "What language is used for web apps?",
    "What does RAM stand for?"
]

answers = [
    "paris",
    "central processing unit",
    "12",
    "javascript",
    "random access memory"
]

index = 0
score = 0

def submit_answer():
    global score
    user = entry.get().lower().strip()
    if user == answers[index]:
        result_label.config(text="Correct")
        score += 1
    else:
        result_label.config(text="Incorrect")

def next_question():
    global index
    index += 1
    if index < len(questions):
        question_label.config(text=questions[index])
        entry.delete(0, tk.END)
        result_label.config(text="")
    else:
        question_label.config(text="Quiz Finished")
        entry.pack_forget()
        submit_button.pack_forget()
        next_button.pack_forget()
        result_label.config(text="You got " + str(score) + " out of " + str(len(questions)) + " correct")

root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text=questions[index], font=("Arial", 16))
question_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack(pady=5)

next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()