# VARIABLES
prog_name :=simeis-server

debug ?=

$(info debug is $(debug))

# MODE BUG
ifdef debug
	release :=
	target :=debug
	extension :=debug
# MODE RELEASE
else
	release :=--release
	target :=release
	extension :=
	RUSTFLAGS := -C code-model=kernel -C codegen-units=1
endif

build:
	cargo build $(release)
	strip target/$(target)/$(prog_name)
install:
	cp target/$(target)/$(prog_name) ~/bin/$(prog_name)$(extension)
documentation:
	typst compile doc/manual.typ
check:
	cargo check
unit_tests:
	cargo test
clean:
	cargo clean
	
all: build install

#Make help
help:
	@echo "make debug=1 pour debug ou make sans options pour release"