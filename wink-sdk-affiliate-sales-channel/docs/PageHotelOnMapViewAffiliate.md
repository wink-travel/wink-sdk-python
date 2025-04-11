# PageHotelOnMapViewAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[HotelOnMapViewAffiliate]**](HotelOnMapViewAffiliate.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectAffiliate**](PageableObjectAffiliate.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.page_hotel_on_map_view_affiliate import PageHotelOnMapViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PageHotelOnMapViewAffiliate from a JSON string
page_hotel_on_map_view_affiliate_instance = PageHotelOnMapViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(PageHotelOnMapViewAffiliate.to_json())

# convert the object into a dict
page_hotel_on_map_view_affiliate_dict = page_hotel_on_map_view_affiliate_instance.to_dict()
# create an instance of PageHotelOnMapViewAffiliate from a dict
page_hotel_on_map_view_affiliate_from_dict = PageHotelOnMapViewAffiliate.from_dict(page_hotel_on_map_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


