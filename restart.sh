#!/bin/sh

rm /etc/netplan/static.yaml
rm /etc/dhcp/dhcpd.conf
cp dhcpd.conf /etc/dhcp
cp static.yaml /etc/netplan/
sudo netplan apply
