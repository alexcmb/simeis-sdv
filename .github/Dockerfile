# Étape 1 : build Rust
FROM rust:1.85.0-bookworm AS builder
WORKDIR /app

COPY Cargo.toml Cargo.lock ./
COPY src ./src

RUN cargo build --release

# Étape 2 : image finale minimale
FROM debian:bookworm-slim
WORKDIR /app

COPY --from=builder /app/target/release/simeis-server /app/simeis-server

EXPOSE 8080
CMD ["./simeis-server"]