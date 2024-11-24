# ImageAttributionAuthenticatedEntity

Whether image has attribution properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_user_settings.models.image_attribution_authenticated_entity import ImageAttributionAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributionAuthenticatedEntity from a JSON string
image_attribution_authenticated_entity_instance = ImageAttributionAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ImageAttributionAuthenticatedEntity.to_json())

# convert the object into a dict
image_attribution_authenticated_entity_dict = image_attribution_authenticated_entity_instance.to_dict()
# create an instance of ImageAttributionAuthenticatedEntity from a dict
image_attribution_authenticated_entity_from_dict = ImageAttributionAuthenticatedEntity.from_dict(image_attribution_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


