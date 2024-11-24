https://www.kernel.org/pub/linux/utils/boot/syslinux/
качаем syslinux-6.03.tar.gz    


https://releases.ubuntu.com/20.04/
качаем 	ubuntu-20.04.6-live-server-amd64.iso
извлекаем  vmlinuz (ядро) и initrd.img (он там initrd, поэтому переименовываем)

(для арм)
https://ubuntu.com/download/server/arm
качаем ubuntu-24.04.1-live-server-arm64.iso
извлекаем  vmlinuz (ядро) и initrd.img (он там initrd, поэтому переименовываем)


далее положить этот iso в html и в pxelinux.cfg/default сменить url 