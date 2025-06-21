# UpdateChannelManagerRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_provider** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) | Property&#39;s channel manager. Rate ownership is decided based on the channel manager selected. This can be both an enum and an identifier. | 

## Example

```python
from wink_sdk_extranet_property.models.update_channel_manager_request_supplier import UpdateChannelManagerRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChannelManagerRequestSupplier from a JSON string
update_channel_manager_request_supplier_instance = UpdateChannelManagerRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpdateChannelManagerRequestSupplier.to_json())

# convert the object into a dict
update_channel_manager_request_supplier_dict = update_channel_manager_request_supplier_instance.to_dict()
# create an instance of UpdateChannelManagerRequestSupplier from a dict
update_channel_manager_request_supplier_from_dict = UpdateChannelManagerRequestSupplier.from_dict(update_channel_manager_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


