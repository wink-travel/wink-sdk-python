# ImageAttributionNonAuthenticatedEntity

Whether image has attribution properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_lookup.models.image_attribution_non_authenticated_entity import ImageAttributionNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributionNonAuthenticatedEntity from a JSON string
image_attribution_non_authenticated_entity_instance = ImageAttributionNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ImageAttributionNonAuthenticatedEntity.to_json())

# convert the object into a dict
image_attribution_non_authenticated_entity_dict = image_attribution_non_authenticated_entity_instance.to_dict()
# create an instance of ImageAttributionNonAuthenticatedEntity from a dict
image_attribution_non_authenticated_entity_from_dict = ImageAttributionNonAuthenticatedEntity.from_dict(image_attribution_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


