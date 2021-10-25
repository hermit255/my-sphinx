FROM alpine:3.10 AS builder
ARG PLANTUML_VERSION=1.2019.12
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
      curl
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /temp
# plantuml
RUN curl -sSL -o /temp/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download
# font
RUN curl -sSL -o /temp/NotoSansCJKjp-Regular.ttf https://github.com/hnakamur/Noto-Sans-CJK-JP/raw/master/fonts/NotoSansCJKjp-Regular.ttf

FROM alpine:3.10
ARG PLANTUML_DIR
ARG FONT_DIR
COPY --from=builder /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
COPY --from=builder /usr/bin/sphinx-* /usr/bin/
COPY --from=builder /usr/lib/python3.7/site-packages/ /usr/lib/python3.7/site-packages/
COPY --from=builder /temp/plantuml.jar ${PLANTUML_DIR}/plantuml.jar
COPY --from=builder /temp/NotoSansCJKjp-Regular.ttf ${FONT_DIR}/NotoSansCJKjp-Regular.ttf

RUN apk add --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.6/main \
        python3 \
        make \
        su-exec \
        zlib \
        libjpeg-turbo \
        freetype \
        ttf-droid \
        ttf-droid-nonlatin \
        # for latexPDF build
        texlive-full \
        # for PlantUml
        openjdk8-jre \
        'graphviz<2.39' \
    && mkdir -p /usr/share/zoneinfo/Asia \
    && ln /etc/localtime /usr/share/zoneinfo/Asia/Tokyo

WORKDIR /docs
CMD ["sphinx-autobuild", ".", "_build/html", "--host", "0.0.0.0"]
