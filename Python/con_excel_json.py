import pandas as pd

def excel_to_json(excel_file_path, json_file_path):
    try:
        df = pd.read_excel(excel_file_path, sheet_name='Sheet1')#.drop(columns=' ')
        df_stripped = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        df_stripped.to_json(json_file_path, orient='records', indent=2)
        print("Excel file converted to JSON successfully!")
    except Exception as e:
        print(f"Error: {e}")


excel_file_path = "sample.xlsx"
json_file_path = "manifest_new.json"
excel_to_json(excel_file_path, json_file_path)
