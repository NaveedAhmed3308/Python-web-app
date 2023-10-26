from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='Templates')
JOBS = [{
    'id':
    1,
    'title':
    'Python Developer',
    'location':
    'New York',
    'salary':
    '$100,000',
    'company':
    'Google',
    'description':
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
}, {
    'id':
    2,
    'title':
    'java Developer',
    'location':
    'pakistan',
    'salary':
    '$120,000',
    'company':
    'Microsoft',
    'description':
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
}, {
    'id':
    3,
    'title':
    '.net Developer',
    'location':
    'karachi',
    'salary':
    '$130,000',
    'company':
    'Microsoft',
    'description':
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
}]


@app.route("/")
def hello_world():
  return render_template('index.html', jobs=JOBS)


@app.route("/jobs")
def Jobs_Info():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
