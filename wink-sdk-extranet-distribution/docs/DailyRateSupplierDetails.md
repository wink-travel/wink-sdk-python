# DailyRateSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_base_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_base_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_base_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_extra_pax_modifier** | **float** |  | [optional] 
**internal_extra_pax_modifier** | **float** |  | [optional] 
**user_specified_currency_extra_pax_modifier** | **float** |  | [optional] 
**source_extra_child_modifier** | **float** |  | [optional] 
**internal_extra_child_modifier** | **float** |  | [optional] 
**user_specified_currency_extra_child_modifier** | **float** |  | [optional] 
**source_single_occupant_modifier** | **float** |  | [optional] 
**internal_single_occupant_modifier** | **float** |  | [optional] 
**user_specified_currency_single_occupant_modifier** | **float** |  | [optional] 
**source_promotional_modifier** | **float** |  | [optional] 
**internal_promotional_modifier** | **float** |  | [optional] 
**user_specified_currency_promotional_modifier** | **float** |  | [optional] 
**source_premium_modifier** | **float** |  | [optional] 
**internal_premium_modifier** | **float** |  | [optional] 
**user_specified_currency_premium_modifier** | **float** |  | [optional] 
**source_channel_modifier** | **float** |  | [optional] 
**internal_channel_modifier** | **float** |  | [optional] 
**user_specified_currency_channel_modifier** | **float** |  | [optional] 
**available** | **bool** |  | [optional] 
**is_start_date** | **bool** |  | [optional] 
**is_end_date** | **bool** |  | [optional] 
**is_between_date** | **bool** |  | [optional] 
**is_last_night** | **bool** |  | [optional] 
**offer_details** | [**List[LocalizedDescriptionSupplierDetails]**](LocalizedDescriptionSupplierDetails.md) |  | [optional] 
**has_modification** | **bool** |  | [optional] 
**is_bundled_modifier** | **bool** |  | [optional] 
**has_channel_discount** | **bool** |  | [optional] 
**channel_discount_percent** | **float** |  | [optional] 
**promotional_discount_percent** | **float** |  | [optional] 
**premium_percent** | **float** |  | [optional] 
**promotion** | **str** |  | [optional] 
**adults** | **int** |  | [optional] 
**children** | **int** |  | [optional] 
**rate** | [**DailyRateRateSupplierDetails**](DailyRateRateSupplierDetails.md) |  | 
**max_adult_occupancy** | **int** | Maximum number of adults allowed in a room type. | [default to 2]
**max_child_occupancy** | **int** | Maximum number of children allowed in a room type. | [default to 0]
**included_adult_occupancy** | **int** | The number of pax the room price was meant for | [default to 2]
**included_child_occupancy** | **int** | The number of children the room price was meant for | [default to 0]
**source_to_user_currency_quote** | [**QuoteLightweightSupplierDetails**](QuoteLightweightSupplierDetails.md) |  | 
**source_to_internal_currency_quote** | [**QuoteLightweightSupplierDetails**](QuoteLightweightSupplierDetails.md) |  | 
**phantom** | **bool** |  | 
**var_date** | **date** |  | [optional] 
**quantity** | **int** |  | [optional] 
**source_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**end_date** | **bool** |  | [optional] 
**max_occupancy** | **int** |  | [optional] 
**min_occupancy** | **int** |  | [optional] 
**base_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**min_los** | **int** |  | [optional] 
**max_los** | **int** |  | [optional] 
**total_discount_percent** | **float** |  | [optional] 
**close_on_departure** | **bool** |  | [optional] 
**inventory_available** | **bool** |  | [optional] 
**master_availability** | **bool** |  | [optional] 
**close_on_arrival** | **bool** |  | [optional] 
**rate_identifier** | **str** |  | [optional] 
**start_date** | **bool** |  | [optional] 
**between_date** | **bool** |  | [optional] 
**last_night** | **bool** |  | [optional] 
**bundled_modifier** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.daily_rate_supplier_details import DailyRateSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRateSupplierDetails from a JSON string
daily_rate_supplier_details_instance = DailyRateSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(DailyRateSupplierDetails.to_json())

# convert the object into a dict
daily_rate_supplier_details_dict = daily_rate_supplier_details_instance.to_dict()
# create an instance of DailyRateSupplierDetails from a dict
daily_rate_supplier_details_from_dict = DailyRateSupplierDetails.from_dict(daily_rate_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


