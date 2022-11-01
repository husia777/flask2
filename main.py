from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/<users>/<id>')
def id_users(users, id):
    return render_template('users/show.html', id=id, nickname=users)


@app.route('/users')
def get_users():
    users = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    return render_template('users/index.html', users=users)


@app.route('/users/')
def filter_users():
    users = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    term = request.args.get('term')
    filtered_users = [i for i in users if term in i]
    return render_template('users/index.html', users=filtered_users, search=term)



if __name__ == '__main__':
    app.run(debug=True)
