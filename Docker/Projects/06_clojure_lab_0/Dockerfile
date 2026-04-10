FROM clojure:temurin-21-tools-deps

WORKDIR /app

COPY deps.edn .

RUN clojure -P

COPY src ./src

CMD ["clojure", "-M", "-m", "core"]