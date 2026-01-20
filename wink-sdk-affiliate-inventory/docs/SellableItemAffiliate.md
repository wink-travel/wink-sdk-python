# SellableItemAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**owner_identifier** | **UUID** | AffiliateAccount / Owner identifier | 
**name** | **str** | Descriptive name of this item for seller use | 
**customization_identifier** | **UUID** | Which configuration to use with this item | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Title and description of inventory. | 
**keywords** | **List[str]** |  | 
**status** | **str** | Availability status | [default to 'ACTIVE']
**inventory_status** | **str** | Url sell status | 
**inventory_type** | **str** | The type of inventory being offer up for sale | 
**channel_inventory_type** | **str** | Channel inventory type is a subset of inventory type in that it does not include the &#x60;HOTEL&#x60; type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property. | 
**supplier_identifier** | **UUID** | Supplier / Hotel identifier that owns this inventory. | 
**channel_inventory_identifier** | **UUID** | The channel inventory record identifier describing the relationship between supplier and seller. | 
**multimedias** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) |  | 
**animate** | **bool** | Create an animated gif instead of a list of images. Feature currently not available. Feel free to enable and it will become available at a later date. | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. | [optional] 
**sort** | **str** | The specific badge to display over the image on the Web Component. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']

## Example

```python
from wink_sdk_affiliate_inventory.models.sellable_item_affiliate import SellableItemAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SellableItemAffiliate from a JSON string
sellable_item_affiliate_instance = SellableItemAffiliate.from_json(json)
# print the JSON string representation of the object
print(SellableItemAffiliate.to_json())

# convert the object into a dict
sellable_item_affiliate_dict = sellable_item_affiliate_instance.to_dict()
# create an instance of SellableItemAffiliate from a dict
sellable_item_affiliate_from_dict = SellableItemAffiliate.from_dict(sellable_item_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


