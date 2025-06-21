# ImageAttributionSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_extranet_distribution.models.image_attribution_supplier_details import ImageAttributionSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributionSupplierDetails from a JSON string
image_attribution_supplier_details_instance = ImageAttributionSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ImageAttributionSupplierDetails.to_json())

# convert the object into a dict
image_attribution_supplier_details_dict = image_attribution_supplier_details_instance.to_dict()
# create an instance of ImageAttributionSupplierDetails from a dict
image_attribution_supplier_details_from_dict = ImageAttributionSupplierDetails.from_dict(image_attribution_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


