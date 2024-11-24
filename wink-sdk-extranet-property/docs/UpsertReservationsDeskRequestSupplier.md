# UpsertReservationsDeskRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations_contact** | [**ContactSupplier**](ContactSupplier.md) |  | 
**reservation_desk_start_time** | **str** | If the reservation desk does not operate 24 hours, enter a start time. | 
**reservation_desk_end_time** | **str** | If the reservation desk does not operate 24 hours, enter an end time. | 

## Example

```python
from wink_sdk_extranet_property.models.upsert_reservations_desk_request_supplier import UpsertReservationsDeskRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReservationsDeskRequestSupplier from a JSON string
upsert_reservations_desk_request_supplier_instance = UpsertReservationsDeskRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertReservationsDeskRequestSupplier.to_json())

# convert the object into a dict
upsert_reservations_desk_request_supplier_dict = upsert_reservations_desk_request_supplier_instance.to_dict()
# create an instance of UpsertReservationsDeskRequestSupplier from a dict
upsert_reservations_desk_request_supplier_from_dict = UpsertReservationsDeskRequestSupplier.from_dict(upsert_reservations_desk_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


