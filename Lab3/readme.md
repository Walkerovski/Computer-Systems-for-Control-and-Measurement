# [SKPS] - Laboratorium 3

Cel laboratorium:
1. [x] Zapoznanie z SDK OpenWRT
2. [x] Zbudowanie własnych pakietów
3. [x] Debugowanie pakietu

## Pierwszy pakiet

Pobrano i rozpakowano SDK OpenWRT, oraz przygotowany pakiet demonstracyjny.

Dodano ścieżkę do pakietów demonstracyjnych w pliku `feeds.conf.default`:
```
src-link skps /home/user/Documents/SKPS/demo1_owrt_pkg
```

Zakutalizowano listy pakietów:
```
LANG=C ./scripts/feeds update -a
LANG=C ./scripts/feeds install -p skps -a
LANG=C ./scripts/feeds install -p packages -a
```

Włączono pakiety demonstracyne w `make menuconfig`, a następnie zbudowano je: `make package/demo1/compile`, `make package/demo1mak/compile`.

Przeniesiono pliki zbudowane pliki .ipk na RPi i zainstalowano je za pomocą `opkg install demo1_1.0-1_aarch64_cortex-a72.ipk`
i `opkg install demo1mak_1_aarch64_cortex-a72.ipk`.

## Pakiety "worms" i "buggy"

W repozytorium znajdują się Makefile pakietów _worms_ i _buggy_ gotowe do wykorzystania w OpenWRT.
Aby ułatwić pracę, katalogi te umioszczono w tym samym katalogu co pakiety `demo1` i `demo1mak`.

Zaktualizowano listy pakietów (`LANG=C ./scripts/feeds update -a`, `LANG=C ./scripts/feeds install -p skps -a`); a następnie zbudowano pakiety:
`make package/buggy/compile` i `make package/worms/compile`.

Pliki ipk przeniesiono na RPi i zainstalowano za pomocą opkg.

## Debugowanie zdalne

Uruchomiono debugowanie programu `bug3` na RPi za pomocą polecenia `gdbserver :9000 /usr/bin/bug3`.
Następnie połączono się z hosta do serwera gdb za pomocą skryptu w SDK: `./scripts/remote-gdb 10.42.0.196:9000 ./build_dir/target-aarch64_cortex-a72_musl/buggy-1.0/bug3`.

Aby poprawnie zadziałało wyświetlanie kodu źródłowego dodano odpowiedni katalog za pomocą polecenia GDB: `directory /home/user/Pulpit/WZ_W3_przyklady/demo1_owrt_pkg/buggy/src`.

Wykonano następujące polecenia:
- ustawianie breapointu: `break main`
    ```
    (gdb) break main
    Breakpoint 1 at 0x4004b0: file buggy-1.0/bug3.c, line 12.
    (gdb) run
    The program being debugged has been started already.
    Start it from the beginning? (y or n) y
    Starting program: /home/user/Documents/openwrt_sdk/build_dir/target-aarch64_cortex-a72_musl/buggy-1.0/bug3

    Breakpoint 1, main () at buggy-1.0/bug3.c:12
    (gdb)
    ```
- pracę krokową: `next`
    ```
    12	in buggy-1.0/bug3.c
    (gdb) n
    13	in buggy-1.0/bug3.c
    (gdb) n
    12	in buggy-1.0/bug3.c
    ```
- podgląd wartości zmiennej: `print/display i`
    ```
    (gdb) print i
    $2 = 2
    (gdb) display i
    1: i = 2
    (gdb) n
    12	  for(i=0;i<24;i++) {
    1: i = 3
    (gdb) n
    13	    s1[i]=i+64;
    1: i = 3
    (gdb) n
    12	  for(i=0;i<24;i++) {
    1: i = 4
    (gdb)
    ```
- podgląd stosu: `x/20x $sp`
    ```
    (gdb) x/20x $sp
    0x7ffffffd60:	0xfffffd70	0x0000007f	0xf7f93190	0x0000007f
    0x7ffffffd70:	0x00000000	0x00000000	0x00000000	0x00000000
    0x7ffffffd80:	0xfffffda0	0x0000007f	0xf7ffdca8	0x0000007f
    0x7ffffffd90:	0xf7ffde50	0x0000007f	0xf7ffde50	0x0000007f
    0x7ffffffda0:	0x00000002	0x00000000	0xffffff70	0x0000007f
    ```
- backtrace: `bt`
    ```
    (gdb) bt
    #0  main () at buggy-1.0/bug3.c:12
    ```
- wykorzystanie watchpointów: `watch s1[9]`
    ```
    (gdb) watch s1[9]
    Watchpoint 3: s1[9]
    (gdb) c
    Continuing.

    Watchpoint 3: s1[9]

    Old value = 0 '\000'
    New value = 73 'I'
    main () at buggy-1.0/bug3.c:12
    (gdb) 
    ```

Znalezione błędy:
- bug1: Tablica `table` nigdy nie jest alokowana
- bug2: Próba dostania się poza tablicę
- bug3: Nadpisanie kończącego NULLa w ciągu znaków

