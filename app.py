from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

todo_tasks = []

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todo_tasks.append(task)
        else:
            print("No Task to Add")
    return render_template('index.html', todo_tasks=todo_tasks)

@app.route("/remove", methods=["POST"])
def remove_one():
    task = request.form.get('single_task')
    if task in todo_tasks:
        todo_tasks.remove(task)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
