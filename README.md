# FlexClient Valorant

Bu repo, Valorant açıkken sol üstte görünen basit bir profil avatarı overlay'i içerir.

- Sağ tık veya `Esc`: kapatır.
- Avatar sürüklenebilir.
- Valorant ön planda değilken gizlenir.
- Oyun dosyalarına, belleğine veya oynanışına müdahale etmez.

## EXE üretme

GitHub Actions içindeki **Build FlexClient EXE** workflow'u her `main` push'unda veya manuel çalıştırmada Windows runner üzerinde `FlexClient.exe` üretir.

1. GitHub'da **Actions** sekmesini aç.
2. **Build FlexClient EXE** workflow'unu seç.
3. **Run workflow** ile manuel başlatabilir veya `main` branch'ine push bekleyebilirsin.
4. Tamamlanınca run sayfasındaki **Artifacts** bölümünden `FlexClient-windows` dosyasını indir.

## Yerel test

```bash
python app.py
```
