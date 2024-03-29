from flask import Flask, render_template, request, redirect, url_for
from scraper import Scraper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    country_option = int(request.form['country'])
    product_name = request.form['product']
    page_count = int(request.form['pages'])

    s = Scraper()
    s.set_country(country_option)
    s.set_product_name(product_name)
    s.set_page_count(page_count)

    s.scraping()
    s.export_to_csv()

    # Redirigir al usuario a la página de inicio después de completar el scraping
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)