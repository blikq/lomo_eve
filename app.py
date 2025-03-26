from eve import Eve, logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin
from validators import MyValidator
from flask import request


logging.logging.basicConfig(level=logging.logging.INFO)
logger = logging.logging.getLogger(__name__)

app = Eve(validator=MyValidator)

cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize the limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per day", "5 per minute"],  # Global limits
    storage_uri="memory://",
)

def add_ip(items):
    for item in items:
        ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        item['ipaddress'] = ip
        logger.info(f"Assigning IP {ip} to new document.")
        
app.on_insert_people += add_ip


# Apply a limit to the users POST endpoint (e.g., 5 requests per minute)
@limiter.limit("5 per minute")
@app.route('/people', methods=['POST'])
@cross_origin()
def limited_post():
    # logger.info(request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr))

    return app.view_functions['users']()




if __name__ == '__main__':
    app.run()