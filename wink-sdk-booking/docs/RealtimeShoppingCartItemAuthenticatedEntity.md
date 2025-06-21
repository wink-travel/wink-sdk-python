# RealtimeShoppingCartItemAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | identifier for item in cart | 
**hotel_identifier** | **str** | Unique hotel record identifier. | 
**start_date** | **date** | Date when guest arrives on the premises. | 
**end_date** | **date** | Date when guest departs the premises. | 
**room_configuration** | [**RoomConfigurationAuthenticatedEntity**](RoomConfigurationAuthenticatedEntity.md) | Room configuration is how the guest wants the room to support her accompanying guests. | 
**promotional_codes** | **List[object]** |  | [optional] 
**room_rate_identifier** | **str** | The unique master rate that made the guest room / rate plan available for sale. | 
**bedroom_configuration_identifier** | **str** | Guest can optionally request a specific bedroom layout if the room type is set up with multiple layout choices. | [optional] 
**ancillaries** | **List[object]** |  | [optional] 
**special_requests** | **str** | A guest can send a special request to the hotel in free-text here. | [optional] 
**user** | [**BookingUserRequestAuthenticatedEntity**](BookingUserRequestAuthenticatedEntity.md) | User object contains details of the person that made the booking. | 
**hotel** | [**PropertyAggregateLightweightAuthenticatedEntity**](PropertyAggregateLightweightAuthenticatedEntity.md) | The hotel where the stay occurs. | 
**stay** | [**RoomStayAuthenticatedEntity**](RoomStayAuthenticatedEntity.md) | The priced stay. | 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | 
**commission** | **float** | The commission percentage. | 
**language** | **str** | User&#39;s language preference | 
**currency** | **str** | User&#39;s currency preference | 
**lifestyle** | **str** | Control which lifestyle context your user was in. | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.realtime_shopping_cart_item_authenticated_entity import RealtimeShoppingCartItemAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RealtimeShoppingCartItemAuthenticatedEntity from a JSON string
realtime_shopping_cart_item_authenticated_entity_instance = RealtimeShoppingCartItemAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RealtimeShoppingCartItemAuthenticatedEntity.to_json())

# convert the object into a dict
realtime_shopping_cart_item_authenticated_entity_dict = realtime_shopping_cart_item_authenticated_entity_instance.to_dict()
# create an instance of RealtimeShoppingCartItemAuthenticatedEntity from a dict
realtime_shopping_cart_item_authenticated_entity_from_dict = RealtimeShoppingCartItemAuthenticatedEntity.from_dict(realtime_shopping_cart_item_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


