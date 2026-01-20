# ChannelManagerProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Property ID | 
**name** | **str** | Property name | 
**city** | **str** | City property is located in or near | 
**country_code** | **str** | Country code property is located in | 
**currency_code** | **str** | Currency code property uses | 
**time_zone** | **str** | Timezone property is located in | 

## Example

```python
from wink_sdk_channel_manager.models.channel_manager_property import ChannelManagerProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelManagerProperty from a JSON string
channel_manager_property_instance = ChannelManagerProperty.from_json(json)
# print the JSON string representation of the object
print(ChannelManagerProperty.to_json())

# convert the object into a dict
channel_manager_property_dict = channel_manager_property_instance.to_dict()
# create an instance of ChannelManagerProperty from a dict
channel_manager_property_from_dict = ChannelManagerProperty.from_dict(channel_manager_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


