PROJET = simeis-server

.PHONY: all release build test check manual clean

all: check test

build:
	RUSTFLAGS="-C code-model=kernel -C codegen-units=1" cargo build --release

release: build
	strip target/release/$(PROJET)

test:
	cargo test

check:
	cargo check

manual:
	typst compile doc/manual.typ

clean:
	cargo clean

