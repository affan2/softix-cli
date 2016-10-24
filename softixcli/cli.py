import click
import json
import softix

from .validations import validate_fee


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
        context.fail(error.message)

@cli.command(name='create-basket')
@click.argument('performance-code', type=str)
@click.option('--section', type=str, required=True)
@click.option('--demand', nargs=3, required=True, multiple=True, help='Price Type Code, Quantity, Admits')
@click.option('--fee', required=True, nargs=2, multiple=True, help='Fee: type, code', callback=validate_fee)
@click.pass_context
def create_basket(context, performance_code, section, demand, fee):
    """
    Create a cart/basket.
    """
    softix_client = softix.SoftixCore()
    softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    seller_code = context.obj['seller_code']
    demands = [softix.Demand(*d) for d in demand]
    fees = [softix.Fee(*f) for f in fee]
    basket = softix_client.create_basket(seller_code, performance_code, section, demands, fees)
    click.echo(json.dumps(basket))
    

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

@cli.command(name='get-performance-prices')
@click.argument('performance-code', type=str)
@click.pass_context
def get_performance_prices(context, performance_code):
    """
    Get performance prices.
    """
    softix_client = softix.SoftixCore()
    softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    seller_code = context.obj['seller_code']
    try:
        performance_prices = softix_client.performance_prices(seller_code, performance_code)
        output = json.dumps(performance_prices)
        click.echo(output)
    except softix.exceptions.SoftixError as error:
        click.echo(error.message)
        context.exit(1)

@cli.command(name='get-basket')
@click.argument('basket-id', type=str)
@click.pass_context
def get_basket(context, basket_id):
    """
    Get basket.
    """
    softix_client = softix.SoftixCore()
    softix_client.authenticate(context.obj['client_id'], context.obj['secret'])
    seller_code = context.obj['seller_code']
    try:
        basket = softix_client.basket(seller_code, basket_id)
        output = json.dumps(basket)
        click.echo(output)
    except softix.exceptions.SoftixError as error:
        click.echo(error.message)
        context.exit(1)


if __name__ == "__main__":
    cli()
