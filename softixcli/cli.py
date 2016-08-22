import click
import json
import softix


@click.group()
@click.option('--client-id', envvar='SOFTTIX_CLIENT_ID')
@click.option('--secret', envvar='SOFTTIX_SECRET')
@click.option('--seller-code', envvar='SOFTTIX_SELLER_CODE')
@click.pass_context
def cli(context, client_id, secret, seller_code):
    context.obj = {}
    context.obj['client_id'] = client_id
    context.obj['secret'] = secret
    context.obj['seller_code'] = seller_code


@cli.command(name='create-customer')
@click.option("--data", "-d", help="Customer data as json", required=True)
@click.pass_context
def create_customer(context, data):
    """Create a new customer."""
    softix_client = softix.SoftixCore()
    softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    try:
        json.loads(data)
    except ValueError:
        click.echo("Unable to parse customer data as JSON")
        context.exit(1)


@cli.command(name='delete-customer')
def delete_customer(context):
    """Delete a customer."""
    pass
