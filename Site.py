
from flask import Flask

app = Flask(__name__)

blog_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Мой блог о программировании</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Главная</a></li>
            <li><a href="/about">Обо мне</a></li>
        </ul>
    </nav>

    <h1>Добро пожаловать в мой блог</h1>

    <p>Здесь я делюсь мыслями о разработке</p>


    <h2>Полезные ресурсы</h2>
    <p>Рекомендую посетить:
        <a href="https://github.com/Kitrusp0st">это мой github</a>
    </p>
</body>
</html>
"""

@app.route("/")
def hello_world():
    return blog_page

@app.route("/about")
def about():
    return "<h1>Обо мне</h1><p>Я начинающий разработчик, изучаю Flask и Python</p>"

if __name__ == "__main__":
    app.run(debug=True)
