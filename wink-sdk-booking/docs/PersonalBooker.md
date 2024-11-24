# PersonalBooker

Detailed customer information for this profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **str** | Identifier the gender of the customer. | [optional] 
**birth_date** | **date** | Indicates the date of birth as indicated in the document, in ISO 8601 prescribed format. | [optional] 
**marital_status** | **str** | Marital status of the traveler. | [optional] 
**child_quantity** | **int** | The number of children of the customer. | [optional] 
**citizenship** | **str** | Name of the (self-professed) country that is clamided for citizenship. | [optional] 
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal code | [optional] 
**country** | **str** | Country | [optional] 
**preferred_currency** | **str** | Type of funds preferred for reviewing monetary values, in ISO 4217 codes | [optional] 
**language** | **str** | The primary language of the customer | [optional] 
**contact_person** | [**List[ContactBooker]**](ContactBooker.md) |  | [optional] 
**phys_chall_name** | **List[str]** |  | [optional] 
**pet_info** | [**List[PetInfoDtoBooker]**](PetInfoDtoBooker.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.personal_booker import PersonalBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalBooker from a JSON string
personal_booker_instance = PersonalBooker.from_json(json)
# print the JSON string representation of the object
print(PersonalBooker.to_json())

# convert the object into a dict
personal_booker_dict = personal_booker_instance.to_dict()
# create an instance of PersonalBooker from a dict
personal_booker_from_dict = PersonalBooker.from_dict(personal_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


