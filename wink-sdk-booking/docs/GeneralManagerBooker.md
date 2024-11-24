# GeneralManagerBooker

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaBooker**](SimpleMultimediaBooker.md) |  | [optional] 
**descriptions** | [**List[LocalizedDescriptionBooker]**](LocalizedDescriptionBooker.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_booking.models.general_manager_booker import GeneralManagerBooker

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerBooker from a JSON string
general_manager_booker_instance = GeneralManagerBooker.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerBooker.to_json())

# convert the object into a dict
general_manager_booker_dict = general_manager_booker_instance.to_dict()
# create an instance of GeneralManagerBooker from a dict
general_manager_booker_from_dict = GeneralManagerBooker.from_dict(general_manager_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


