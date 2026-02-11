# Zrozumienie Factory Reset Protection (FRP)

## Czym jest FRP?

Factory Reset Protection to zabezpieczenie wprowadzone przez Google w Androidzie 5.1. Po przywróceniu ustawień fabrycznych wymaga podania danych konta Google powiązanego z urządzeniem.

## Jak działa FRP?

1. Użytkownik loguje się na konto Google.
2. Po wykonaniu resetu system żąda tych samych danych logowania.
3. Bez nich urządzenie pozostaje zablokowane.

## Dlaczego omijać FRP?

- **Legalne odzyskiwanie dostępu** do własnych urządzeń.
- **Edukacja i analiza** mechanizmów bezpieczeństwa Androida.

## Techniki bypassu

- **Samsung**: tryb testowy `*#0*#`, instalacja APK z poziomu przeglądarki, TWRP.
- **Xiaomi**: tryb recovery, wyłączenie konta MI, tryb EDL.
- **Huawei**: komendy fastboot, exploity HiSuite.
- **Oppo**: tryb EDL, flashowanie przez QFIL.

## Nowe wersje Androida (12-15)

- **Android 12**: ograniczenia w kreatorze konfiguracji.
- **Android 13**: blokada pakietów systemowych.
- **Android 14**: dynamiczne partycje i ograniczenia ADB.
- **Android 15**: wzmocniona ochrona partycji FRP.

## Ryzyka

- Możliwa utrata danych lub uszkodzenie urządzenia.
- Konsekwencje prawne przy użyciu na cudzym sprzęcie.

## Podstawowe komendy

```bash
adb devices
adb shell pm install /path/to/frp_bypass.apk
adb reboot
fastboot devices
fastboot erase frp
fastboot reboot
fastboot flash recovery twrp.img
```
