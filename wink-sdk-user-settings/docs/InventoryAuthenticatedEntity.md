# InventoryAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**sales_channel** | [**SalesChannelLightweightAuthenticatedEntity**](SalesChannelLightweightAuthenticatedEntity.md) | Parent sales channel | 
**inventory_type** | **str** | Inventory type | 
**inventory_identifier** | **str** | Inventory type identifier | 
**inventory_name** | **str** | Name of inventory as hotel is seeing it | 
**inventory_name_in_english** | **str** | Name of inventory as traveler is seeing it | 
**enabled** | **bool** | Whether this inventory is enabled or not | [default to True]
**image** | [**SimpleMultimediaAuthenticatedEntity**](SimpleMultimediaAuthenticatedEntity.md) | Main image of inventory | 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**location** | [**GeoJsonPointAuthenticatedEntity**](GeoJsonPointAuthenticatedEntity.md) | Location | 
**address** | [**InventoryAddressAuthenticatedEntity**](InventoryAddressAuthenticatedEntity.md) | Defaults to property address. | 
**quantity** | **int** | quantity | [default to 0]
**commissionable** | **bool** | Whether this is commissionable or not | [default to False]
**bookable** | **bool** | Whether inventory can be booked | [default to True]
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary in platform currency | [optional] 

## Example

```python
from wink_sdk_user_settings.models.inventory_authenticated_entity import InventoryAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAuthenticatedEntity from a JSON string
inventory_authenticated_entity_instance = InventoryAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InventoryAuthenticatedEntity.to_json())

# convert the object into a dict
inventory_authenticated_entity_dict = inventory_authenticated_entity_instance.to_dict()
# create an instance of InventoryAuthenticatedEntity from a dict
inventory_authenticated_entity_from_dict = InventoryAuthenticatedEntity.from_dict(inventory_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


