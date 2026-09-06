from flask import Flask
import random
from datetime import date

app = Flask(__name__)

header = """
<header style="background-color: #f0f0f0; padding: 10px; text-align: center;">
    <h1>Мой блог</h1>
    <p>Программирование и веб-разработка</p>
    <nav>
        <a href="/">Главная</a> |
        <a href="/blog/1">Пост 1</a> |
        <a href="/blog/2">Пост 2</a> |
        <a href="/blog/3">Пост 3</a> |
        <a href="/coin">Монетка</a> |
        <a href="/meme">Мем</a> |
        <a href="/about">Обо мне</a>
    </nav>
</header>
"""

footer = """
<footer style="background-color: #ddd; padding: 10px; text-align: center;">
    <p>Автор: начинающий Python-разработчик</p>
    <p>
        <a href="https://github.com/Kitrusp0st">GitHub</a> |
        <a href="#">Telegram</a> |
        <a href="#">VK</a>
    </p>
    <a href="/">Вернуться на главную</a>
</footer>
"""


p1 = open("post1.html", encoding="utf-8").read()
p2 = open("post2.html", encoding="utf-8").read()
p3 = open("post3.html", encoding="utf-8").read()

@app.route("/")
def main_page():
    return header + """
    <main style="padding: 20px;">
        <h2>Добро пожаловать!</h2>
        <p>Это мой блог, здесь я делюсь мыслями о коде.</p>
    </main>
    """ + footer

@app.route("/blog/1")
def first_post():
    return header + p1 + footer

@app.route("/blog/2")
def second_post():
    return header + p2 + footer

@app.route("/blog/3")
def third_post():
    return header + p3 + footer

@app.route("/coin")
def coin_flip():
    result = random.choice(["Орел", "Решка"])
    return header + f"<main style='padding:20px;'><h1>Бросок монетки</h1><p>{result}</p><a href='/coin'>Ещё раз</a></main>" + footer

@app.route("/meme")
def meme_of_day():
    day = int(date.today().strftime("%j"))
    memes = ["Кот с ноутбуком", "Грустная собака", "Смешной пингвин", "Танцующий сж"]
    meme = memes[day % len(memes)]
    return header + f"<main style='padding:20px;'><h1>Мем дня</h1><p>{meme}</p></main>" + footer

@app.route("/secret")
def secret_page():
    return header + "<main style='padding:20px;'><h1>Секретная страница</h1><p>Вы нашли скрытый путь!</p></main>" + footer

@app.route("/about")
def about_page():
    about_content = """
    <main style="padding:20px;">
        <h1>Обо мне</h1>
        <p>Этот блог создан на Flask для изучения веб-разработки.</p>
        <p>Автор — начинающий Python-разработчик, интересуется веб-технологиями.</p>
        <p>В блоге публикуются посты о программировании и HTML.</p>
        <p>Мой GitHub: <a href="https://github.com/Kitrusp0st">Kitrusp0st</a></p>
    </main>
    """
    return header + about_content + footer


@app.route("/project")
def project_page():

    project_header = """
    <header style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; text-align: center;">
        <h1 style="font-family: 'Arial', sans-serif; letter-spacing: 2px;">Учебный проект Flask</h1>
        <p style="font-style: italic;">Программирование и веб-разработка</p>
        <nav style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 5px;">
            <a href="/" style="color: white;">Главная</a> |
            <a href="/blog/1" style="color: white;">Пост 1</a> |
            <a href="/blog/2" style="color: white;">Пост 2</a> |
            <a href="/blog/3" style="color: white;">Пост 3</a> |
            <a href="/coin" style="color: white;">Монетка</a> |
            <a href="/meme" style="color: white;">Мем</a> |
            <a href="/about" style="color: white;">Обо мне</a>
        </nav>
    </header>
    """
    project_footer = """
    <footer style="background: #333; color: white; padding: 15px; text-align: center; margin-top: 30px;">
        <p>© 2026 Учебный проект на Flask</p>
    </footer>
    """

    content = """
    <main style="max-width: 900px; margin: 30px auto; padding: 20px; background: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-family: 'Segoe UI', sans-serif;">
        <h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">Это учебный проект на Flask</h2>
        <p style="font-size: 18px; line-height: 1.6;">Проект посвящён программированию и веб-разработке.</p>
        <h3 style="color: #764ba2;">Что на сайте:</h3>
        <ul style="list-style: none; padding: 0;">
            <li style="margin: 10px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #667eea;">
                <strong>Главная</strong> — приветствие, открывающее двери в мир кода.
            </li>
            <li style="margin: 10px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #764ba2;">
                <strong>Три поста</strong> — подгружаются из файлов post1.html, post2.html, post3.html.
            </li>
            <li style="margin: 10px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #667eea;">
                <strong>Монетка</strong> — случайный выбор между «Орлом» и «Решкой» через random, маленькая игра в непредсказуемость.
            </li>
            <li style="margin: 10px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #764ba2;">
                <strong>Мем дня</strong> — выбирается по дню года через date.today().strftime("%j"), чтобы каждый день приносил свою порцию юмора.
            </li>
            <li style="margin: 10px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #667eea;">
                <strong>Секретная страница /secret</strong> — скрытый уголок, доступный лишь тем, кто знает путь.
            </li>
            <li style="margin: 10px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #764ba2;">
                <strong>Обо мне</strong> — страница, где автор приоткрывает завесу своей истории.
            </li>
        </ul>
        <p style="text-align: center; margin-top: 30px;">
            <a href="/" style="background: #667eea; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Вернуться на главную</a>
        </p>
    </main>
    """
    return project_header + content + project_footer

if __name__ == "__main__":
    app.run(debug=True)
