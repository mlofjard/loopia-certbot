#!/bin/sh

echo -e "Auth hook env: $LOOPIA_USER"

if [ -f /tmp/certtoken ]; then
	FIRSTTOKEN=$(cat /tmp/certtoken)
	echo "Running with $FIRSTTOKEN and $CERTBOT_VALIDATION"
	/opt/loopia/creatednsrecord.py $FIRSTTOKEN $CERTBOT_VALIDATION $LOOPIA_USER $LOOPIA_PASS $SUBDOMAIN
	sleep 300
else
	echo $CERTBOT_VALIDATION >/tmp/certtoken
	echo "First run"
fi
