# RatePlanLevelFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescription]**](LocalizedDescription.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_extranet_monetize.models.rate_plan_level_fee import RatePlanLevelFee

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFee from a JSON string
rate_plan_level_fee_instance = RatePlanLevelFee.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFee.to_json())

# convert the object into a dict
rate_plan_level_fee_dict = rate_plan_level_fee_instance.to_dict()
# create an instance of RatePlanLevelFee from a dict
rate_plan_level_fee_from_dict = RatePlanLevelFee.from_dict(rate_plan_level_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


