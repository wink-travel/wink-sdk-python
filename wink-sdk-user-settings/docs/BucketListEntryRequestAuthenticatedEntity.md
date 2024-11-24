# BucketListEntryRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**identifier** | **str** |  | 
**channel_inventory_identifier** | **str** |  | 
**inventory_name** | **str** |  | 
**engine_configuration_identifier** | **str** |  | 

## Example

```python
from wink_sdk_user_settings.models.bucket_list_entry_request_authenticated_entity import BucketListEntryRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BucketListEntryRequestAuthenticatedEntity from a JSON string
bucket_list_entry_request_authenticated_entity_instance = BucketListEntryRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BucketListEntryRequestAuthenticatedEntity.to_json())

# convert the object into a dict
bucket_list_entry_request_authenticated_entity_dict = bucket_list_entry_request_authenticated_entity_instance.to_dict()
# create an instance of BucketListEntryRequestAuthenticatedEntity from a dict
bucket_list_entry_request_authenticated_entity_from_dict = BucketListEntryRequestAuthenticatedEntity.from_dict(bucket_list_entry_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


