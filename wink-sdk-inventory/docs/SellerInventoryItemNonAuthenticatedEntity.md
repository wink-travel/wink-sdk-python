# SellerInventoryItemNonAuthenticatedEntity

Identifier blocking record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**seller_identifier** | **str** | Company / Owner identifier | 
**seller_inventory_item_name** | **str** | Descriptive name of this item for seller use | 
**engine_configuration_identifier** | **str** | Which configuration to use with this item | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | Title and description of blocking. | 
**keywords** | **List[str]** |  | 
**status** | **str** | Availability status | [default to 'ACTIVE']
**inventory_status** | **str** | Url sell status | 
**inventory_type** | **str** | The type of blocking being offer up for sale | 
**channel_inventory_type** | **str** | Channel blocking type is a subset of blocking type in that it does not include the &#x60;HOTEL&#x60; type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property. | 
**supplier_identifier** | **str** | Supplier / Hotel identifier that owns this blocking. | 
**channel_inventory_identifier** | **str** | The channel blocking record identifier describing the relationship between supplier and seller. | 
**multimedia_identifiers** | **List[str]** | Reference identifiers to Cloudinary media assets | 
**animate** | **bool** | Create an animated gif instead of a list of images. Feature currently not available. Feel free to enable and it will become available at a later date. | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. | [optional] 
**sort** | **str** | The specific badge to display over the image on the Web Component. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']

## Example

```python
from wink_sdk_inventory.models.seller_inventory_item_non_authenticated_entity import SellerInventoryItemNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryItemNonAuthenticatedEntity from a JSON string
seller_inventory_item_non_authenticated_entity_instance = SellerInventoryItemNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryItemNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_item_non_authenticated_entity_dict = seller_inventory_item_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryItemNonAuthenticatedEntity from a dict
seller_inventory_item_non_authenticated_entity_from_dict = SellerInventoryItemNonAuthenticatedEntity.from_dict(seller_inventory_item_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


