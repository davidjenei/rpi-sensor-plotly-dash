#!/bin/sh

while :; do
	payload=$(cat <<-EOF
	{
	"value": "$(curl -s ifconfig.me)",
	"ttl": 60,
	"type": "A",
	"name": "$NAME",
	"zone_id": "$ZONE_ID"
	}
	EOF
	)
	curl -s -X "PUT" "https://dns.hetzner.com/api/v1/records/$RECORD" \
	-H 'Content-Type: application/json' \
	-H "Auth-API-Token: $TOKEN" \
	-d "$payload"
	sleep 300 # TODO: TTL
done
