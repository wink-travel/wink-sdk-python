# SellerUrlAffiliate

Seller URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**seller_identifier** | **str** | Company identifier | 
**seller_url_name** | **str** | Descriptive name of this url for seller use only | 
**engine_configuration_identifier** | **str** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Localized link descriptions | 
**keywords** | **List[str]** | Keywords | 
**unique_id** | **str** | Unique link id | 
**twitter_account** | **str** | Twitter account is used with OpenGraph data | [optional] 
**facebook_app_id** | **str** | Facebook APP ID is used with OpenGraph data | [optional] 
**theme** | **str** | Url theme controls the look and feel of the ad banner. | 
**status** | **str** | Url sell status | 
**inventory_status** | **str** | Url sell status | 
**inventory_type** | **str** | Inventory type | 
**channel_inventory_type** | **str** | Channel inventory type is a subset of blocking type in that it does not include the &#x60;HOTEL&#x60; type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property. | 
**supplier_identifier** | **str** | The entity supplying the blocking. Usually a hotel. | 
**channel_inventory_identifier** | **str** | Selected blocking record | 
**transactional_item_identifier** | **str** | The transactional item to retrieve pricing for. If left empty, will find the cheapest priced item. | 
**multimedia_identifiers** | **List[str]** | Cloudinary identifiers | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Animation delay in milliseconds | [optional] [default to -1]

## Example

```python
from wink_sdk_affiliate_inventory.models.seller_url_affiliate import SellerUrlAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SellerUrlAffiliate from a JSON string
seller_url_affiliate_instance = SellerUrlAffiliate.from_json(json)
# print the JSON string representation of the object
print(SellerUrlAffiliate.to_json())

# convert the object into a dict
seller_url_affiliate_dict = seller_url_affiliate_instance.to_dict()
# create an instance of SellerUrlAffiliate from a dict
seller_url_affiliate_from_dict = SellerUrlAffiliate.from_dict(seller_url_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


