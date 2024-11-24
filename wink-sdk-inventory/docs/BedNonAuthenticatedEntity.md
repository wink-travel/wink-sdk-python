# BedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bed_type_code** | **str** | Indicates the type of bed(s) found in the room. Typical values would be Double, Twin, Queen, or King. Supported OTA specification &#x60;BED&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory). | 
**quantity** | **int** | Number of beds for this bed type. | 

## Example

```python
from wink_sdk_inventory.models.bed_non_authenticated_entity import BedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BedNonAuthenticatedEntity from a JSON string
bed_non_authenticated_entity_instance = BedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BedNonAuthenticatedEntity.to_json())

# convert the object into a dict
bed_non_authenticated_entity_dict = bed_non_authenticated_entity_instance.to_dict()
# create an instance of BedNonAuthenticatedEntity from a dict
bed_non_authenticated_entity_from_dict = BedNonAuthenticatedEntity.from_dict(bed_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


