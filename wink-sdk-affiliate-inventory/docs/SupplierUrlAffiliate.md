# SupplierUrlAffiliate

Supplier URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**seller_identifier** | **str** | Company identifier | 
**supplier_url_name** | **str** | Descriptive supplierUrlName of this url for seller use only | 
**engine_configuration_identifier** | **str** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Localized link descriptions | 
**keywords** | **List[str]** |  | 
**unique_id** | **str** | Unique link id | 
**twitter_account** | **str** | Twitter account is used with OpenGraph data | [optional] 
**facebook_app_id** | **str** | Facebook APP ID is used with OpenGraph data | [optional] 
**theme** | **str** | Url theme controls the look and feel of the ad banner. | [optional] 
**status** | **str** | Url sell status | 
**supplier_identifier** | **str** | The entity supplying the blocking. Usually a hotel. | 
**multimedia_identifiers** | **List[str]** | Cloudinary identifiers | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Animation delay in milliseconds | [optional] [default to -1]

## Example

```python
from wink_sdk_affiliate_inventory.models.supplier_url_affiliate import SupplierUrlAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierUrlAffiliate from a JSON string
supplier_url_affiliate_instance = SupplierUrlAffiliate.from_json(json)
# print the JSON string representation of the object
print(SupplierUrlAffiliate.to_json())

# convert the object into a dict
supplier_url_affiliate_dict = supplier_url_affiliate_instance.to_dict()
# create an instance of SupplierUrlAffiliate from a dict
supplier_url_affiliate_from_dict = SupplierUrlAffiliate.from_dict(supplier_url_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


