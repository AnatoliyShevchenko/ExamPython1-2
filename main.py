from flask import (Flask, render_template, request)
from document import log


app = Flask(__name__)
posts = {}
name = ''


@app.route('/', methods=['get', 'post'])
def main():
    return render_template('index.html')

@app.route('/posts', methods=['get', 'post'])
def second():
    answer = 'Wrong login or password. Get out'
    global name, posts
    name = request.form.get('login')
    password = request.form.get('password')
    if name in log and password in log[name]:
        return render_template('posts.html', posts=posts)
    elif name not in log or password not in log[name]:
        return render_template('index.html', answer=answer)

    return render_template('posts.html', posts=posts)

@app.route('/posts/add', methods=['GET' ,'POST'])
def third():
    global name, posts
    name = name
    about = request.form.get('about')
    text = request.form.get('text')
    val_name = name.split('/')
    val_about = about.split('/')
    val_text = text.split('/')
    temp = dict.fromkeys(val_about, dict.fromkeys(val_text, val_name))
    posts.update(temp)
    print(posts)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(port=8092, debug=True)