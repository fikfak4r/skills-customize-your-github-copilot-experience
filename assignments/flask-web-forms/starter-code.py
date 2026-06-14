from flask import Flask, render_template_string, request

app = Flask(__name__)

home_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Flask Web Form</title>
  </head>
  <body>
    <h1>Tell us about yourself</h1>
    <form method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" />
      <br /><br />
      <label for="topic">Favorite programming topic:</label>
      <input type="text" id="topic" name="topic" />
      <br /><br />
      <button type="submit">Submit</button>
    </form>
    {% if error %}
      <p style="color: red;">{{ error }}</p>
    {% endif %}
  </body>
</html>
"""

response_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Flask Response</title>
  </head>
  <body>
    <h1>Submission Received</h1>
    <p>Hello, {{ name }}! Your favorite topic is {{ topic }}.</p>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        topic = request.form.get('topic', '').strip()

        if not name or not topic:
            error = 'Please enter both your name and favorite topic.'
        else:
            return render_template_string(response_template, name=name, topic=topic)

    return render_template_string(home_template, error=error)

if __name__ == '__main__':
    app.run(debug=True)
