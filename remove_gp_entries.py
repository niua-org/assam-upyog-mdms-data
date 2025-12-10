#!/usr/bin/env python3
import json

def remove_gp_entries():
    # Read tenants.json
    with open('/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/data/as/tenant/tenants.json', 'r') as f:
        tenants_data = json.load(f)
    
    # Read tenantInfo.json
    with open('/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/data/as/tenant/tenantInfo.json', 'r') as f:
        tenant_info_data = json.load(f)
    
    # Filter out GP entries from tenants.json
    original_tenants_count = len(tenants_data['tenants'])
    tenants_data['tenants'] = [
        tenant for tenant in tenants_data['tenants'] 
        if tenant.get('city', {}).get('ulbGrade') != 'GRAM_PANCHAYAT'
    ]
    new_tenants_count = len(tenants_data['tenants'])
    
    # Get list of GP codes to remove from tenantInfo
    gp_codes = set()
    with open('/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/data/as/tenant/tenants.json', 'r') as f:
        original_tenants_data = json.load(f)
    
    for tenant in original_tenants_data['tenants']:
        if tenant.get('city', {}).get('ulbGrade') == 'GRAM_PANCHAYAT':
            gp_codes.add(tenant['code'])
    
    # Filter out GP entries from tenantInfo.json
    original_tenant_info_count = len(tenant_info_data['tenantInfo'])
    tenant_info_data['tenantInfo'] = [
        info for info in tenant_info_data['tenantInfo'] 
        if info['code'] not in gp_codes
    ]
    new_tenant_info_count = len(tenant_info_data['tenantInfo'])
    
    # Write back the filtered data
    with open('/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/data/as/tenant/tenants.json', 'w') as f:
        json.dump(tenants_data, f, indent=2)
    
    with open('/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/data/as/tenant/tenantInfo.json', 'w') as f:
        json.dump(tenant_info_data, f, indent=2)
    
    print(f"Removed {original_tenants_count - new_tenants_count} GP entries from tenants.json")
    print(f"Removed {original_tenant_info_count - new_tenant_info_count} GP entries from tenantInfo.json")
    print(f"Remaining tenants: {new_tenants_count}")
    print(f"Remaining tenant info: {new_tenant_info_count}")

if __name__ == "__main__":
    remove_gp_entries()