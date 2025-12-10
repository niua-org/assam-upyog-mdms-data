import json

# Load the district mapping
with open('proper_district_gp_mapping.json', 'r') as f:
    district_mapping = json.load(f)

# Create reverse mapping: GP -> District
gp_to_district = {}
for district, gps in district_mapping.items():
    for gp in gps:
        gp_to_district[gp.lower().replace(' ', '').replace('-', '')] = district

# Load current tenants.json
with open('data/as/tenant/tenants.json', 'r') as f:
    tenants_data = json.load(f)

# Update district names
updated_count = 0
for tenant in tenants_data['tenants']:
    if 'city' in tenant and tenant['city']:
        city_name = tenant['city']['name']
        # Normalize city name for matching
        normalized_name = city_name.lower().replace(' ', '').replace('-', '')
        
        if normalized_name in gp_to_district:
            district = gp_to_district[normalized_name]
            tenant['city']['districtName'] = district
            print(f"Updated {city_name} -> District: {district}")
            updated_count += 1
        else:
            print(f"No district found for: {city_name}")

print(f"\nTotal updated: {updated_count}")

# Save updated file
with open('data/as/tenant/tenants_updated.json', 'w') as f:
    json.dump(tenants_data, f, indent=2, ensure_ascii=False)

print("Updated file saved as tenants_updated.json")