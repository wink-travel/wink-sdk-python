# CountResponseNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True if count query worked. | 
**count** | **int** | Number of reviews for this property. | 

## Example

```python
from wink_sdk_reference.models.count_response_non_authenticated_entity import CountResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CountResponseNonAuthenticatedEntity from a JSON string
count_response_non_authenticated_entity_instance = CountResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CountResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
count_response_non_authenticated_entity_dict = count_response_non_authenticated_entity_instance.to_dict()
# create an instance of CountResponseNonAuthenticatedEntity from a dict
count_response_non_authenticated_entity_from_dict = CountResponseNonAuthenticatedEntity.from_dict(count_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


