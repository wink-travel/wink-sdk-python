# UpsertIndividualRateRequestSupplier

Values to update this rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** |  | [optional] 
**delta_quantity** | **int** |  | [optional] 
**master** | **bool** |  | [optional] 
**closed_on_arrival** | **bool** |  | [optional] 
**closed_on_departure** | **bool** |  | [optional] 
**min_length_of_stay** | **int** |  | [optional] 
**max_length_of_stay** | **int** |  | [optional] 
**rate** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**extra_pax_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**single_occupancy_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.upsert_individual_rate_request_supplier import UpsertIndividualRateRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertIndividualRateRequestSupplier from a JSON string
upsert_individual_rate_request_supplier_instance = UpsertIndividualRateRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertIndividualRateRequestSupplier.to_json())

# convert the object into a dict
upsert_individual_rate_request_supplier_dict = upsert_individual_rate_request_supplier_instance.to_dict()
# create an instance of UpsertIndividualRateRequestSupplier from a dict
upsert_individual_rate_request_supplier_from_dict = UpsertIndividualRateRequestSupplier.from_dict(upsert_individual_rate_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


