FROM alpine:3.10 AS builder

ADD requirements.txt .
RUN apk add --update --no-cache \
        python3 \
        python3-dev \
        make \
        build-base \
        git \
        zlib-dev \
        libjpeg-turbo-dev \
        freetype-dev \
        tzdata \
        gcc \
    && pip3 install --upgrade pip \
    && pip install -r  ${script_dir}requirements.txt

FROM alpine:3.10

ENV PLANTUML_VERSION 1.2019.12

COPY --from=builder /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
COPY --from=builder /usr/bin/sphinx-* /usr/bin/
COPY --from=builder /usr/lib/python3.7/site-packages/ /usr/lib/python3.7/site-packages/

RUN apk add --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.6/main \
        python3 \
        make \
        su-exec \
        zlib \
        libjpeg-turbo \
        freetype \
        'graphviz<2.39' \
        ttf-droid \
        ttf-droid-nonlatin \
        openjdk8-jre \
        curl \
    && mkdir /plantuml \
    && curl -sSL -o /plantuml/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download \
    && mkdir /fonts \
    && curl -sSL -o /fonts/NotoSansCJKjp-Regular.ttf https://github.com/hnakamur/Noto-Sans-CJK-JP/raw/master/fonts/NotoSansCJKjp-Regular.ttf \
    && mkdir -p /usr/share/zoneinfo/Asia \
    && ln /etc/localtime /usr/share/zoneinfo/Asia/Tokyo

WORKDIR /docs

CMD ["sphinx-autobuild", "source", "build/html", "--host", "0.0.0.0"]
