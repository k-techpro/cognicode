from flask import Flask, render_template, request, redirect, url_for, session
import io
import contextlib

app = Flask(__name__)
app.secret_key = "cognicode_secret_key"


@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if email.endswith("@gmail.com") and len(password) >= 8:
            return redirect(url_for("home"))
        else:
            error = "Enter a valid Gmail and password with at least 8 characters."

    return render_template("auth.html", error=error)


@app.route("/home")
def home():
    return render_template(
        "home.html",
        user_name="Shakthi",
        user_email="kombaiyashakthi@gmail.com",
        status="Cognitive Explorer"
    )


@app.route("/level/<level>")
def level(level):
    return render_template("level.html", level=level)


@app.route("/analytics")
def analytics():
    sample_daily_time = [25, 40, 35, 50, 30, 65, 45]
    sample_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    return render_template(
        "analytics.html",
        daily_time=sample_daily_time,
        daily_labels=sample_days
    )


def get_problems():
    return {
        "python": [
            {
                "title": "Addition of Two Numbers",
                "question": "Write a Python program to print the sum of two numbers.",
                "description": "Create a simple Python program that stores two numbers in variables and prints their sum.",
                "difficulty": "Easy",
                "file_name": "main.py",
                "code": "a = 5\nb = 10\nprint(a + b)",
                "expected_output": "15",
                "hint": "Store the numbers in variables and use print(a + b).",
                "solution": "a = 5\nb = 10\nprint(a + b)",
                "main_hints": [
                    "Use two variables to store the numbers.",
                    "Use the + operator to add the values.",
                    "Use print() to display the result.",
                    "Check indentation and spelling carefully."
                ],
                "similar_questions": [
                    {
                        "title": "Similar Question 1",
                        "question": "Write a Python program to print the sum of 7 and 3.",
                        "starter_code": "a = 7\nb = 3\nprint(a + b)"
                    },
                    {
                        "title": "Similar Question 2",
                        "question": "Write a Python program to print the sum of 12 and 8.",
                        "starter_code": "a = 12\nb = 8\nprint(a + b)"
                    }
                ]
            },
            {
                "title": "Multiplication of Two Numbers",
                "question": "Write a Python program to print the product of two numbers.",
                "description": "Create a Python program that stores two numbers in variables and prints their multiplication result.",
                "difficulty": "Easy",
                "file_name": "main.py",
                "code": "a = 4\nb = 6\nprint(a * b)",
                "expected_output": "24",
                "hint": "Use the * operator for multiplication.",
                "solution": "a = 4\nb = 6\nprint(a * b)",
                "main_hints": [
                    "Use variables to store the two numbers.",
                    "Use the * operator for multiplication.",
                    "Print the result with print().",
                    "Check whether you used + by mistake."
                ],
                "similar_questions": [
                    {
                        "title": "Similar Question 1",
                        "question": "Write a Python program to print the product of 3 and 5.",
                        "starter_code": "a = 3\nb = 5\nprint(a * b)"
                    },
                    {
                        "title": "Similar Question 2",
                        "question": "Write a Python program to print the product of 2 and 9.",
                        "starter_code": "a = 2\nb = 9\nprint(a * b)"
                    }
                ]
            }
        ],
        "java": [
            {
                "title": "Print Sum in Java",
                "question": "Write a Java program to print the sum of two integers.",
                "description": "Use the main method and System.out.println to display the sum of two values.",
                "difficulty": "Moderate",
                "file_name": "Main.java",
                "code": (
                    "public class Main {\n"
                    "    public static void main(String[] args) {\n"
                    "        int a = 5;\n"
                    "        int b = 10;\n"
                    "        System.out.println(a + b);\n"
                    "    }\n"
                    "}"
                ),
                "expected_output": "15",
                "hint": "Use System.out.println(a + b); inside main().",
                "solution": (
                    "public class Main {\n"
                    "    public static void main(String[] args) {\n"
                    "        int a = 5;\n"
                    "        int b = 10;\n"
                    "        System.out.println(a + b);\n"
                    "    }\n"
                    "}"
                ),
                "main_hints": [
                    "Declare integer variables first.",
                    "Write code inside public static void main.",
                    "Use System.out.println() to print the sum.",
                    "End each statement with a semicolon."
                ],
                "similar_questions": [
                    {
                        "title": "Similar Question 1",
                        "question": "Write a Java program to print the sum of 8 and 2.",
                        "starter_code": (
                            "public class Main {\n"
                            "    public static void main(String[] args) {\n"
                            "        int a = 8;\n"
                            "        int b = 2;\n"
                            "        System.out.println(a + b);\n"
                            "    }\n"
                            "}"
                        )
                    },
                    {
                        "title": "Similar Question 2",
                        "question": "Write a Java program to print the sum of 14 and 6.",
                        "starter_code": (
                            "public class Main {\n"
                            "    public static void main(String[] args) {\n"
                            "        int a = 14;\n"
                            "        int b = 6;\n"
                            "        System.out.println(a + b);\n"
                            "    }\n"
                            "}"
                        )
                    }
                ]
            },
            {
                "title": "Print Product in Java",
                "question": "Write a Java program to print the product of two integers.",
                "description": "Use variables and System.out.println to display multiplication output.",
                "difficulty": "Moderate",
                "file_name": "Main.java",
                "code": (
                    "public class Main {\n"
                    "    public static void main(String[] args) {\n"
                    "        int a = 4;\n"
                    "        int b = 6;\n"
                    "        System.out.println(a * b);\n"
                    "    }\n"
                    "}"
                ),
                "expected_output": "24",
                "hint": "Use the * operator inside System.out.println.",
                "solution": (
                    "public class Main {\n"
                    "    public static void main(String[] args) {\n"
                    "        int a = 4;\n"
                    "        int b = 6;\n"
                    "        System.out.println(a * b);\n"
                    "    }\n"
                    "}"
                ),
                "main_hints": [
                    "Declare integer variables first.",
                    "Use the * operator for multiplication.",
                    "Print the result with System.out.println().",
                    "Check semicolons and braces carefully."
                ],
                "similar_questions": [
                    {
                        "title": "Similar Question 1",
                        "question": "Write a Java program to print the product of 3 and 5.",
                        "starter_code": (
                            "public class Main {\n"
                            "    public static void main(String[] args) {\n"
                            "        int a = 3;\n"
                            "        int b = 5;\n"
                            "        System.out.println(a * b);\n"
                            "    }\n"
                            "}"
                        )
                    },
                    {
                        "title": "Similar Question 2",
                        "question": "Write a Java program to print the product of 2 and 9.",
                        "starter_code": (
                            "public class Main {\n"
                            "    public static void main(String[] args) {\n"
                            "        int a = 2;\n"
                            "        int b = 9;\n"
                            "        System.out.println(a * b);\n"
                            "    }\n"
                            "}"
                        )
                    }
                ]
            }
        ],
        "css": [
            {
                "title": "Basic Page Styling",
                "question": "Write CSS to change the background color and center text on the page.",
                "description": "Use CSS properties to style the body and align content neatly.",
                "difficulty": "Easy",
                "file_name": "style.css",
                "code": "body {\n    background-color: #0a2b52;\n    color: white;\n    text-align: center;\n}",
                "expected_output": "styled",
                "hint": "Use background-color and text-align inside body.",
                "solution": "body {\n    background-color: #0a2b52;\n    color: white;\n    text-align: center;\n}",
                "main_hints": [
                    "Style the body selector.",
                    "Use background-color for page color.",
                    "Use text-align: center for alignment.",
                    "Add color if you want visible text."
                ],
                "similar_questions": [
                    {
                        "title": "Similar Question 1",
                        "question": "Write CSS to make the page background dark blue and text white.",
                        "starter_code": "body {\n    background-color: navy;\n    color: white;\n}"
                    },
                    {
                        "title": "Similar Question 2",
                        "question": "Write CSS to center all text and make it cyan.",
                        "starter_code": "body {\n    text-align: center;\n    color: cyan;\n}"
                    }
                ]
            },
            {
                "title": "Button Styling",
                "question": "Write CSS to make a button blue with white text and rounded corners.",
                "description": "Use CSS properties to style a button element with background, color, and border-radius.",
                "difficulty": "Easy",
                "file_name": "style.css",
                "code": "button {\n    background: blue;\n    color: white;\n    border-radius: 8px;\n}",
                "expected_output": "styled",
                "hint": "Use background, color, and border-radius for button styling.",
                "solution": "button {\n    background: blue;\n    color: white;\n    border-radius: 8px;\n}",
                "main_hints": [
                    "Target the button selector.",
                    "Use background for button color.",
                    "Use color for text color.",
                    "Use border-radius for rounded corners."
                ],
                "similar_questions": [
                    {
                        "title": "Similar Question 1",
                        "question": "Write CSS to make a green button with black text.",
                        "starter_code": "button {\n    background: green;\n    color: black;\n}"
                    },
                    {
                        "title": "Similar Question 2",
                        "question": "Write CSS to make a red button with white text and rounded corners.",
                        "starter_code": "button {\n    background: red;\n    color: white;\n    border-radius: 10px;\n}"
                    }
                ]
            }
        ]
    }


