# UpsertSellableSupplierUrlRequestAffiliate

Upserts a SellableSupplierUrlLightweight entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name of this url for seller use only | 
**customization_identifier** | **str** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Localized link descriptions | 
**keywords** | **List[object]** |  | 
**twitter_account** | **str** | Twitter account is used with OpenGraph data | [optional] 
**facebook_app_id** | **str** | Facebook APP ID is used with OpenGraph data | [optional] 
**theme** | **str** | Url theme controls the look and feel of the ad banner. | [optional] 
**supplier_identifier** | **str** | The entity supplying the blocking. Usually a hotel. | 
**multimedia_identifiers** | **List[str]** | Cloudinary identifiers | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Animation delay in milliseconds | [optional] [default to -1]

## Example

```python
from wink_sdk_affiliate_inventory.models.upsert_sellable_supplier_url_request_affiliate import UpsertSellableSupplierUrlRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSellableSupplierUrlRequestAffiliate from a JSON string
upsert_sellable_supplier_url_request_affiliate_instance = UpsertSellableSupplierUrlRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSellableSupplierUrlRequestAffiliate.to_json())

# convert the object into a dict
upsert_sellable_supplier_url_request_affiliate_dict = upsert_sellable_supplier_url_request_affiliate_instance.to_dict()
# create an instance of UpsertSellableSupplierUrlRequestAffiliate from a dict
upsert_sellable_supplier_url_request_affiliate_from_dict = UpsertSellableSupplierUrlRequestAffiliate.from_dict(upsert_sellable_supplier_url_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


