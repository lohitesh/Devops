[kvmhost:vars] nixcraft_vlan_lan_subnet=10.8.0.0/24
nixcraft_http_port=10.8.0.1:3128
nixcraft_cloud_server_ip=72.xxx.yyy.zzz
nixcraft_memory=1024

use in jinja file as {{ nixcraft_vlan_lan_subnet }} to access the values
