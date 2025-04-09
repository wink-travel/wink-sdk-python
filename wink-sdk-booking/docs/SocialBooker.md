# SocialBooker

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 

## Example

```python
from wink_sdk_booking.models.social_booker import SocialBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SocialBooker from a JSON string
social_booker_instance = SocialBooker.from_json(json)
# print the JSON string representation of the object
print(SocialBooker.to_json())

# convert the object into a dict
social_booker_dict = social_booker_instance.to_dict()
# create an instance of SocialBooker from a dict
social_booker_from_dict = SocialBooker.from_dict(social_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


