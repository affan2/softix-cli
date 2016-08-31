# Softix CLI

All commands require account information: client-id, secret, and seller-code. The CLI can use environment variables (my recommendation).
 - SOFTIX_CLIENT_ID
 - SOFTIX_SECRET
 - SOFTIX_SELLER_CODE

## Creating new customer

```bash

$ softix create-customer --data '{"internationalcode": "971", "firstname": "ajilan", "areacode": "unknown", "lastname": "MA", "phonenumber": "507156120", "salutation": "-", "nationality": "IN", "city": "dubai", "countrycode": "IN", "dateofbirth": "4-23-2015", "state": "dubai", "addressline2": "-", "addressline3": "-", "addressline1": "-", "email": "unknown@unknown.com"}'
{"id": 1301777}

```
