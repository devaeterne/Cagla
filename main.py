import pandas as pd

def increment_segments(input_value, max_increment=8):
    segments = input_value.split('/')
    incremented_segments = [segments[0]]  # İlk segmenti olduğu gibi bırak

    for i in range(1, len(segments)):
        increment = min(i, max_increment)
        new_segment = f"{segments[i]}{increment}"
        incremented_segments.append(new_segment)
        
    return '/'.join(incremented_segments)

input_file = '/Users/devaeterne/Projects/Cagla/data/Book3.xlsx'
output_file = '/Users/devaeterne/Projects/Cagla/data/Book3_out.xlsx'

try:
    # Doğru satırdan sütun adlarını oku
    df = pd.read_excel(input_file, header=0)  # header=0, ilk satırı sütun adı olarak alır
    
    # 'input' sütununun mevcut olduğunu kontrol et
    if 'input' not in df.columns:
        raise KeyError(f"'input' column not found in the Excel file. Available columns: {df.columns.tolist()}")
    
    # 'input' sütununu işle
    df['input'] = df['input'].apply(increment_segments)
    
    # Yeni Excel dosyasına kaydet
    df.to_excel(output_file, index=False)
    
    print("Dataset successfully processed and saved.")
except FileNotFoundError:
    print(f"File not found: {input_file}")
except KeyError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
