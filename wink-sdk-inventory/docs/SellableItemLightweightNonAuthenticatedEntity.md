# SellableItemLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique identifier | 
**owner_identifier** | **UUID** | AffiliateAccount / Owner identifier | 
**name** | **str** | Descriptive name of this item for seller use | 
**customization_identifier** | **UUID** | Which configuration to use with this item | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) |  | 
**keywords** | **List[str]** |  | 
**status** | **str** | Availability status | [default to 'ACTIVE']
**inventory_status** | **str** | Url sell status | 
**inventory_type** | **str** | The type of inventory being offer up for sale | 
**channel_inventory_type** | **str** | Channel inventory type is a subset of inventory type in that it does not include the &#x60;HOTEL&#x60; type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property. | 
**supplier_identifier** | **UUID** | Supplier / Hotel identifier that owns this inventory. | 
**channel_inventory_identifier** | **UUID** | The channel inventory record identifier describing the relationship between supplier and seller. | 
**multimedias** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) |  | 
**animate** | **bool** | Create an animated gif instead of a list of images. Feature currently not available. Feel free to enable and it will become available at a later date. | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. | [optional] 
**sort** | **str** | The specific badge to display over the image on the Web Component. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']

## Example

```python
from wink_sdk_inventory.models.sellable_item_lightweight_non_authenticated_entity import SellableItemLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableItemLightweightNonAuthenticatedEntity from a JSON string
sellable_item_lightweight_non_authenticated_entity_instance = SellableItemLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableItemLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_item_lightweight_non_authenticated_entity_dict = sellable_item_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of SellableItemLightweightNonAuthenticatedEntity from a dict
sellable_item_lightweight_non_authenticated_entity_from_dict = SellableItemLightweightNonAuthenticatedEntity.from_dict(sellable_item_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


