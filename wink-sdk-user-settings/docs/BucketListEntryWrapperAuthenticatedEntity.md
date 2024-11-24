# BucketListEntryWrapperAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**BucketListEntryAuthenticatedEntity**](BucketListEntryAuthenticatedEntity.md) |  | 
**inventory** | [**InventoryAuthenticatedEntity**](InventoryAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_user_settings.models.bucket_list_entry_wrapper_authenticated_entity import BucketListEntryWrapperAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BucketListEntryWrapperAuthenticatedEntity from a JSON string
bucket_list_entry_wrapper_authenticated_entity_instance = BucketListEntryWrapperAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BucketListEntryWrapperAuthenticatedEntity.to_json())

# convert the object into a dict
bucket_list_entry_wrapper_authenticated_entity_dict = bucket_list_entry_wrapper_authenticated_entity_instance.to_dict()
# create an instance of BucketListEntryWrapperAuthenticatedEntity from a dict
bucket_list_entry_wrapper_authenticated_entity_from_dict = BucketListEntryWrapperAuthenticatedEntity.from_dict(bucket_list_entry_wrapper_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


