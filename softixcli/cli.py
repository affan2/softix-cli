import click
import json
import softix


@click.group()
@click.option('--client-id', help='Client ID', envvar='SOFTIX_CLIENT_ID')
@click.option('--secret', help='Secret', envvar='SOFTIX_SECRET')
@click.option('--seller-code', help='Seller code', envvar='SOFTIX_SELLER_CODE')
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
    """
    Create a new customer.
    """
    softix_client = softix.SoftixCore()
    softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    seller_code = context.obj['seller_code']
    try:
        customer_data = json.loads(data)
        customer_id = softix_client.create_customer(seller_code, **customer_data)
        output = json.dumps({'id': customer_id})
        click.echo(output)
    except ValueError:
        click.echo("Unable to parse customer data as JSON")
        context.exit(1)
    except softix.exceptions.SoftixError as error:
        click.echo(error.message)
        context.exit(1)


@cli.command(name='delete-customer')
def delete_customer(context):
    """Delete a customer."""
    pass

@cli.command(name='get-performance-availabilities')
@click.argument('performance-code', type=str)
@click.pass_context
def get_performance_availabilities(context, performance_code):
    """
    Get performance availabilities.

    Performance availabilities is basically event information
    """
    softix_client = softix.SoftixCore()
    softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    seller_code = context.obj['seller_code']
    try:
        performance_data = softix_client.performance_availabilities(seller_code, performance_code)
        output = json.dumps(performance_data)
        click.echo(output)
    except softix.exceptions.SoftixError as error:
        click.echo(error.message)
        context.exit(1)

if __name__ == "__main__":
    cli()
