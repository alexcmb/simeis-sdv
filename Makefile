# Makefile pour le projet simeis
DOSSIER = target/release/

.PHONY: release
release:
        @echo "=== Compilation release de simeis ==="
        RUSTFLAGS="-C code-model=kernel -C codegen-units=1" cargo build --release
        strip $(DOSSIER)simeis-server
        @echo "Binaire optimisé généré : $(DOSSIER)"

# Build manuel avec Typst
.PHONY: manual
manual:
        @echo "=== Compilation du manuel ==="
        typst compile manual.typ manual.pdf
        @echo "Manuel généré : manual.pdf"

# Vérification du code
.PHONY: check
check:
        @echo "=== Vérification du code ==="
        caro check
        cargo fmt -- --check
        cargo clippy -- -D warnings

.PHONY: python-check
python-check:
		@echo "=== Vérification du code python ==="
		black --check .

# Lancer les tests unitaires
.PHONY: test
test:
        @echo "=== Exécution des tests unitaires ==="
        cargo test

# Nettoyage
.PHONY: clean
clean:
        @echo "=== Nettoyage des fichiers de build ==="
        cargo clean
        rm -f manual.pdf
        @echo "Nettoyage terminé"
