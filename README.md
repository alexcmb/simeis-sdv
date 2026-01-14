# Compiler

```
# Pour seulement compiler
cargo build

# Pour le lancer
cargo run
```

# Tester

```
cargo test
```
# Organisation des branches

main        : branche de développement principale (features + bugs)
feature/x   : développement de nouvelles fonctionnalités → merge dans main
bug/x       : correction de bugs → merge dans main et release
release/x   : branche de release (ex: release/1.0.0) main vers release 
