# DynamicSellerListAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique search result identifier gets populated for when you want to save your query. | 
**owner_identifier** | **str** | Entity identifier of record creator | 
**name** | **str** | Name of dynamic list for when user want to persist it | 
**property_name** | **str** | Regex expression filter matching on property name. | [optional] 
**location_categories** | **List[str]** | Supported OTA specification &#x60;LOC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**segment_categories** | **List[str]** | Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**hotel_categories** | **List[str]** | Supported OTA specification &#x60;PCT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**architectural_styles** | **List[str]** | Supported OTA specification &#x60;ARC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**inventory_name** | **str** | Regex expression filter matching on blocking name | [optional] 
**continents** | **List[str]** | Continent filter | [optional] 
**countries** | **List[str]** | Country filter | [optional] 
**cities** | **List[str]** | City filter | [optional] 
**show_eco_friendly** | **bool** | Filter on eco-friendly hotels | [optional] [default to False]
**show_pet_friendly** | **bool** | Filter on pet-friendly hotels | [optional] [default to False]
**show_child_friendly** | **bool** | Filter on child-friendly hotels | [optional] [default to False]
**show_popular** | **bool** | Filter on hotel that has had a certain amount of bookings | [optional] [default to False]
**show_direct_only** | **bool** | Filter on direct blocking | [optional] [default to False]
**lifestyles** | **List[str]** | Filter on lifestyles | [optional] 
**hotel_stars** | **int** | Filter on number of stars the hotel has. | [optional] 
**aggregate_review_rating** | **int** | Filter on aggregate review score the hotel has | [optional] 
**near_point** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) |  | [optional] 
**radius_in_meters** | **int** | Use this in conjunction with &#x60;nearPoint&#x60;. Control the distance from point we are searching for. | [optional] [default to 0]
**inventory_types** | **List[str]** | Filter on blocking types | [optional] 
**primary_order_by** | **str** | Control how you want the search results sorted. Options are:  - 1: Inventory name - 2: Price: High to low - 3: Price: Low to high - 4: Commission: High to low - 5: Commission: Low to high - 6: Discount: High to low - 7: Discount: Low to high  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.dynamic_seller_list_affiliate import DynamicSellerListAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSellerListAffiliate from a JSON string
dynamic_seller_list_affiliate_instance = DynamicSellerListAffiliate.from_json(json)
# print the JSON string representation of the object
print(DynamicSellerListAffiliate.to_json())

# convert the object into a dict
dynamic_seller_list_affiliate_dict = dynamic_seller_list_affiliate_instance.to_dict()
# create an instance of DynamicSellerListAffiliate from a dict
dynamic_seller_list_affiliate_from_dict = DynamicSellerListAffiliate.from_dict(dynamic_seller_list_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


