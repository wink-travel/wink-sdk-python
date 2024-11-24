# PageHotelWithBestPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[HotelWithBestPriceNonAuthenticatedEntity]**](HotelWithBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.page_hotel_with_best_price_non_authenticated_entity import PageHotelWithBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageHotelWithBestPriceNonAuthenticatedEntity from a JSON string
page_hotel_with_best_price_non_authenticated_entity_instance = PageHotelWithBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageHotelWithBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_hotel_with_best_price_non_authenticated_entity_dict = page_hotel_with_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of PageHotelWithBestPriceNonAuthenticatedEntity from a dict
page_hotel_with_best_price_non_authenticated_entity_from_dict = PageHotelWithBestPriceNonAuthenticatedEntity.from_dict(page_hotel_with_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


