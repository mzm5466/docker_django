# 基础镜像
FROM python:3.6-alpine3.8

RUN mkdir /var/www
# 指定工作路径
WORKDIR /var/www
#设置时区和源
ENV TIME_ZONE Asia/Shanghai
#使用清华源
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories

RUN apk add --no-cache -U tzdata \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \ 
    && echo "${TIME_ZONE}" > /etc/timezone
# 拷贝安装python包清单
COPY . ./

# 安装项目依赖包
RUN apk update && apk add --no-cache --virtual=build-dependencies \
    g++ bash \
    build-base libffi-dev python3-dev \
    libffi openssl ca-certificates \
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    linux-headers pcre-dev supervisor\
    &&  python -m pip install --upgrade --force pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    &&  pip install setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple\
    && pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && apk del \
        gcc \
        libc-dev \
        linux-headers \
    && rm -rf /tmp/*

#切换工作目录
WORKDIR /var/www/src

CMD ["/usr/bin/supervisord","-c","/var/www/supervisord.conf"]