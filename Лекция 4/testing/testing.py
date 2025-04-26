from random import shuffle
from datetime import datetime

def get_user_choice() -> int:
    while True:
        user_input = input()
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 5:
                return choice
            print("Должна быть введена цифра от 1 до 5!")
        else:
            print("Введено не число!")

def load_questions(filename: str) -> list:
    questions = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        if lines[i][0].isdigit() and '.' in lines[i]:
            question_text = lines[i].split('.', 1)[1].strip()
            options = []
            for j in range(1, 6):
                options.append(lines[i + j].split('.', 1)[1].strip())
            answer_line = lines[i + 6]
            correct_indices = []
            if "или" in answer_line:
                parts = answer_line.split(":")[1].split("или")
                correct_indices = [int(part.strip()) for part in parts]
            else:
                correct_indices = [int(answer_line.split(":")[1].strip())]
            correct_answers = [options[idx - 1] for idx in correct_indices]
            questions.append({
                "question": question_text,
                "options": options,
                "correct_answers": correct_answers
            })
            i += 7
        else:
            i += 1

    shuffle(questions)
    for q in questions:
        shuffle(q["options"])
    return questions

def save_results(filename: str, start_time: datetime, end_time: datetime, total: int, correct: int) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Время начала теста: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Время окончания теста: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Общее количество вопросов: {total}\n")
        file.write(f"Количество правильных ответов: {correct}\n")
        file.write(f"Процент правильных ответов: {correct / total * 100:.2f}%\n")

def main():
    quiz_questions = load_questions("questions.txt")
    total_questions = len(quiz_questions)
    correct_count = 0
    start_time = datetime.now()

    for index, question in enumerate(quiz_questions, start=1):
        print(f"\nВопрос {index}/{total_questions}: {question['question']}")
        for option_num, option in enumerate(question["options"], start=1):
            print(f"{option_num}. {option}")
        user_choice = get_user_choice()
        chosen_option = question["options"][user_choice - 1]
        if chosen_option in question["correct_answers"]:
            correct_count += 1
            print("Правильно!")
        else:
            print("Неправильно")
        if index != total_questions:
            print("Переходим к следующему вопросу...")

    end_time = datetime.now()
    print("\nТестирование завершено!")
    print(f"Общее количество вопросов: {total_questions}")
    print(f"Количество правильных ответов: {correct_count}")
    print(f"Процент правильных ответов: {correct_count / total_questions * 100:.2f}%")

    save_results("result.txt", start_time, end_time, total_questions, correct_count)

if __name__ == "__main__":
    main()
