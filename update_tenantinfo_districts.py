import json

# Load tenants.json to get proper district codes
with open('data/as/tenant/tenants.json', 'r') as f:
    tenants_data = json.load(f)

# Create mapping: tenant code -> district code
tenant_to_district = {}
for tenant in tenants_data['tenants']:
    tenant_code = tenant['code']
    if 'city' in tenant and tenant['city'] and 'districtCode' in tenant['city']:
        district_code = tenant['city']['districtCode']
        tenant_to_district[tenant_code] = district_code

# Load tenantInfo.json
with open('data/as/tenant/tenantInfo.json', 'r') as f:
    tenant_info_data = json.load(f)

# Update district codes in tenantInfo
updated_count = 0
for tenant_info in tenant_info_data['tenantInfo']:
    tenant_code = tenant_info['code']
    
    if tenant_code in tenant_to_district:
        old_district = tenant_info.get('districtCode')
        new_district = tenant_to_district[tenant_code]
        
        if old_district != new_district:
            tenant_info['districtCode'] = new_district
            print(f"Updated {tenant_code}: {old_district} -> {new_district}")
            updated_count += 1

print(f"\nTotal tenantInfo entries updated: {updated_count}")

# Save updated tenantInfo.json
with open('data/as/tenant/tenantInfo.json', 'w') as f:
    json.dump(tenant_info_data, f, indent=2, ensure_ascii=False)

print("TenantInfo district codes updated successfully!")