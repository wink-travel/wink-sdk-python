# ChannelNameSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | **str** |  | 
**owner_identifier** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.channel_name_supplier import ChannelNameSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelNameSupplier from a JSON string
channel_name_supplier_instance = ChannelNameSupplier.from_json(json)
# print the JSON string representation of the object
print(ChannelNameSupplier.to_json())

# convert the object into a dict
channel_name_supplier_dict = channel_name_supplier_instance.to_dict()
# create an instance of ChannelNameSupplier from a dict
channel_name_supplier_from_dict = ChannelNameSupplier.from_dict(channel_name_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


