# StaticListItemAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**parent** | [**StaticListLightweightAffiliate**](StaticListLightweightAffiliate.md) | Parent list | 
**item** | [**StaticListItemInventoryAffiliate**](StaticListItemInventoryAffiliate.md) | Channel inventory | 
**sort** | **int** | Sort key | [optional] 
**status** | **str** | Status | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticListItemAffiliate from a JSON string
static_list_item_affiliate_instance = StaticListItemAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticListItemAffiliate.to_json())

# convert the object into a dict
static_list_item_affiliate_dict = static_list_item_affiliate_instance.to_dict()
# create an instance of StaticListItemAffiliate from a dict
static_list_item_affiliate_from_dict = StaticListItemAffiliate.from_dict(static_list_item_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


