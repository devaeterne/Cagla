import pandas as pd

def increment_segments(input_value, max_increment=8):
    print(f"Processing: {input_value}")  # İşlem sırasında hangi değerin işlendiğini yazdır
    segments = input_value.split('/')
    incremented_segments = [segments[0]]  # İlk segmenti olduğu gibi bırak

    for i in range(1, len(segments)):
        segment_parts = segments[i].split('/')
        
        # Artırma işlemi
        incremented_parts = []
        for part in segment_parts:
            try:
                incremented_part = str(int(part) + 1)
                incremented_parts.append(incremented_part)
            except ValueError:
                print(f"Could not convert part to int: {part}")  # Eğer dönüştürme başarısız olursa yazdır
                
        new_segment = '/'.join(incremented_parts)
        print(f"Incremented segment: {new_segment}")  # Yeni segmenti yazdır
        incremented_segments.append(new_segment)
        
    result = '/'.join(incremented_segments)
    print(f"Resulting value: {result}")  # Sonucu yazdır
    return result

input_file = '/Users/devaeterne/Projects/Cagla/data/Book3.xlsx'
output_file = '/Users/devaeterne/Projects/Cagla/data/Book3_out.xlsx'

try:
    # Doğru satırdan sütun adlarını oku
    df = pd.read_excel(input_file, header=0)  # header=0, ilk satırı sütun adı olarak alır
    print("Original DataFrame:")
    print(df.head())
    
    # 'input' sütununun mevcut olduğunu kontrol et
    if 'input' not in df.columns:
        raise KeyError(f"'input' column not found in the Excel file. Available columns: {df.columns.tolist()}")
    
    # 'input' sütununu işle
    df['input'] = df['input'].apply(increment_segments)
    print("Processed DataFrame:")
    print(df.head())
    
    # Yeni Excel dosyasına kaydet
    df.to_excel(output_file, index=False)
    print(f"Dataset successfully processed and saved to {output_file}.")
except FileNotFoundError:
    print(f"File not found: {input_file}")
except KeyError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
