from flask import Flask, render_template, request, redirect
app = Flask(__name__)

student_list = []

@app.route('/')
def index():
    return render_template('index.html', student_list = student_list, num=len(student_list))

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        student_name = request.form['name']
        student_list.append(student_name)
        return redirect('/')
    return render_template('register.html')

@app.route('/delete', methods=['POST'])
def delete():
    student_list.pop()
    return redirect('/')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 