# A systemd no-ip client

[No-ip](https://www.noip.com/) is a popular DDNS service.

This python client connects no-ip's servers repeatedly, using a systemd service

1. Edit ```noip.py```
2. As root, copy it into ```/usr/sbin/noip.py``` and do it ```chmod a+x```
3. As root, copy ```noip.service``` into ```etc/systemd/system/noip.service``` (edit there also the connection interval to no-ip's servers)
4. Enable & start:
```
sudo systemctl --user enable noip.service 
sudo systemctl --user start noip.service
```
5. Stop & disable
```
sudo systemctl --user stop noip.service
sudo systemctl --user disable noip.service
```
6. See status
```
sudo systemctl status pusher.service
sudo journalctl -q --unit noip.service -f
```

## Authors
Sampsa Riikonen

## Copyright
(C) 2019 Sampsa Riikonen

## License
MIT
