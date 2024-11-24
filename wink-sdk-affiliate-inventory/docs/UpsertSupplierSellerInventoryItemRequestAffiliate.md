# UpsertSupplierSellerInventoryItemRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_inventory_item_name** | **str** | Descriptive name of this item for seller use | 
**engine_configuration_identifier** | **str** | Which configuration to use with this item | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Title and description of blocking. | 
**keywords** | **List[str]** |  | 
**inventory_type** | **str** | The type of blocking being offer up for sale | 
**channel_inventory_type** | **str** | Channel blocking type is a subset of blocking type in that it does not include the &#x60;HOTEL&#x60; type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property. | 
**supplier_identifier** | **str** | Supplier / Hotel identifier that owns this blocking. | 
**multimedia_identifiers** | **List[str]** | Reference identifiers to Cloudinary media assets | 
**animate** | **bool** | Create an animated gif instead of a list of images. Feature currently not available. Feel free to enable and it will become available at a later date. | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. | [optional] 
**sort** | **str** | The specific badge to display over the image on the Web Component. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']

## Example

```python
from wink_sdk_affiliate_inventory.models.upsert_supplier_seller_inventory_item_request_affiliate import UpsertSupplierSellerInventoryItemRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSupplierSellerInventoryItemRequestAffiliate from a JSON string
upsert_supplier_seller_inventory_item_request_affiliate_instance = UpsertSupplierSellerInventoryItemRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSupplierSellerInventoryItemRequestAffiliate.to_json())

# convert the object into a dict
upsert_supplier_seller_inventory_item_request_affiliate_dict = upsert_supplier_seller_inventory_item_request_affiliate_instance.to_dict()
# create an instance of UpsertSupplierSellerInventoryItemRequestAffiliate from a dict
upsert_supplier_seller_inventory_item_request_affiliate_from_dict = UpsertSupplierSellerInventoryItemRequestAffiliate.from_dict(upsert_supplier_seller_inventory_item_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


