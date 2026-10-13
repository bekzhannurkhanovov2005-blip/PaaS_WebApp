from flask import Flask, render_template_string

app = Flask(__name__)

# Басты бет
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="kk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PaaS веб-қосымшасы</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #eef2f7;
                text-align: center;
                padding: 50px 15px;
                margin: 0;
            }

            .container {
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }

            h1 {
                color: #2457a7;
            }

            p {
                font-size: 18px;
                line-height: 1.6;
                color: #333;
            }

            a {
                display: inline-block;
                margin: 10px;
                padding: 12px 20px;
                background-color: #2457a7;
                color: white;
                text-decoration: none;
                border-radius: 6px;
            }

            a:hover {
                background-color: #173d78;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>PaaS веб-қосымшасына қош келдіңіз!</h1>
            <p>Бұл веб-қосымша Python және Flask көмегімен жасалды.</p>
            <p>Мақсаты: бұлттық платформаларда веб-қосымшаларды
            әзірлеу және орналастыру мүмкіндіктерін зерттеу.</p>
            <a href="/info">Қосымша туралы ақпарат</a>
        </div>
    </body>
    </html>
    """)


# Қосымша туралы ақпарат беті
@app.route("/info")
def info():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="kk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Қосымша туралы</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #eef2f7;
                text-align: center;
                padding: 50px 15px;
            }

            .container {
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
            }

            h1 {
                color: #2457a7;
            }

            p {
                font-size: 18px;
                line-height: 1.6;
            }

            a {
                color: #2457a7;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Қосымша туралы ақпарат</h1>
            <p>Қосымша Python бағдарламалау тілінде әзірленді.</p>
            <p>Flask фреймворкі HTTP сұраныстарын өңдеу үшін қолданылады.</p>
            <p>HTML және CSS веб-беттің интерфейсін қалыптастырады.</p>
            <a href="/">Басты бетке қайту</a>
        </div>
    </body>
    </html>
    """)


if __name__ == "__main__":
    app.run(debug=True)