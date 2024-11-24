# DescriptiveReasonSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**map** | **Dict[str, str]** |  | [optional] 
**reasons** | **List[str]** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.descriptive_reason_supplier_details import DescriptiveReasonSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptiveReasonSupplierDetails from a JSON string
descriptive_reason_supplier_details_instance = DescriptiveReasonSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(DescriptiveReasonSupplierDetails.to_json())

# convert the object into a dict
descriptive_reason_supplier_details_dict = descriptive_reason_supplier_details_instance.to_dict()
# create an instance of DescriptiveReasonSupplierDetails from a dict
descriptive_reason_supplier_details_from_dict = DescriptiveReasonSupplierDetails.from_dict(descriptive_reason_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


