# ImageAttributionSupplier

Whether image has attribution properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_affiliate.models.image_attribution_supplier import ImageAttributionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributionSupplier from a JSON string
image_attribution_supplier_instance = ImageAttributionSupplier.from_json(json)
# print the JSON string representation of the object
print(ImageAttributionSupplier.to_json())

# convert the object into a dict
image_attribution_supplier_dict = image_attribution_supplier_instance.to_dict()
# create an instance of ImageAttributionSupplier from a dict
image_attribution_supplier_from_dict = ImageAttributionSupplier.from_dict(image_attribution_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


