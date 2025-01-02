#!/bin/sh

echo -e "Entrypoint env: $LOOPIA_USER"

echo -e "Running certbot manual mode for lofjard.se"
certbot certonly -n --agree-tos --manual -m mikael@lofjard.se --preferred-challenges=dns --server https://acme-staging-v02.api.letsencrypt.org/directory --manual-auth-hook /opt/loopia/auth_hook.sh -d *.lofjard.se -d lofjard.se
/opt/loopia/cleanup_hook.sh
cat /etc/letsencrypt/live/lofjard.se/fullchain.pem /etc/letsencrypt/live/lofjard.se/privkey.pem >/etc/letsencrypt/live/lofjard.se/haproxy.pem
echo -e "Done for lofjard.se"

echo -e "Running certbot manual mode for int.lofjard.se"
certbot certonly -n --agree-tos --manual -m mikael@lofjard.se --preferred-challenges=dns --server https://acme-staging-v02.api.letsencrypt.org/directory --manual-auth-hook /opt/loopia/auth_hook.sh -d *.int.lofjard.se -d int.lofjard.se
/opt/loopia/cleanup_hook.sh
cat /etc/letsencrypt/live/int.lofjard.se/fullchain.pem /etc/letsencrypt/live/int.lofjard.se/privkey.pem >/etc/letsencrypt/live/int.lofjard.se/haproxy.pem
echo -e "Done for int.lofjard.se"
echo -e "All done!"
