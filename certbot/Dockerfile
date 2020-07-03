FROM alpine:3.10

ARG VERSION

RUN apk add --no-cache --update python3 ca-certificates libffi-dev openssl-dev openssl && \
    apk add --no-cache --virtual=build-dependencies build-base linux-headers python3-dev tzdata && \
    pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir certbot-dns-ovh==${VERSION} && \
    apk del build-dependencies

ENTRYPOINT ["certbot"]

LABEL org.label-schema.name="Certbot" \
      org.label-schema.version=${VERSION} \
      org.label-schema.docker.schema-version="1.0"
