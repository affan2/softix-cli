import click
import datetime
import json


def validate_fee(context, param, fees):
    """
    Validate fees.
    """
    return fees


def validate_token_file(context, param, value):
    """
    Validate token file.
    """
    softix_client = context.obj['softix_client']
    if not value:
        return softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    try:
        auth_data = json.loads(value)
        expiration_date = datetime.datetime.strptime(auth_data['expiration_date'], '%Y-%m-%dT%H:%M:%S.%f')
        expired = datetime.datetime.utcnow() > expiration_date

        if expired:
            raise click.BadParameter('Token expired. Generate new token')
        else:
            softix_client = context.obj['softix_client']
            softix_client.access_token = auth_data['access_token']
            return auth_data['access_token']
    except ValueError:
        raise click.BadParameter('Invalid JSON data')
    except KeyError as error:
        raise click.BadParameter('Invalid token file')
