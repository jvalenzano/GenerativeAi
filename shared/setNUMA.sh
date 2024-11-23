#!/bin/bash

#Reference: https://stackoverflow.com/questions/44232898/memoryerror-in-tensorflow-and-successful-numa-node-read-from-sysfs-had-negativ
#for pcidev in $(lspci -D|grep 'VGA compatible controller: NVIDIA'|sed -e 's/[[:space:]].*//'); 
for pcidev in $(lspci -D|grep 'NVIDIA'|sed -e 's/[[:space:]].*//'); 
do 
  echo "Saving 0 to /sys/bus/pci/devices/${pcidev}/numa_node";
  echo 0 > /sys/bus/pci/devices/${pcidev}/numa_node;
done
