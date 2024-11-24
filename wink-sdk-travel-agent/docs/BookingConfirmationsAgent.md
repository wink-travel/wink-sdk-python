# BookingConfirmationsAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[BookingViewAgent]**](BookingViewAgent.md) |  | [optional] 
**points_to_be_earned** | **int** |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_confirmations_agent import BookingConfirmationsAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingConfirmationsAgent from a JSON string
booking_confirmations_agent_instance = BookingConfirmationsAgent.from_json(json)
# print the JSON string representation of the object
print(BookingConfirmationsAgent.to_json())

# convert the object into a dict
booking_confirmations_agent_dict = booking_confirmations_agent_instance.to_dict()
# create an instance of BookingConfirmationsAgent from a dict
booking_confirmations_agent_from_dict = BookingConfirmationsAgent.from_dict(booking_confirmations_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


