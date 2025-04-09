# ChannelNameSupplierDetails

Channel owner of blocking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_identifier** | **str** |  | 
**sub_type** | **str** |  | 
**owner_identifier** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.channel_name_supplier_details import ChannelNameSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelNameSupplierDetails from a JSON string
channel_name_supplier_details_instance = ChannelNameSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ChannelNameSupplierDetails.to_json())

# convert the object into a dict
channel_name_supplier_details_dict = channel_name_supplier_details_instance.to_dict()
# create an instance of ChannelNameSupplierDetails from a dict
channel_name_supplier_details_from_dict = ChannelNameSupplierDetails.from_dict(channel_name_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


