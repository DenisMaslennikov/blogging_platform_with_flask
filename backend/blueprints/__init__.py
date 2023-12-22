from collections import namedtuple

from .index import index_blueprint
from .post import post_blueprint
from .tags import tags_blueprint

BlueprintContainer = namedtuple(
    'BlueprintContainer', ['blueprint', 'url_prefix']
)

blueprints = [
    BlueprintContainer(index_blueprint, ''),
    BlueprintContainer(post_blueprint, '/post'),
    BlueprintContainer(tags_blueprint, '/tag'),
]
