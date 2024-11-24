# KeyValuePairAdministrator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value that should be persisted. | 
**label** | **str** | English readable text of the value. | 

## Example

```python
from wink_sdk_reference.models.key_value_pair_administrator import KeyValuePairAdministrator

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairAdministrator from a JSON string
key_value_pair_administrator_instance = KeyValuePairAdministrator.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairAdministrator.to_json())

# convert the object into a dict
key_value_pair_administrator_dict = key_value_pair_administrator_instance.to_dict()
# create an instance of KeyValuePairAdministrator from a dict
key_value_pair_administrator_from_dict = KeyValuePairAdministrator.from_dict(key_value_pair_administrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


