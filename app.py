#!/usr/bin/env python3

# app.py
# Heroku Minima
# implemented by by Terzo Technical
# (c) 2024 Shannon Douglas Ware 


from flask import Flask, render_template, send_from_directory, request
import markdown
# import markdown.extensions.fenced_code


app = Flask(__name__) #, static_folder='static', static_url_path='')

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


@app.get('/articles/analogue')
def article_analogue():
    return render_template('article.html')
    ##return 'static/articles/toward-analogue-design-02-mar-2025.md'


@app.get('/one-page-python')
def one_page_python():
    return render_template('one-page-python.html')


@app.context_processor
def context_preprocessor():
    with open("static/articles/toward-analogue-design-02-mar-2025.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    # html = markdown.markdown(text, extensions=["fenced_code"])
    # see https://artandhacks.se/articles/flask-markdown/ for {{stringOfMarkdown|safe}}
    return dict(text=text, markdown=markdown.markdown)


@app.get('/resume-sql')
def resume_sql():
    return render_template('resume-sql.html')


@app.get('/articles/flask-heroku')
def article_flask_heroku():
    # return 'This is a test'
    return render_template('article-flask-heroku.html')


@app.get('/one-page-trigonometry')
def one_page_trigonometry():
    return render_template('one-page-trigonometry.html')


@app.route('/ads.txt', methods=['GET'])
def static_from_root():
    print("request.path[1:]:", request.path[1:])
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run() # debug=True, host='0.0.0.0'
