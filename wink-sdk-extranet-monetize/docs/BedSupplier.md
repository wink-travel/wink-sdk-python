# BedSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bed_type_code** | **str** | Indicates the type of bed(s) found in the room. Typical values would be Double, Twin, Queen, or King. Supported OTA specification &#x60;BED&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory). | 
**quantity** | **int** | Number of beds for this bed type. | 

## Example

```python
from wink_sdk_extranet_monetize.models.bed_supplier import BedSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BedSupplier from a JSON string
bed_supplier_instance = BedSupplier.from_json(json)
# print the JSON string representation of the object
print(BedSupplier.to_json())

# convert the object into a dict
bed_supplier_dict = bed_supplier_instance.to_dict()
# create an instance of BedSupplier from a dict
bed_supplier_from_dict = BedSupplier.from_dict(bed_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


