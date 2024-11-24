# BrowseSuppliers400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.browse_suppliers400_response import BrowseSuppliers400Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseSuppliers400Response from a JSON string
browse_suppliers400_response_instance = BrowseSuppliers400Response.from_json(json)
# print the JSON string representation of the object
print(BrowseSuppliers400Response.to_json())

# convert the object into a dict
browse_suppliers400_response_dict = browse_suppliers400_response_instance.to_dict()
# create an instance of BrowseSuppliers400Response from a dict
browse_suppliers400_response_from_dict = BrowseSuppliers400Response.from_dict(browse_suppliers400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


