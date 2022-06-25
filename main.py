import os
import json


def choices():
    print('#' * 25)
    print('Seçim yapınız.')
    print('1 -> Çıkış Yap. 2 -> Tekrar çalıştır.')
    choice = input()
    if choice == '1':
        print('#' * 25)
        exit('Bye bye :)')
    elif choice == '2':
        count_label()
    else:
        print('#' * 25)
        exit('Bilemedin. :)') 
        
           
def count_label():
    print('#' * 25)
    print('Lütfen dizin yolu giriniz :) :P')
    label_path = input()
    if os.path.exists(label_path):
        print('#' * 25)
        print('Lütfen bekleyiniz... Sayıyorum...')
        # .json dosya uzantılı dosyaların adlarını bir listeye attık
        file_json_list = [
            file for file in os.listdir(label_path) if (file.lower().endswith('.json'))
        ]
        tag_dict = {}
        for file_name in file_json_list:
            with open(f'{label_path}/{file_name}', 'r') as f:
                json_dict = json.load(f)
                for label_obj in json_dict.get('shapes', []):
                    try:
                        tag_dict[label_obj['label']] += 1
                    except KeyError:
                        tag_dict[label_obj['label']] = 1
        if tag_dict:
            print('#' * 25)
            print('Aha da saydım. :)')
            print(tag_dict)
            print()
            print()
        else:
            print('#' * 25)
            print('Elde var SIFIR :)')
            print()
            print()
        choices()
    else:
        print('#' * 25)
        print('Böyle bir dizin yok :( :/')
        count_label()
        
if __name__ =='__main__':
    count_label()
