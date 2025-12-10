import json

# District to tenant code mapping
district_tenant_mapping = {
    "DHEMAJI": "as.dhemajimb",
    "NALBARI": "as.nalbarimb", 
    "DIBRUGARH": "as.dibrugarh",
    "TINSUKIA": "as.tinsukiamb",
    "JORHAT": "as.jorhatmb",
    "SONITPUR": "as.tezpurmb",
    "BISWANATH": "as.biswanathcharialimb",
    "NORTH_LAKHIMPUR": "as.northlakhimpurmb",
    "BOMGAIGAON": "as.bongaigaon",
    "DHUBRI": "as.dhubri",
    "GOALPARA": "as.goalparamb"
}

# Load current tenants.json
with open('data/as/tenant/tenants.json', 'r') as f:
    tenants_data = json.load(f)

# Update district tenant codes
updated_count = 0
for tenant in tenants_data['tenants']:
    if 'city' in tenant and tenant['city']:
        district_code = tenant['city'].get('districtCode')
        
        if district_code in district_tenant_mapping:
            old_code = tenant['city'].get('districtTenantCode')
            new_code = district_tenant_mapping[district_code]
            tenant['city']['districtTenantCode'] = new_code
            print(f"Updated {tenant['city']['name']}: {old_code} -> {new_code}")
            updated_count += 1

print(f"\nTotal district tenant codes updated: {updated_count}")

# Save updated file
with open('data/as/tenant/tenants.json', 'w') as f:
    json.dump(tenants_data, f, indent=2, ensure_ascii=False)

print("District tenant codes updated successfully!")