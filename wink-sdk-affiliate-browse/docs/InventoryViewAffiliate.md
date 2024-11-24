# InventoryViewAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**inventory** | [**InventoryAffiliate**](InventoryAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_browse.models.inventory_view_affiliate import InventoryViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryViewAffiliate from a JSON string
inventory_view_affiliate_instance = InventoryViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventoryViewAffiliate.to_json())

# convert the object into a dict
inventory_view_affiliate_dict = inventory_view_affiliate_instance.to_dict()
# create an instance of InventoryViewAffiliate from a dict
inventory_view_affiliate_from_dict = InventoryViewAffiliate.from_dict(inventory_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


