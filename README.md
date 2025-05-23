# Flarion Music Bot



## Özellikler
- YouTube ve SoundCloud'dan şarkı çalma
- Şarkıları duraklatma, devam ettirme ve atlama
- YouTube ve SoundCloud'da şarkı arama
- Çalma listesine şarkı ekleme
- Çalma listelerini oynatma
- Şarkıları ve çalma listelerini döngüye alma

## Komutlar
- `play <şarkı adı/url>` bir şarkı çalmak için
- `pause` mevcut şarkıyı duraklatmak için
- `resume` mevcut şarkıya devam etmek için
- `skip` mevcut şarkıyı atlamak için
- `loop` mevcut şarkıyı veya çalma listesini döngüye almak için
- `leave` ses kanalından ayrılmak için
- `clear` mevcut sırayı temizlemek için
- `queue` mevcut sırayı görüntülemek için
- `nowplaying` mevcut parçayı görüntülemek için
- `node` mevcut düğümü görüntülemek için
- `resume` mevcut şarkıya devam etmek için
- `skip` mevcut şarkıyı atlamak için
- `volume` ses seviyesini değiştirmek için

## Nasıl Yüklenir
- `pip install -r requirements.txt`
- `1 Adet Lavalink Sunucusu`

## Nasıl Kullanılır
- Botu sunucunuza davet edin
- Eğik çizgi komutlar bölümündeki komutları kullanın

## Lisans
MIT Lisansı


## Docker Ortam Değişkenleri

```dockerfile
# Bot yapılandırması
TOKEN=your_discord_bot_token
PREFIX=!
NODE_HOST=lavalink_server_host
NODE_PORT=2333
NODE_PASSWORD=your_lavalink_password
NODE_SECURE=false
```

Bu değişkenleri `.env` dosyasında tanımlayabilir veya Docker çalıştırırken `-e` parametresi ile tanımlayabilirsiniz


## Hazır Paketlenmiş Docker İmajı

https://hub.docker.com/repository/docker/alperdev/flarion-music-bot

