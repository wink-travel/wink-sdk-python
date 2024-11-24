# BucketListEntryAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_list_identifier** | **str** |  | 
**user_identifier** | **str** |  | 
**type** | **str** |  | 
**identifier** | **str** |  | 
**channel_inventory_identifier** | **str** |  | 
**inventory_name** | **str** |  | 
**engine_identifier** | **str** |  | 
**engine_configuration_identifier** | **str** |  | 
**client_id** | **str** |  | 

## Example

```python
from wink_sdk_user_settings.models.bucket_list_entry_authenticated_entity import BucketListEntryAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BucketListEntryAuthenticatedEntity from a JSON string
bucket_list_entry_authenticated_entity_instance = BucketListEntryAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BucketListEntryAuthenticatedEntity.to_json())

# convert the object into a dict
bucket_list_entry_authenticated_entity_dict = bucket_list_entry_authenticated_entity_instance.to_dict()
# create an instance of BucketListEntryAuthenticatedEntity from a dict
bucket_list_entry_authenticated_entity_from_dict = BucketListEntryAuthenticatedEntity.from_dict(bucket_list_entry_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


