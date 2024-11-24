# SocialSupplierDetails

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 
**enabled** | **bool** | Whether social network is available for use. | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.social_supplier_details import SocialSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SocialSupplierDetails from a JSON string
social_supplier_details_instance = SocialSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SocialSupplierDetails.to_json())

# convert the object into a dict
social_supplier_details_dict = social_supplier_details_instance.to_dict()
# create an instance of SocialSupplierDetails from a dict
social_supplier_details_from_dict = SocialSupplierDetails.from_dict(social_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


