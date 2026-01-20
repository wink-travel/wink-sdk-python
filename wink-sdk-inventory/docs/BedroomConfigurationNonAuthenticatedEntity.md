# BedroomConfigurationNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[BedroomNonAuthenticatedEntity]**](BedroomNonAuthenticatedEntity.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_inventory.models.bedroom_configuration_non_authenticated_entity import BedroomConfigurationNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfigurationNonAuthenticatedEntity from a JSON string
bedroom_configuration_non_authenticated_entity_instance = BedroomConfigurationNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BedroomConfigurationNonAuthenticatedEntity.to_json())

# convert the object into a dict
bedroom_configuration_non_authenticated_entity_dict = bedroom_configuration_non_authenticated_entity_instance.to_dict()
# create an instance of BedroomConfigurationNonAuthenticatedEntity from a dict
bedroom_configuration_non_authenticated_entity_from_dict = BedroomConfigurationNonAuthenticatedEntity.from_dict(bedroom_configuration_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


