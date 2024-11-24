# RateKeySupplier

Unique key for this rate update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** |  | 
**rate_plan_identifier** | **str** |  | 
**guest_room_identifier** | **str** |  | 
**var_date** | **date** |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.rate_key_supplier import RateKeySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RateKeySupplier from a JSON string
rate_key_supplier_instance = RateKeySupplier.from_json(json)
# print the JSON string representation of the object
print(RateKeySupplier.to_json())

# convert the object into a dict
rate_key_supplier_dict = rate_key_supplier_instance.to_dict()
# create an instance of RateKeySupplier from a dict
rate_key_supplier_from_dict = RateKeySupplier.from_dict(rate_key_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


