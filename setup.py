import logging
import Flaskr
import sys

logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    encoding='utf-8',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flaskr.create_app(None)
app.run()
