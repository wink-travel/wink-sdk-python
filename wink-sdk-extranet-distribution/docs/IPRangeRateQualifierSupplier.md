# IPRangeRateQualifierSupplier

Restrict promotion to specific IP ranges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_ip_range** | **str** | start of IP range | 
**end_ip_range** | **str** | end of IP range | 

## Example

```python
from wink_sdk_extranet_distribution.models.ip_range_rate_qualifier_supplier import IPRangeRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of IPRangeRateQualifierSupplier from a JSON string
ip_range_rate_qualifier_supplier_instance = IPRangeRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(IPRangeRateQualifierSupplier.to_json())

# convert the object into a dict
ip_range_rate_qualifier_supplier_dict = ip_range_rate_qualifier_supplier_instance.to_dict()
# create an instance of IPRangeRateQualifierSupplier from a dict
ip_range_rate_qualifier_supplier_from_dict = IPRangeRateQualifierSupplier.from_dict(ip_range_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


