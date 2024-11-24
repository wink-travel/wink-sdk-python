# BedAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bed_type_code** | **str** | Indicates the type of bed(s) found in the room. Typical values would be Double, Twin, Queen, or King. Supported OTA specification &#x60;BED&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory). | 
**quantity** | **int** | Number of beds for this bed type. | 

## Example

```python
from wink_sdk_travel_agent.models.bed_agent import BedAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BedAgent from a JSON string
bed_agent_instance = BedAgent.from_json(json)
# print the JSON string representation of the object
print(BedAgent.to_json())

# convert the object into a dict
bed_agent_dict = bed_agent_instance.to_dict()
# create an instance of BedAgent from a dict
bed_agent_from_dict = BedAgent.from_dict(bed_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


