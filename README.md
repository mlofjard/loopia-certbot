### Config:

Edit the following files to suit your needs:  
`loopia/entrypoint.sh`  
`loopia/entrypoint_staging.sh`  
`loopia/creatednsrecord.py`  
`loopia/removednsrecord.py`  
My example is for two wildcard certificates for *.lofjard.se and *.int.lofjard.se respectively.

### Run with:
```
podman run \
	-v <Log folder>:/var/log/letsencrypt \
	-v <Cert store>:/etc/letsencrypt \
	-v ./loopia:/opt/loopia \
	-e LOOPIA_USER=<API username> \
	-e LOOPIA_PASS=<API password> \
	--entrypoint /opt/loopia/entrypoint.sh \
	-it --rm --name cert-renew certbot/certbot
```


