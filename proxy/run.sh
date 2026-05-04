#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'

#p iniciar o servoço prroxy em shell e configurar p rodar em 1 plano