from eve import Eve
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin

app = Eve()

cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize the limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "5 per minute"],  # Global limits
)

# Apply a limit to the users POST endpoint (e.g., 5 requests per minute)
@limiter.limit("5 per minute")
@app.route('/people', methods=['POST'])
@cross_origin()
def limited_post():
    return app.view_functions['users']()




if __name__ == '__main__':
    app.run()