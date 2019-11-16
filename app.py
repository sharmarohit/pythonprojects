from flask import render_template
# from swagger_ui_bundle import swagger_ui_path
import connexion

app = connexion.App(__name__, specification_dir='openapi/')

app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
