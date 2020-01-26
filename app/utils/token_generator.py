import app.models.tokens as model
from app.utils.db_initializer import db
from app.models.tokens import Tokens, TokenListSchema
from werkzeug.contrib.cache import MemcachedCache

cache = MemcachedCache(['127.0.0.1:11211'])


def tokens():
    """Get all tokens from Database"""
    tokens = db.session.query(Tokens).filter(Tokens.id >= 0)
    token_schema = model.TokenListSchema(many=True)
    result = token_schema.dump(tokens)
    return result


def generate_token():
    """Get token from Cache"""
    queue = cache.get('token_queue')
    if queue is None:
        get_tokens = tokens()
        cache.set('token_queue', get_tokens, 5000)
    queue = cache.get('token_queue')
    token = queue.pop(0)
    token['used_count'] += 1
    queue.append(token)
    cache.set('token_queue', queue, 5000)
    return token['token_name']


def save_token(tokens):
    """Save token status into Database"""
    token = db.session.query(Tokens).filter(Tokens.token_name == tokens['token_name']).first()
    token.used_count = tokens['used_count']
    db.session.commit()
