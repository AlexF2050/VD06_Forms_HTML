# Прописываем логику маршрутизации

from flask import Flask, render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        if title and hobby:
            posts.append({'title': title, 'age': age, 'city': city,'hobby': hobby})
            return redirect(url_for('index'))
    return render_template('user_profiles.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

