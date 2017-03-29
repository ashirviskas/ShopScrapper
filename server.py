
from flask import Flask, jsonify, request
import extractproducts
import json
from celery import Celery





app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://',
    CELERY_RESULT_BACKEND='redis://'
)

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

@celery.task(name="celerytasks.cpu")
def cpu():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/procesoriai-stac-komp-procesoriai-desktop-cpu-c-86_85_182_584.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.motherboard")
def motherboard():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/pagrindines-plokstes-priedai-pagrindines-plokstes-c-86_85_826_248.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.cooler")
def cooler():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/ausintuvai-procesoriu-ausintuvai-c-86_85_116_115.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.casecooler")
def casecooler():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/ausintuvai-sisteminiai-korpusu-c-86_85_116_111.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.ram")
def ram():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/operatyvine-atmintis-stac-komp-atmintis-dimm-c-86_85_217_419.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.hdd")
def hdd():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/vidiniai-duomenu-kaupikliai-hdd-ssd-priedai-magnetiniai-standieji-diskai-hdd-c-86_85_1407_139.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.ssd")
def ssd():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/vidiniai-duomenu-kaupikliai-hdd-ssd-priedai-ssd-tipo-kaupikliai-solidstate-drive-c-86_85_1407_1408.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.gpu")
def gpu():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/vaizdo-plokstes-priedai-vaizdo-plokstes-vga-c-86_85_197_284.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.case")
def case():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/korpusai-priedai-korpusai-c-86_85_274_510.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.psu")
def psu():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/kompiuteriu-komponentai-maitinimo-blokai-c-86_85_300.html?sand=0&pav=0&sort=5a&grp=1')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)

@celery.task(name="celerytasks.dvd")
def dvd():
    a = extractproducts.Shopv(
        'http://www.skytech.lt/optiniai-irenginiai-dvd-irenginiai-c-86_85_224_59.html?sand=&pav=&sort=&grp=')
    return json.dumps([ob.__dict__ for ob in a.extract_all_products()], ensure_ascii=False)






@app.route('/', methods=['GET'])
def index_route():
    return json.dumps({
        'endpoints': {
            'cpu': '/cpu',
            'motherboard': '/motherboard',
            'cooler': '/cooler',
            'casecooler': '/casecooler',
            'ram': '/ram',
            'hdd': '/hdd',
            'ssd': '/ssd',
            'gpu': '/gpu',
            'case': '/case',
            'psu': '/psu'
        }
    })



fuct = {
            'cpu': cpu,
            'motherboard': motherboard,
            'cooler': cooler,
            'casecooler': casecooler,
            'ram': ram,
            'hdd': hdd,
            'ssd': ssd,
            'gpu': gpu,
            'case': case,
            'psu': psu,
            'dvd' : dvd
        }




@app.route('/<functionname>/<resultid>')
def result(functionname,resultid):

    if fuct[functionname].AsyncResult(resultid).ready():
        return fuct[functionname].AsyncResult(resultid).result
    return jsonify("Loading")




@app.route('/<part>')
def part(part):
    res=fuct[part].apply_async()
    return jsonify(result=res.task_id)




if __name__ == "__main__":
    app.run(debug=True)


