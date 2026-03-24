# Étape 1 : build Rust
FROM rust:1.85.0-bookworm
WORKDIR /app

COPY target/release/simeis-server .

EXPOSE 8080
CMD ["./simeis-server"]