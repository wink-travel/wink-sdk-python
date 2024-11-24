# UpsertRecognitionSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of rating system the recognition operated on. This allows us to display the score properly. | 
**category** | **str** | Recognition category. | 
**provider** | **str** | The name of the entity that administers this recognition. | 
**rating** | **float** | The actual award or rating received by the hotel facility. | 
**max_rating** | **float** | Use this to let hotels indicate what the total score for this award is. | [optional] 
**var_date** | **date** | The date the award was received | [optional] 
**official_appointment_ind** | **bool** | When true, this indicates the property has received official permission from the award provider to use the rating in publications and marketing materials; when false this permission has not been granted. | [optional] 
**rating_symbol** | **str** | Provides the symbol used in the rating. Used in conjunction with the Rating. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.upsert_recognition_supplier import UpsertRecognitionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertRecognitionSupplier from a JSON string
upsert_recognition_supplier_instance = UpsertRecognitionSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertRecognitionSupplier.to_json())

# convert the object into a dict
upsert_recognition_supplier_dict = upsert_recognition_supplier_instance.to_dict()
# create an instance of UpsertRecognitionSupplier from a dict
upsert_recognition_supplier_from_dict = UpsertRecognitionSupplier.from_dict(upsert_recognition_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


