import pandas as pd

# Excel dosyasını oku
excel_file = 'data/book3.xlsx'  # Excel dosyanızın adını buraya yazın

# Excel dosyasını oku (ilk sayfa varsayılan olarak alınır)
df = pd.read_excel(excel_file)

# Yeni bir sütun ekle
df['OUTPUT'] = ''  # Yeni sütunu boş olarak ekle

# DataFrame'deki tüm hücreleri kontrol et
for row_index in range(df.shape[0]):  # Satır sayısı
    input_value = df.iat[row_index, 1]  # 'INPUT' sütunundaki değeri al (indeks 1)

    # '-' ile parçala
    parts = input_value.split('-')  # '-' ile ayır
    valid_values = set()  # Geçerli değerleri tutmak için bir set

    for part in parts:
        if '/' in part:
            # '/' ile parçala
            sub_parts = part.split('/')  # '/' ile ayır
            
            # İlk kısım (4 haneli kontrolü)
            previous_part = sub_parts[0].strip()  # İlk kısım
            if previous_part.isdigit() and len(previous_part) == 4:  # 4 haneli kontrolü
                valid_values.add(previous_part)  # 4 haneli değeri ekle
                
                # Son kısımdaki tek haneli değeri al
                for i in range(1, len(sub_parts)):
                    current_part = sub_parts[i].strip()
                    if current_part.isdigit() and len(current_part) == 1:  # Tek haneli kontrolü
                        # Son rakamı değiştir
                        new_value = previous_part[:-1] + current_part  # Önceki sayının sonunu değiştir
                        valid_values.add(new_value)  # Yeni sayıyı ekle
                        previous_part = new_value  # Önceki kısmı güncelle
                    else:
                        # Eğer çok haneli bir sayı varsa, doğrudan ekle
                        valid_values.add(current_part)

        else:
            # Eğer '/' yoksa doğrudan parçayı ekle
            valid_values.add(part.strip())

    # Geçerli değerleri sıralayıp yeni sütuna yaz
    result_values = sorted(valid_values, key=int)  # Sayısal olarak sıralayıp birleştir
    df.at[row_index, 'OUTPUT'] = '\t'.join(result_values)  # Sonucu birleştir

# Güncellenmiş DataFrame'i yeni bir Excel dosyasına yaz
output_file = 'data/updated_book3.xlsx'  # Güncellenmiş dosya adı
df.to_excel(output_file, index=False)

print("Veriler güncellendi ve yeni dosyaya kaydedildi.")
