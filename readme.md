# Rock, Paper, Scissors Game

## Hakkında
Bu proje, klasik "Rock, Paper, Scissors" oyununu Python ile komut satırında oynanabilir hale getirir. Kullanıcı, "Rock", "Paper" veya "Scissors" seçeneklerinden birini seçer ve bilgisayarın rastgele yaptığı seçimle karşılaştırılır. İlk olarak 2 puana ulaşan taraf oyunu kazanır.

## Özellikler
- Kullanıcı ile bilgisayar arasında oynanan bir oyun
- Kullanıcının oyunu bitirmesini sağlayan `exit` seçeneği
- Puan takibi ve oyun sonu değerlendirmesi
- Tekrar oynama seçeneği

## Kullanılan Teknolojiler
- **Python**: Oyun mantığını ve kullanıcı etkileşimini sağlamak için kullanıldı.
- **Random Module**: Bilgisayarın rastgele bir seçim yapmasını sağlamak için kullanıldı.

## Mimari
Proje, temel bir Python betiği olarak tasarlanmıştır. Ana bileşenler şunlardır:
- `play_round()`: Bir oyunun roundunu yöneten fonksiyon.
- `play_game()`: Oyunun akışını ve puanlamayı yöneten fonksiyon.
- `main()`: Oyunu başlatan ve tekrar oynama seçeneklerini kontrol eden ana fonksiyon.

## Proje Nasıl Ayağa Kaldırılır
1. Python 3.x'in yüklü olduğundan emin olun.
2. Proje dosyasını indirin veya klonlayın.
3. Komut satırında, proje dizinine gidin.
4. Aşağıdaki komutu çalıştırarak oyunu başlatın:

   ```bash
   python <dosya_adı>.py
