import os
import dotenv
dotenv.load_dotenv()

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_URI = os.environ.get('MONGO_URI', None)



RESOURCE_METHODS = ['POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = []



schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'ipaddress': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': False,
    },
    'email': {
        # Validator
        'isemail': True,
        
        'type': 'string',
        'minlength': 1,
        'maxlength': 60,
        'required': True,
        'unique': True,
    },

}

people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    # 'additional_lookup': {
    #     'url': r'regex("[\w]+")',
    #     'field': 'email'
    # },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['POST'],
    'item_methods': [],

    'schema': schema
}

DOMAIN = {
    'people': people
}