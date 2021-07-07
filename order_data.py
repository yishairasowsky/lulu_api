from datetime import datetime

book = {
   "external_id": "test-line-item",
   "title": "My Book",
   "cover_source_url": "<online URL where to get the PDF of book's one-piece cover>",
   "interior_source_url": "<online URL where to get the PDF of interior>",
   "pod_package_id": "0550X0850BWSTDPB060UW444GXX",
   "quantity": 1,
}

external_id = "printjob-" + datetime.now().strftime("%Y%m%d__%H%M")

books = [book]

# Prepare line items from book order info in `books` list
line_items = []
for book in books:
    if "external_id" in book:
        item_external_id = book["external_id"]
    else:
        item_external_id = "item-" + datetime.now().strftime("%Y%m%d__%H%M")
    line_item = {
        "external_id": item_external_id,
        "printable_normalization": {
            "cover": { "source_url": book["cover_source_url"] },
            "interior": { "source_url": book["interior_source_url"] },
            "pod_package_id": book["pod_package_id"],
        },
        "quantity": book["quantity"],
        "title": book["title"],
    }
    line_items.append(line_item)

# POST data
address = {
   "name": "Hans Dampf",
   "street1": "Street address 1",
   "street2": "(optional) street address second line",
   "city": "Glenmont",
   "postcode": "12077",
   "state_code": "NY",
   "country_code": "US",
   "phone_number": "555-555-0689",
}
shipping_level = 'MAIL' 
"""
MAIL - Slowest ship method. Depending on the destination, tracking might not be available.
PRIORITY_MAIL - priority mail shipping
GROUND - Courier based shipping using ground transportation in the US.
EXPEDITED - expedited (2nd day) delivery via air mail or equivalent
EXPRESS - overnight delivery. Fastest shipping available.
"""
order_json = {
    "contact_email": 'myname@somesite.com',
    "external_id": external_id,
    "line_items": line_items,
    "production_delay": 30,
    "shipping_address": address, # continue here https://github.com/minireference/lulu-api-client/blob/358395d21685245f75a60094c2f7d80b6b3dddb1/luluapi.py#:~:text=self%2C%20address%2C%20books-,%2C,-shipping_level%2C%20external_id%3DNone
    "shipping_level": shipping_level,
}