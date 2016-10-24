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

## Get Performance prices

To retrieve event details from the API, call the command `get-performance-prices`.

A performance in the softix world is what we would consider an event—there's a 1 to 1 relationship between the two.  Therefore, we need to modify the event table schema and add a column named 'performance_id'.  

```bash

$softix get-performance-prices ETES0000004EL
{
    "BasketPrices": null,
    "OfferPrices": {
        "FeeTypes": [
            {
                "FeeBucket": "hfee",
                "FeeType": "5",
                "FeeTypeName": "Handling Fee",
                "FeesDetailed": [
                    {
                        "FeeCode": "W",
                        "FeeDescription": "Web Service - API",
                        "FeeId": "1",
                        "FeeName": "WebServ",
                        "FeeSheetId": 0,
                        "FeeTotal": 0.0,
                        "FinanceCode": null
                    }
                ],
                "Inside": false
            }
        ],
        "Prices": null
    },
    "PriceCategories": [
        {
            "PriceCategoryCode": "1",
            "PriceCategoryId": 1,
            "PriceCategoryName": "General Admission"
        },
        {
            "PriceCategoryCode": "2",
            "PriceCategoryId": 2,
            "PriceCategoryName": "Reserved"
        },
        {
            "PriceCategoryCode": "3",
            "PriceCategoryId": 3,
            "PriceCategoryName": "Vip"
        }
    ],
    "PriceTypes": [
        {
            "AdmitCount": 1,
            "ConcessionCount": 0,
            "Entitlement": null,
            "OfferCode": "",
            "PriceSheetId": 0,
            "PriceTypeCode": "H",
            "PriceTypeDescription": "Nmfzco",
            "PriceTypeId": 1,
            "PriceTypeName": "NMFZCO",
            "QualifierCode": null
        },
        {
            "AdmitCount": 1,
            "ConcessionCount": 0,
            "Entitlement": null,
            "OfferCode": "",
            "PriceSheetId": 0,
            "PriceTypeCode": "C",
            "PriceTypeDescription": "Complimentary",
            "PriceTypeId": 2,
            "PriceTypeName": "COMP ",
            "QualifierCode": null
        },
        {
            "AdmitCount": 1,
            "ConcessionCount": 0,
            "Entitlement": null,
            "OfferCode": "",
            "PriceSheetId": 0,
            "PriceTypeCode": "Q",
            "PriceTypeDescription": "Nmfzco",
            "PriceTypeId": 3,
            "PriceTypeName": "NMFZCO",
            "QualifierCode": null
        },
        {
            "AdmitCount": 1,
            "ConcessionCount": 0,
            "Entitlement": null,
            "OfferCode": "",
            "PriceSheetId": 0,
            "PriceTypeCode": "G",
            "PriceTypeDescription": "10disc",
            "PriceTypeId": 4,
            "PriceTypeName": "10DIS",
            "QualifierCode": null
        },
        {
            "AdmitCount": 1,
            "ConcessionCount": 0,
            "Entitlement": null,
            "OfferCode": "",
            "PriceSheetId": 0,
            "PriceTypeCode": "Z",
            "PriceTypeDescription": "Zcomp",
            "PriceTypeId": 5,
            "PriceTypeName": "ZCOMP",
            "QualifierCode": null
        }
    ],
    "TicketPrices": {
        "FeeTypes": null,
        "Prices": [
            {
                "FeeTypes": null,
                "PriceCategoryCode": "1",
                "PriceCategoryId": 1,
                "PriceId": 1,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "H",
                "PriceTypeId": 1
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "2",
                "PriceCategoryId": 2,
                "PriceId": 2,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "H",
                "PriceTypeId": 1
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "1",
                "PriceCategoryId": 1,
                "PriceId": 3,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "C",
                "PriceTypeId": 2
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "2",
                "PriceCategoryId": 2,
                "PriceId": 4,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "C",
                "PriceTypeId": 2
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "3",
                "PriceCategoryId": 3,
                "PriceId": 5,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "C",
                "PriceTypeId": 2
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "1",
                "PriceCategoryId": 1,
                "PriceId": 6,
                "PriceNet": 10000,
                "PriceSheetId": 0,
                "PriceTypeCode": "Q",
                "PriceTypeId": 3
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "2",
                "PriceCategoryId": 2,
                "PriceId": 7,
                "PriceNet": 20000,
                "PriceSheetId": 0,
                "PriceTypeCode": "Q",
                "PriceTypeId": 3
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "3",
                "PriceCategoryId": 3,
                "PriceId": 8,
                "PriceNet": 30000,
                "PriceSheetId": 0,
                "PriceTypeCode": "Q",
                "PriceTypeId": 3
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "1",
                "PriceCategoryId": 1,
                "PriceId": 9,
                "PriceNet": 8000,
                "PriceSheetId": 0,
                "PriceTypeCode": "G",
                "PriceTypeId": 4
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "2",
                "PriceCategoryId": 2,
                "PriceId": 10,
                "PriceNet": 7000,
                "PriceSheetId": 0,
                "PriceTypeCode": "G",
                "PriceTypeId": 4
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "3",
                "PriceCategoryId": 3,
                "PriceId": 11,
                "PriceNet": 6000,
                "PriceSheetId": 0,
                "PriceTypeCode": "G",
                "PriceTypeId": 4
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "1",
                "PriceCategoryId": 1,
                "PriceId": 12,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "Z",
                "PriceTypeId": 5
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "2",
                "PriceCategoryId": 2,
                "PriceId": 13,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "Z",
                "PriceTypeId": 5
            },
            {
                "FeeTypes": null,
                "PriceCategoryCode": "3",
                "PriceCategoryId": 3,
                "PriceId": 14,
                "PriceNet": 0,
                "PriceSheetId": 0,
                "PriceTypeCode": "Z",
                "PriceTypeId": 5
            }
        ]
    }
}
```

