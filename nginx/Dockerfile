#nginx
FROM alpine:3.8

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories
RUN apk update \
        && apk upgrade \
        && apk add --no-cache bash \
        bash-doc \
        bash-completion \
        && rm -rf /var/cache/apk/* \
        && /bin/bash

RUN apk add --no-cache nginx

CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
