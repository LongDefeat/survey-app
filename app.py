from flask import Flask, request, render_template 


from surveys import satisfaction_survey as surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "made-up-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_survey():
    """Select a survey"""
    title = surveys.title
    instructions = surveys.instructions
    return render_template('survey_start.html', title=title, instructions=instructions)

@app.route('/questions')
def survey_questions():
    title = satisfaction_survey.title
    questions = satisfaction_survey.questions
    return render_template('questions.html', title=title, questions=questions)

# @app.route('/begin', methods=["POST"])
# def start_survey():
#     """Clear the session from old responses"""
#     session[RESPONSES_KEY] = []
#     return redirect ("/questions/0")

# @app.route("/answer", methods=["POST"])
# def handle_question():
#     """Save response and redirects to next question"""

#     # gets response to choice
#     choice = request.form['answer']

#     # add this response to the session
#     responses = session[RESPONSES_KEY]
#     responses.append(choice)
#     session[RESPONSES_KEY] = responses

#     if (len(responses) == len(survey.questions)):
#         # all questions have been answered
#         return redirect("/complete")

# @app.route("/questions/<int:qid>")
# def show_question(qid):
#     """Display current question"""
#     responses = session.get(RESPONSES_KEY)
    

