import pandas as pd
import json

def extract_district_gp_mapping(excel_path):
    """Extract district and gram panchayat mapping from Excel file"""
    
    # Read Excel file
    df = pd.read_excel(excel_path)
    
    # Extract districts (Column A) and gram panchayats (Column J)
    # Assuming first row might be header, so we'll handle it
    districts = df.iloc[:, 0].dropna()  # Column A (index 0)
    gram_panchayats = df.iloc[:, 9].dropna()  # Column J (index 9)
    
    print("Districts found:")
    print(districts.head(10))
    print(f"\nTotal districts: {len(districts)}")
    
    print("\nGram Panchayats found:")
    print(gram_panchayats.head(10))
    print(f"Total gram panchayats: {len(gram_panchayats)}")
    
    # Create mapping dictionary
    mapping = {}
    min_length = min(len(districts), len(gram_panchayats))
    
    for i in range(min_length):
        district = str(districts.iloc[i]).strip()
        gp = str(gram_panchayats.iloc[i]).strip()
        
        if district != 'nan' and gp != 'nan':
            if district not in mapping:
                mapping[district] = []
            if gp not in mapping[district]:
                mapping[district].append(gp)
    
    return mapping

def save_mapping_to_json(mapping, output_path):
    """Save mapping to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    excel_file = "/Users/atul/Downloads/corrected Final 21 DA Area Mapping Planning Sheet_Assam.xlsx"
    output_file = "/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/district_gp_mapping.json"
    
    try:
        print("Reading Excel file...")
        mapping = extract_district_gp_mapping(excel_file)
        
        print(f"\nMapping created with {len(mapping)} districts")
        for district, gps in list(mapping.items())[:5]:  # Show first 5
            print(f"{district}: {len(gps)} gram panchayats")
        
        print(f"\nSaving mapping to {output_file}")
        save_mapping_to_json(mapping, output_file)
        print("Done!")
        
    except Exception as e:
        print(f"Error: {e}")