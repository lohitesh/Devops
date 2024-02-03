import pandas as pd

def excel_to_json(excel_file_path, json_file_path):
    try:
        df = pd.read_excel(excel_file_path, sheet_name='Sheet1')#.drop(columns=' ')
        // The applymap method is used to apply the provided lambda function to each element in the DataFrame. The lambda function checks if an element is a string and then applies the strip method to remove leading and trailing whitespaces.
        df_stripped = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        //The orient='records' parameter in the to_json method specifies the format in which the JSON data will be structured. When orient is set to 'records', each row in the DataFrame becomes a JSON record (dictionary), and the resulting JSON file is an array of dictionaries.
        df_stripped.to_json(json_file_path, orient='records', indent=2)
        print("Excel file converted to JSON successfully!")
    except Exception as e:
        print(f"Error: {e}")


excel_file_path = "sample.xlsx"
json_file_path = "manifest_new.json"
excel_to_json(excel_file_path, json_file_path)
