import pandas as pd
import json

def analyze_excel_structure(excel_path):
    """Analyze Excel file structure to understand the data better"""
    
    # Read Excel file
    df = pd.read_excel(excel_path)
    
    print("Excel file columns:")
    for i, col in enumerate(df.columns):
        print(f"Column {chr(65+i)} (index {i}): {col}")
    
    print(f"\nTotal rows: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    
    # Show first 20 rows to understand structure
    print("\nFirst 20 rows:")
    print(df.head(20))
    
    return df

def extract_proper_mapping(df):
    """Extract proper district-GP mapping"""
    
    # Column A is districts (index 0), Column J is gram panchayats (index 9)
    mapping = {}
    current_district = None
    
    for index, row in df.iterrows():
        district_val = row.iloc[0] if pd.notna(row.iloc[0]) else None
        gp_val = row.iloc[9] if pd.notna(row.iloc[9]) else None
        
        # If we find a district name, update current district
        if district_val and str(district_val).strip() != '':
            current_district = str(district_val).strip()
            if current_district not in mapping:
                mapping[current_district] = []
        
        # If we find a gram panchayat and have a current district
        if gp_val and current_district and str(gp_val).strip() != '' and str(gp_val).strip() != 'Gram Panchayat':
            gp_name = str(gp_val).strip()
            if gp_name not in mapping[current_district]:
                mapping[current_district].append(gp_name)
    
    return mapping

if __name__ == "__main__":
    excel_file = "/Users/atul/Downloads/corrected Final 21 DA Area Mapping Planning Sheet_Assam.xlsx"
    
    try:
        print("Analyzing Excel file structure...")
        df = analyze_excel_structure(excel_file)
        
        print("\n" + "="*50)
        print("Extracting proper mapping...")
        mapping = extract_proper_mapping(df)
        
        print(f"\nFound {len(mapping)} districts:")
        for district, gps in mapping.items():
            print(f"{district}: {len(gps)} gram panchayats")
            if len(gps) > 0:
                print(f"  Sample GPs: {gps[:3]}")  # Show first 3 GPs
        
        # Save to JSON
        output_file = "/Users/atul/Documents/mdmdassam/assam-upyog-mdms-data-atul/proper_district_gp_mapping.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)
        
        print(f"\nMapping saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()