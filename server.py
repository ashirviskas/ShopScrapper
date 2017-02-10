
from flask import Flask, jsonify, request
import extractproducts
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_route():
    return json.dumps({
        'endpoints': {
            'cpu': '/cpu',
            'motherboard': '/motherboard',
            'cooler': '/cooler',
            'case cooler': '/casecooler',
            'ram': '/ram',
            'hdd': '/hdd',
            'sdd': '/sdd',
            'gpu': '/gpu',
            'case': '/case',
            'psu': '/psu'
        }
    })


@app.route('/cpu')
def cpu():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/procesoriai-stac-komp-procesoriai-desktop-cpu-c-86_85_182_584.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/motherboard')
def motherboard():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/pagrindines-plokstes-priedai-pagrindines-plokstes-c-86_85_826_248.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/cooler')
def cooler():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/ausintuvai-procesoriu-ausintuvai-c-86_85_116_115.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/casecooler')
def casecooler():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/ausintuvai-sisteminiai-korpusu-c-86_85_116_111.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/ram')
def ram():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/operatyvine-atmintis-stac-komp-atmintis-dimm-c-86_85_217_419.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/hdd')
def hdd():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/vidiniai-duomenu-kaupikliai-hdd-ssd-priedai-magnetiniai-standieji-diskai-hdd-c-86_85_1407_139.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/ssd')
def sdd():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/vidiniai-duomenu-kaupikliai-hdd-ssd-priedai-ssd-tipo-kaupikliai-solidstate-drive-c-86_85_1407_1408.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/gpu')
def gpu():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/vaizdo-plokstes-priedai-vaizdo-plokstes-vga-c-86_85_197_284.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/case')
def case():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/korpusai-priedai-korpusai-c-86_85_274_510.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])
@app.route('/psu')
def psu():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/kompiuteriu-komponentai-maitinimo-blokai-c-86_85_300.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()])

if __name__ == "__main__":
    app.run()


