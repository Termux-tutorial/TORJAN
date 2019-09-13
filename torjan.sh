clear
figlet TORJAN |lolcat
echo "\33[0;36m============================================"
echo "=     \33[31;1mSCURITY TORJAN CYBER INDONESIAN      ="
echo "=       \33[31;1m            TORJAN                 ="
echo "=     \33[31;1m         Author : TUTORIAL TERMUX            ="
echo "\33[0;36m============================================"
echo "\33[0;36m                @@@@@@@@@@@@@@@          @@"
echo "\33[0;36m                @1234567891011@ ========@  @"
echo "\33[0;36m                @@@@@@@@@@@@@@@          @@"
echo
echo "\33[33;1mKetik 8 Untuk Melanjutkan Torjan"
echo "\33[33;1mKetik 5 Untuk Keluar"
read -p "Masukan Pilihan Anda :" tutorial

case $tutorial in
8)
clear
python2 torjancyber.py
;;
5)
echo "Keluar"
;;
*)
echo "Pilihan Anda Salah"
sleep 5
sh torjan.sh
;;
esac
