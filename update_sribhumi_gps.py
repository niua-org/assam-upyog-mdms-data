import json

# List of Sribhumi/Karimganj GPs
sribhumi_gps = [
    "Nayabari Kesharkapon", "Sarisha Charakuri", "Longaighat", "Bakharshal-Nairgram",
    "North Karimganj", "Krishna Nagar", "Medal Sarifnagar", "Sadarahi", 
    "Kanishail- Sarifnagar", "Akborpur", "Nortth Karimganj", "Sadarashi",
    "Pirerchak", "Kanishail-Sarifnagar", "Longaighat -Bazarghat", "Prasarpur",
    "Maijgram", "Bakharshail- Nairgram", "Latu Sajpur", "Bakharsal Nairgram",
    "Kanishail Patel Nagar", "Sarisha- Charakuri", "Maizgram", "Karimganj GP"
]

# Load current tenants.json
with open('data/as/tenant/tenants.json', 'r') as f:
    tenants_data = json.load(f)

# Update Sribhumi GPs
updated_count = 0
for tenant in tenants_data['tenants']:
    if 'city' in tenant and tenant['city']:
        city_name = tenant['city']['name']
        
        # Check if this GP is in Sribhumi list
        if city_name in sribhumi_gps:
            tenant['city']['districtName'] = "Sribhumi"
            tenant['city']['districtCode'] = "SRIBHUMI"
            tenant['city']['districtTenantCode'] = "as.sribhumimb"
            print(f"Updated {city_name} -> Sribhumi district")
            updated_count += 1

print(f"\nTotal Sribhumi GPs updated: {updated_count}")

# Save updated file
with open('data/as/tenant/tenants.json', 'w') as f:
    json.dump(tenants_data, f, indent=2, ensure_ascii=False)

print("Sribhumi GPs updated successfully!")