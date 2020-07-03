```
mkdir -p nginx/sites-enabled && NGINX_HOSTNAME=example.com envsubst < nginx/plotly-dash.template > nginx/sites-enabled/example.com.conf
```
