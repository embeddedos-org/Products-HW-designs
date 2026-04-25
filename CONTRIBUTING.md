# Contributing to Products-HW-designs

Thank you for your interest in contributing!

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make your changes
4. Run the build and tests locally
5. Submit a pull request

## Development Setup

```bash
git clone https://github.com/embeddedos-org/Products-HW-designs.git
cd Products-HW-designs
cmake -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

## Code Guidelines

- **Standard:** C11
- **Warnings:** `-Wall -Wextra` must compile clean
- **Naming:** `snake_case` for all identifiers
- **Types:** Use `<stdint.h>` types

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):
```
feat: add new feature
fix: resolve bug
docs: update documentation
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
