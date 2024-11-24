# DowPatternGroupBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mon** | **bool** | Set to &#x60;true&#x60; to enable Monday. | [optional] 
**tue** | **bool** | Set to &#x60;true&#x60; to enable Tuesday. | [optional] 
**wed** | **bool** | Set to &#x60;true&#x60; to enable Wednesday. | [optional] 
**thu** | **bool** | Set to &#x60;true&#x60; to enable Thursday. | [optional] 
**fri** | **bool** | Set to &#x60;true&#x60; to enable Friday. | [optional] 
**sat** | **bool** | Set to &#x60;true&#x60; to enable Saturday. | [optional] 
**sun** | **bool** | Set to &#x60;true&#x60; to enable Sunday. | [optional] 
**disabled** | **bool** | Convenience property to quickly determine if this existing object has any active days enabled. | [optional] 

## Example

```python
from wink_sdk_booking.models.dow_pattern_group_booker import DowPatternGroupBooker

# TODO update the JSON string below
json = "{}"
# create an instance of DowPatternGroupBooker from a JSON string
dow_pattern_group_booker_instance = DowPatternGroupBooker.from_json(json)
# print the JSON string representation of the object
print(DowPatternGroupBooker.to_json())

# convert the object into a dict
dow_pattern_group_booker_dict = dow_pattern_group_booker_instance.to_dict()
# create an instance of DowPatternGroupBooker from a dict
dow_pattern_group_booker_from_dict = DowPatternGroupBooker.from_dict(dow_pattern_group_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


