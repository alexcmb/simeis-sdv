FROM rust:1.85.0-bookworm

WORKDIR /app

# On copie uniquement le binaire déjà compilé par le workflow via make release
COPY target/release/simeis-server .

EXPOSE 8080

CMD ["./simeis-server"]