@app.route("/problem/<language>", methods=["GET", "POST"])
def problem(language):
    problems = get_problems()
    question_list = problems.get(language.lower())

    if not question_list:
        return redirect(url_for("home"))

    q_index = request.args.get("q", 0, type=int)
    if q_index < 0 or q_index >= len(question_list):
        q_index = 0

    selected = question_list[q_index]
    session_key = f"wrong_attempts_{language}_{q_index}"

    # FIXED BUG: clean reset and fresh reload
    reset_attempts = request.args.get("reset", "0")
    if reset_attempts == "1":
        session[session_key] = 0
        return redirect(url_for("problem", language=language, q=q_index))

    if session_key not in session:
        session[session_key] = 0

    wrong_attempts = session[session_key]

    output = None
    status_message = None
    success_message = None

    show_hint_btn = False
    show_solution_btn = False
    show_similar_btn = False
    show_similar_popup = False

    if request.method == "POST":
        action = request.form.get("action", "run")
        user_code = request.form.get("code", "")
        selected["code"] = user_code

        if action == "run":
            if language.lower() == "python":
                buffer = io.StringIO()
                try:
                    with contextlib.redirect_stdout(buffer):
                        exec(user_code, {})
                    output = buffer.getvalue().strip()

                    if not output:
                        output = "Python code executed successfully."

                    if output.strip() == selected["expected_output"]:
                        status_message = "Correct output. Well done!"
                        success_message = "Congratulations! Your code passed."
                        session[session_key] = 0
                        wrong_attempts = 0
                    else:
                        session[session_key] += 1
                        wrong_attempts = session[session_key]
                        status_message = "Wrong output. Try again."

                except Exception as e:
                    output = f"Error: {e}"
                    session[session_key] += 1
                    wrong_attempts = session[session_key]
                    status_message = "Code execution failed."

            elif language.lower() == "java":
                output = "Java execution backend not connected yet. UI is ready."
                session[session_key] += 1
                wrong_attempts = session[session_key]
                status_message = "Run simulated. Backend not connected."

            elif language.lower() == "css":
                output = "CSS code captured successfully. Live preview can be added next."
                session[session_key] += 1
                wrong_attempts = session[session_key]
                status_message = "Run simulated for CSS."

        elif action == "hint":
            output = f"Hint: {selected['hint']}"

        elif action == "solution":
            output = selected["solution"]

    # adaptive loop
    if wrong_attempts >= 1:
        show_hint_btn = True
    if wrong_attempts >= 2:
        show_solution_btn = True
    if wrong_attempts >= 4:
        show_similar_btn = True
        show_similar_popup = False
    else:
        show_similar_btn = False
        show_similar_popup = False

    has_next_question = q_index < len(question_list) - 1
    next_question_url = url_for("problem", language=language, q=q_index + 1)

    return render_template(
        "problem.html",
        language=language,
        title=selected["title"],
        question=selected["question"],
        description=selected["description"],
        difficulty=selected["difficulty"],
        file_name=selected["file_name"],
        code=selected["code"],
        output=output,
        status_message=status_message,
        wrong_attempts=wrong_attempts,
        show_hint_btn=show_hint_btn,
        show_solution_btn=show_solution_btn,
        show_similar_btn=show_similar_btn,
        show_similar_popup=show_similar_popup,
        success_message=success_message,
        has_next_question=has_next_question,
        next_question_url=next_question_url,
        similar_page_url=url_for("similar_questions", language=language, q=q_index)
    )


@app.route("/similar/<language>")
def similar_questions(language):
    problems = get_problems()
    question_list = problems.get(language.lower())

    if not question_list:
        return redirect(url_for("home"))

    q_index = request.args.get("q", 0, type=int)
    if q_index < 0 or q_index >= len(question_list):
        q_index = 0

    selected = question_list[q_index]

    return render_template(
        "similar.html",
        language=language,
        title=selected["title"],
        main_hints=selected["main_hints"],
        similar_one=selected["similar_questions"][0],
        similar_two=selected["similar_questions"][1],
        return_main_url=url_for("problem", language=language, q=q_index, reset=1)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)