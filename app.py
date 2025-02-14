#!/usr/bin/env python3

# app.py
# Heroku Minima
# implemented by by Terzo Technical
# (c) 2024 Shannon Douglas Ware 


from flask import Flask, render_template

app = Flask(__name__)

### Web Pages ###
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.errorhandler(404)
def not_found(e):
  return render_template('error_404.html'), 404

    
# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World! Brought to you by Terzo Technical'


@app.get('/terms')
def terms():
    return render_template('terms.html')


@app.get('/privacy')
def privacy():
    return render_template('privacy.html')


@app.get('/contact')
def contact():
    return render_template('contact.html')


@app.get('/resume-support-engineer')
def resume_support_engineer():
    return render_template('curriculum-vitae.html')


@app.get('/resume-data-engineer')
def resume_data_engineer():
    return render_template('curriculum-vitae.html')


@app.get('/resume-full-stack-developer')
def resume_full_stack_developer():
    return render_template('curriculum-vitae.html')


@app.get('/resume-administrator')
def resume_administrator():
    return render_template('curriculum-vitae.html')


@app.get('/portfolio-data-engineer')
def portfolio_data_engineer():
    return render_template('curriculum-vitae.html')


@app.get('/curriculum-vitae')
def curriculum_vitae():
    return render_template('curriculum-vitae.html')


@app.get('/portfolio')
def portfolio():
    return render_template('portfolio-data-engineer.html')

@app.get('/problems-solved')
def problems_solved():
    return render_template('problems-solved.html')

@app.get('/barista')
def barista():
    return render_template('barista.html')

@app.get('/one-page-javascript')
def one_page_javascript():
    return render_template('one-page-javascript.html')

@app.get('/one-page-sql')
def one_page_sql():
    return render_template('one-page-sql.html')

@app.get('/one-page-csharp')
def one_page_csharp():
    return render_template('one-page-csharp.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
