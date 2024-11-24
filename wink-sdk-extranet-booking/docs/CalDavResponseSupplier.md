# CalDavResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**hotel_identifier** | **str** |  | [optional] 
**passkey** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.cal_dav_response_supplier import CalDavResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CalDavResponseSupplier from a JSON string
cal_dav_response_supplier_instance = CalDavResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(CalDavResponseSupplier.to_json())

# convert the object into a dict
cal_dav_response_supplier_dict = cal_dav_response_supplier_instance.to_dict()
# create an instance of CalDavResponseSupplier from a dict
cal_dav_response_supplier_from_dict = CalDavResponseSupplier.from_dict(cal_dav_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


