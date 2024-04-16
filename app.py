from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'Location': 'Bengaluru, India',
        'Salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'Location': 'Delhi, India',
        'Salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'Location': 'Remote',
        'Salary': ''
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'Location': 'San Francisco, USA',
        'Salary': '$ 120,000'
    }

]


@app.route('/')
def hello_jovian():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


app.run(debug=True)
