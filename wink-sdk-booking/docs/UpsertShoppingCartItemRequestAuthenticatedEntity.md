# UpsertShoppingCartItemRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Unique hotel record identifier. | 
**start_date** | **date** | Date when guest arrives on the premises. | 
**end_date** | **date** | Date when guest departs the premises. Optional if nights is specified. | [optional] 
**nights** | **int** | Date when guest departs the premises. Optional if endDate is specified. | [optional] 
**room_configuration** | [**RoomConfigurationAuthenticatedEntity**](RoomConfigurationAuthenticatedEntity.md) |  | 
**promotional_codes** | **List[str]** |  | [optional] 
**room_rate_identifier** | **str** | The unique master rate that made the guest room / rate plan available for sale. | 
**bedroom_configuration_identifier** | **str** | Guest can optionally request a specific bedroom layout if the room type is set up with multiple layout choices. | [optional] 
**ancillaries** | [**List[AncillaryRequestAuthenticatedEntity]**](AncillaryRequestAuthenticatedEntity.md) |  | [optional] 
**special_requests** | **str** | A guest can send a special request to the hotel in free-text here. | [optional] 
**user** | [**BookingUserRequestAuthenticatedEntity**](BookingUserRequestAuthenticatedEntity.md) |  | 
**language** | **str** | User&#39;s language preference | [optional] 
**currency** | **str** | User&#39;s currency preference | 
**lifestyle** | **str** | Control which lifestyle the user used. | [optional] 
**engine_configuration_identifier** | **str** | Affiliate customization | 
**valid_user** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.upsert_shopping_cart_item_request_authenticated_entity import UpsertShoppingCartItemRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertShoppingCartItemRequestAuthenticatedEntity from a JSON string
upsert_shopping_cart_item_request_authenticated_entity_instance = UpsertShoppingCartItemRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpsertShoppingCartItemRequestAuthenticatedEntity.to_json())

# convert the object into a dict
upsert_shopping_cart_item_request_authenticated_entity_dict = upsert_shopping_cart_item_request_authenticated_entity_instance.to_dict()
# create an instance of UpsertShoppingCartItemRequestAuthenticatedEntity from a dict
upsert_shopping_cart_item_request_authenticated_entity_from_dict = UpsertShoppingCartItemRequestAuthenticatedEntity.from_dict(upsert_shopping_cart_item_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


