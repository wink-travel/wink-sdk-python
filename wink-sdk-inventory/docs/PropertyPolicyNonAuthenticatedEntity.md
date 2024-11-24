# PropertyPolicyNonAuthenticatedEntity

Outlines basic policies for the property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children_allowed** | **bool** | Indicates whether property allows children | [default to False]
**children_minimum_age** | **int** | When a property allows children, it can also indicate what the minimum age is for children to be allowed. | [optional] 
**internet_availability** | **str** | Indicates the availability of internet on the property. | 
**internet_connection_type** | **str** | Indicates how guests can access the Internet on the property. | 
**internet_connection_location** | **str** | Indicates where internet is available in and around the property. | 
**parking_availability** | **str** | Indicates whether parking is available at the property. | 
**parking_access** | **str** | Indicates what type of parking is available at the property. | 
**pets_allowed** | **bool** | Indicates whether pets are allowed on the property. Note: There are thousand different kinds of pets. Just because the property allows small dogs does not mean the guest can bring a python. Always best to check with property. | [default to False]
**pet_max_weight_in_kilos** | **int** | If pets are allowed, property can further limit on weight. | [optional] 
**pet_charge** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**check_out_time** | **str** | When the guest has to check out. | 
**check_in_time** | **str** | When the guest can check in. | 

## Example

```python
from wink_sdk_inventory.models.property_policy_non_authenticated_entity import PropertyPolicyNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyPolicyNonAuthenticatedEntity from a JSON string
property_policy_non_authenticated_entity_instance = PropertyPolicyNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PropertyPolicyNonAuthenticatedEntity.to_json())

# convert the object into a dict
property_policy_non_authenticated_entity_dict = property_policy_non_authenticated_entity_instance.to_dict()
# create an instance of PropertyPolicyNonAuthenticatedEntity from a dict
property_policy_non_authenticated_entity_from_dict = PropertyPolicyNonAuthenticatedEntity.from_dict(property_policy_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


