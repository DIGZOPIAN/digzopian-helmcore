# 🌐 flask_ui.py - Digzopian HelmCore Web Interface

from flask import Flask, render_template_string, request
from taskbox import route_task
from symbolic_core import interpret_law

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DigzOS Control Panel</title>
</head>
<body style="font-family:sans-serif; text-align:center; padding:2em; background:#111; color:#0f0;">
    <h1>🧠 DIGZOPIAN HELMCORE</h1>
    <form method="post">
        <button name="task" value="analyze">🔍 Analyze</button>
        <button name="task" value="summarize">📝 Summarize</button>
        <button name="task" value="interpret">📜 Interpret Hermetic Law #4</button>
    </form>
    {% if response %}
        <p style="margin-top:2em;">→ {{ response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def control():
    response = None
    if request.method == "POST":
        task = request.form.get("task")
        if task == "interpret":
            response = interpret_law(4)
        else:
            response = route_task(task)
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
