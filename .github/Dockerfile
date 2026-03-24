FROM rust:1.85.0-bookworm

# We assume the binary is placed at this path in the build context
COPY target/release/simeis-server /usr/local/bin/simeis-server

# Expose typical web server port (assuming 8080)
EXPOSE 8080

ENTRYPOINT ["simeis-server"]
