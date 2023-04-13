from graphics import GraphWin, Point, Text, Entry, Rectangle

# Create a graphics window
win = GraphWin("Microorganism Quiz", 600, 400)

# List of questions and answers
questions = [
    # Question 1
    {
        'question': 'This microorganism consists of genetic material surrounded by a protein coat.',
        'options': ['virus', 'bacteria', 'parasite'],
        'answer': 'virus'
    },
    # Question 2
    {
        'question': 'This microorganism is a single-celled organism that can reproduce on its own.',
        'options': ['virus', 'bacteria', 'parasite'],
        'answer': 'bacteria'
    },
    # Add more questions here
]

# Loop through the questions
for i, question in enumerate(questions):
    # Display the question
    question_text = Text(Point(300, 100), f"Question {i+1}: {question['question']}")
    question_text.setSize(20)
    question_text.draw(win)

    # Display the options
    option_text = Text(Point(300, 200), 'Options: ' + ', '.join(question['options']))
    option_text.setSize(18)
    option_text.draw(win)

    # Display the entry box for user input
    input_box = Entry(Point(300, 300), 20)
    input_box.draw(win)

    # Display the submit button
    submit_button = Rectangle(Point(250, 350), Point(350, 380))
    submit_button_text = Text(Point(300, 365), 'Submit')
    submit_button.setFill('lightgray')
    submit_button.draw(win)
    submit_button_text.draw(win)

    # Wait for user input
    while True:
        click_point = win.getMouse()
        if 250 <= click_point.getX() <= 350 and 350 <= click_point.getY() <= 380:
            # User clicked the submit button
            user_answer = input_box.getText()
            if user_answer.lower() == question['answer']:
                # Correct answer
                result_text = Text(Point(300, 250), 'Correct!')
                result_text.setSize(18)
                result_text.setTextColor('green')
                result_text.draw(win)
                break
            else:
                # Incorrect answer
                result_text = Text(Point(300, 250), 'Incorrect!')
                result_text.setSize(18)
                result_text.setTextColor('red')
                result_text.draw(win)
                break

# Close the graphics window when done
win.getMouse()
win.close()
