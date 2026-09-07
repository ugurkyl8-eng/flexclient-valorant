# FlexClient Valorant

Windows için hazırlanmış, Mix 1 / Mix 2 / Mix 3 seçeneklerini içeren basit bir masaüstü menüsü.

> Bu proje yerel bir arayüzdür; oyun dosyalarına, belleğine veya Valorant sürecine müdahale etmez.

## Yerelde çalıştırma

Python 3.10+ ile:

```bash
python app.py
```

## GitHub Actions ile `.exe` üretme

1. `main` branch'ine push yap.
2. GitHub'da **Actions** sekmesine gir.
3. **Build Windows EXE** workflow çalışmasını aç.
4. Tamamlandığında **Artifacts** bölümünden `FlexClient-windows` dosyasını indir.

Workflow, `FlexClient.exe` dosyasını Windows runner üzerinde PyInstaller ile üretir.
