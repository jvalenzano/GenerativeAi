#!/bin/bash

#Reference: https://stackoverflow.com/questions/44232898/memoryerror-in-tensorflow-and-successful-numa-node-read-from-sysfs-had-negativ
for pcidev in $(lspci -D|grep 'VGA compatible controller: NVIDIA'|sed -e 's/[[:space:]].*//'); 
do 
  echo 0 > /sys/bus/pci/devices/${pcidev}/numa_node;
done
