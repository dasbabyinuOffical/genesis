# genesis

## 安装依赖包
```shell
yum install python3-devel
pip3 install virtualenv
virtualenv genesis
source genesis/bin/activate
pip3 install uwsgi flask 
pip3 install flask-cors
```

## 修改nginx配置　
```shell
vim /etc/nginx/nginx.conf
location ^~ /nft/ {
	  include uwsgi_params;
	  uwsgi_pass unix:/root/work/nft/genesis/genesis.sock;
	}
 ```
 
 ## 设置开机启动
 ```shell
 cp genesis.service /etc/systemd/system/genesis.service
 systemctl enable genesis
 systemctl start genesis
 ```
