"""This module helps in migrating OAuth 1.0a tokens to OAuth 2.0
"""
from __future__ import absolute_import

import json
from requests_oauthlib import OAuth1

from intuitlib.utils import (
    scopes_to_string,
    send_request,
)
from intuitlib.config import MIGRATION_URL

def migrate(consumer_key, consumer_secret, access_token, access_secret, auth_client, scopes):
    """Migrates OAuth1 tokens to OAuth2 tokens
    
    :param consumer_key: OAuth1 Consumer Key
    :param consumer_secret: OAuth1 Consumer Secret
    :param access_token: OAuth1 Access Token
    :param access_secret: OAuth1 Access Secret
    :param auth_client: AuthClient for OAuth2 specs
    :type auth_client: `intuitlib.client.AuthClient`
    :param scopes: list of `intuitlib.enum.Scopes`
    :raises AuthClientError: if response status != 200
    """

    if auth_client.environment.lower() == 'production':
        migration_url = MIGRATION_URL['production']
    else:
        migration_url = MIGRATION_URL['sandbox']
    
    auth_header = OAuth1(consumer_key, consumer_secret, access_token, access_secret)

    headers = {
        'Content-Type': 'application/json',
    }

    body = {
        'scope': scopes_to_string(scopes),
        'redirect_uri': auth_client.redirect_uri,
        'client_id': auth_client.client_id,
        'client_secret': auth_client.client_secret
    }
    
    send_request('POST', migration_url, headers, auth_client, body=json.dumps(body), oauth1_header=auth_header)
