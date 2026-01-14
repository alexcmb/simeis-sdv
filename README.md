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

# Organisation des Branchs

## Main
développement de features, où pousser tout changement du code

## Feature/x
branche pour développer une nouvelle feature, à merger dans main

## Bug/x
branche pour résoudre un bug, à merger dans main

## release/x
branche contenant une version de release