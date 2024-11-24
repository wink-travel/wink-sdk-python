# LengthOfStayRateQualifierSupplier

Restrict promotion to users who want to stay a certain number of days.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_los** | **int** | Minimum length of stay qualifier | [optional] 
**max_los** | **int** | Maximum length of stay qualifier | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.length_of_stay_rate_qualifier_supplier import LengthOfStayRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of LengthOfStayRateQualifierSupplier from a JSON string
length_of_stay_rate_qualifier_supplier_instance = LengthOfStayRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(LengthOfStayRateQualifierSupplier.to_json())

# convert the object into a dict
length_of_stay_rate_qualifier_supplier_dict = length_of_stay_rate_qualifier_supplier_instance.to_dict()
# create an instance of LengthOfStayRateQualifierSupplier from a dict
length_of_stay_rate_qualifier_supplier_from_dict = LengthOfStayRateQualifierSupplier.from_dict(length_of_stay_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