## Create a basket
What we call a cart, the Dubai API calls a basket.

```
$ softix create-basket ETES0000004EL --section SGA --demand Q 1 3 --fee 5 W

{
    "Fees": [],
    "Id": "19115-32902968",
    "Offers": [
        {
            "Channel": "W",
            "DateTime": "0001-01-01T00:00:00",
            "Demand": [
                {
                    "Admits": 3,
                    "Customer": {
                        "AFile": null,
                        "Account": null,
                        "Id": null,
                        "OrgCustomerId": null
                    },
                    "Entitlement": null,
                    "OfferCode": null,
                    "PriceType": null,
                    "PriceTypeCode": "Q",
                    "PriceTypeId": null,
                    "Prices": [
                        {
                            "Fees": [
                                {
                                    "Bucket": null,
                                    "Code": null,
                                    "FinanceCode": null,
                                    "Id": null,
                                    "Inside": false,
                                    "Name": null,
                                    "SheetId": 0,
                                    "Total": 0,
                                    "Type": "1",
                                    "TypeName": "BookingFee"
                                }
                            ],
                            "Id": null,
                            "Net": 30000,
                            "SheetId": 0
                        }
                    ],
                    "QualifierCode": null,
                    "Quantity": 1
                }
            ],
            "Fees": [
                {
                    "Bucket": null,
                    "Code": "W",
                    "FinanceCode": null,
                    "Id": null,
                    "Inside": false,
                    "Name": null,
                    "SheetId": 0,
                    "Total": 0,
                    "Type": "5",
                    "TypeName": "HandlingFee"
                }
            ],
            "Id": "1",
            "InventorySource": null,
            "PerformanceCode": "ETES0000004EL",
            "PriceCategory": null,
            "PriceCategoryCode": "1",
            "PriceCategoryId": null,
            "Seats": [
                {
                    "Row": "GA",
                    "RzStr": "RGA/Q11-13",
                    "Seats": "11-13",
                    "Section": "SGA"
                }
            ],
            "Seller": "ANMFZ1"
        }
    ]
}
```

## Get basket
$ softix get-basket 19115-32902968
```
{
    "Expiry": null,
    "Fees": null,
    "Id": "19115-32902968",
    "Offers": [
        {
            "Channel": null,
            "DateTime": "0001-01-01T00:00:00",
            "Demand": [
                {
                    "Admits": 3,
                    "Customer": null,
                    "Entitlement": null,
                    "OfferCode": null,
                    "PriceType": null,
                    "PriceTypeCode": "Q",
                    "PriceTypeId": null,
                    "Prices": [
                        {
                            "Fees": [
                                {
                                    "Bucket": null,
                                    "Code": null,
                                    "FinanceCode": null,
                                    "Id": null,
                                    "Inside": false,
                                    "Name": null,
                                    "SheetId": 0,
                                    "Total": 0,
                                    "Type": "1",
                                    "TypeName": "BookingFee"
                                }
                            ],
                            "Id": null,
                            "Net": 30000,
                            "SheetId": 0
                        }
                    ],
                    "QualifierCode": null,
                    "Quantity": 3
                }
            ],
            "Fees": [
                {
                    "Bucket": null,
                    "Code": "W",
                    "FinanceCode": null,
                    "Id": null,
                    "Inside": false,
                    "Name": null,
                    "SheetId": 0,
                    "Total": 0,
                    "Type": "5",
                    "TypeName": "Handling Fee"
                }
            ],
            "Id": "1",
            "InventorySource": {
                "Id": "19115:32902968",
                "Name": "Origin"
            },
            "PerformanceCode": "ETES0000004EL",
            "PriceCategory": null,
            "PriceCategoryCode": "1",
            "PriceCategoryId": "1",
            "Seats": [
                {
                    "Row": "GA",
                    "RzStr": "RGA/Q11-13",
                    "Seats": "-",
                    "Section": "SGA"
                }
            ],
            "Seller": null
        }
    ]
}
```
