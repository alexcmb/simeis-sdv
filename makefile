# VARIABLES
prog_name :=simeis-server

release:
	RUSTFLAGS="-C code-model=kernel -C codegen-units=1" cargo build --release
	strip target/release/$(prog_name)
debug:
	cargo build 
	strip target/debug/$(prog_name)
# install:
# 	cp target/$(target)/$(prog_name) ~/bin/$(prog_name)$(extension)
documentation:
	typst compile doc/manual.typ
check:
	cargo check
	cargo fmt --check
	cargo clippy -- -D warnings

.PHONY: python-check
python-check:
	black --check .

unit_tests:
	cargo test
clean:
	cargo clean

# all: release install

#Make help
help:
	@echo "make debug=1 pour debug ou make sans options pour release"