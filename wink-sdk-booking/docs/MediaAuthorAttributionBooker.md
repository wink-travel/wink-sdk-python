# MediaAuthorAttributionBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_booking.models.media_author_attribution_booker import MediaAuthorAttributionBooker

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttributionBooker from a JSON string
media_author_attribution_booker_instance = MediaAuthorAttributionBooker.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttributionBooker.to_json())

# convert the object into a dict
media_author_attribution_booker_dict = media_author_attribution_booker_instance.to_dict()
# create an instance of MediaAuthorAttributionBooker from a dict
media_author_attribution_booker_from_dict = MediaAuthorAttributionBooker.from_dict(media_author_attribution_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


