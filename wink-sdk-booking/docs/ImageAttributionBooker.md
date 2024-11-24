# ImageAttributionBooker

Whether image has attribution properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_booking.models.image_attribution_booker import ImageAttributionBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributionBooker from a JSON string
image_attribution_booker_instance = ImageAttributionBooker.from_json(json)
# print the JSON string representation of the object
print(ImageAttributionBooker.to_json())

# convert the object into a dict
image_attribution_booker_dict = image_attribution_booker_instance.to_dict()
# create an instance of ImageAttributionBooker from a dict
image_attribution_booker_from_dict = ImageAttributionBooker.from_dict(image_attribution_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


