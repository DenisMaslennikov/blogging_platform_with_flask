from collections import namedtuple

from .index import index_blueprint
from .post import post_blueprint
from .tags import tags_blueprint
from .categories import category_blueprint
from .month import month_blueprint

BlueprintContainer = namedtuple(
    'BlueprintContainer', ['blueprint', 'url_prefix']
)

blueprints = [
    BlueprintContainer(index_blueprint, ''),
    BlueprintContainer(post_blueprint, '/post'),
    BlueprintContainer(tags_blueprint, '/tag'),
    BlueprintContainer(category_blueprint, '/category'),
    BlueprintContainer(month_blueprint, '/month'),
]
