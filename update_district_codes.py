import json

# Load the district mapping
with open('proper_district_gp_mapping.json', 'r') as f:
    district_mapping = json.load(f)

# Create reverse mapping: GP -> District
gp_to_district = {}
for district, gps in district_mapping.items():
    for gp in gps:
        gp_to_district[gp.lower().replace(' ', '').replace('-', '')] = district.upper().replace(' ', '_')

# Load current tenants.json
with open('data/as/tenant/tenants.json', 'r') as f:
    tenants_data = json.load(f)

# Update district codes
updated_count = 0
for tenant in tenants_data['tenants']:
    if 'city' in tenant and tenant['city']:
        city_name = tenant['city']['name']
        # Normalize city name for matching
        normalized_name = city_name.lower().replace(' ', '').replace('-', '')
        
        if normalized_name in gp_to_district:
            district_code = gp_to_district[normalized_name]
            tenant['city']['districtCode'] = district_code
            print(f"Updated {city_name} -> District Code: {district_code}")
            updated_count += 1

print(f"\nTotal district codes updated: {updated_count}")

# Save updated file
with open('data/as/tenant/tenants.json', 'w') as f:
    json.dump(tenants_data, f, indent=2, ensure_ascii=False)

print("District codes updated successfully!")