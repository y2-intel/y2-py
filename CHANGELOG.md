# Changelog

## 0.6.1 (2026-04-01)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/y2-intel/y2-py/compare/v0.6.0...v0.6.1)

### Features

* **internal:** implement indices array format for query and form serialization ([895dd59](https://github.com/y2-intel/y2-py/commit/895dd5901ea0ab39499a792324529600d9baeee6))


### Chores

* **ci:** skip lint on metadata-only changes ([3d0ea28](https://github.com/y2-intel/y2-py/commit/3d0ea2899e62f3553a9de3a456623c9824f8c719))

## 0.6.0 (2026-03-24)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/y2-intel/y2-py/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([7ac8aa7](https://github.com/y2-intel/y2-py/commit/7ac8aa7b848808b0351d0aae655f39619f34111f))
* **api:** manual updates ([bd51662](https://github.com/y2-intel/y2-py/commit/bd51662c507a221c5ce111e5a659e3548984793e))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([97c72ac](https://github.com/y2-intel/y2-py/commit/97c72ac578bfbad7f7b550aa377350b3964763eb))
* **pydantic:** do not pass `by_alias` unless set ([98b74ba](https://github.com/y2-intel/y2-py/commit/98b74baa394cc9837883c35797c85f32ac47f089))
* sanitize endpoint path params ([6d82fdf](https://github.com/y2-intel/y2-py/commit/6d82fdf3827fd6bde5319506eb8b5b27cd6532ef))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([a6dc82b](https://github.com/y2-intel/y2-py/commit/a6dc82b2fa7b7ce51b3656f5044bb399372520fc))
* **internal:** tweak CI branches ([bc0443e](https://github.com/y2-intel/y2-py/commit/bc0443e88062b2f25ba444e4411d5f189878f0f6))
* **internal:** update gitignore ([f5f35c3](https://github.com/y2-intel/y2-py/commit/f5f35c37c951e6127730f9065aae297bdbf72214))
* update SDK settings ([c75bd15](https://github.com/y2-intel/y2-py/commit/c75bd15c12658bbc53c88ba8e349b541a94970ac))
* update SDK settings ([aa71298](https://github.com/y2-intel/y2-py/commit/aa71298ab717275b107e39e6a284b23f33c0e374))

## 0.5.0 (2026-03-04)

Full Changelog: [v0.4.1...v0.5.0](https://github.com/y2-intel/y2-py/compare/v0.4.1...v0.5.0)

### Features

* **api:** api update ([894bca5](https://github.com/y2-intel/y2-py/commit/894bca5be120b8b415bb063627a2a057ad87c9c6))


### Chores

* **internal:** codegen related update ([698699c](https://github.com/y2-intel/y2-py/commit/698699c9d1a4c6053a53991ad573dd37519a53bd))

## 0.4.1 (2026-02-27)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/y2-intel/y2-py/compare/v0.4.0...v0.4.1)

### Chores

* **ci:** bump uv version ([ae89f6f](https://github.com/y2-intel/y2-py/commit/ae89f6f385332d0fece0e90615b7129c6309ccc0))
* format all `api.md` files ([d69710d](https://github.com/y2-intel/y2-py/commit/d69710d70b69922ba6844ab854e4eccc6d9ec843))
* **internal:** add request options to SSE classes ([1906367](https://github.com/y2-intel/y2-py/commit/1906367f1eecb025cb5ed281fddd9084703ac345))
* **internal:** fix lint error on Python 3.14 ([ebc7607](https://github.com/y2-intel/y2-py/commit/ebc7607e150eaaa20e1c4501633990e51f084505))
* **internal:** make `test_proxy_environment_variables` more resilient ([54047d5](https://github.com/y2-intel/y2-py/commit/54047d5f9f57249c61d822ac859cd24475738c04))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([aa71652](https://github.com/y2-intel/y2-py/commit/aa7165232a8a70f10dbca2511791174e2c8a638d))
* **internal:** remove mock server code ([068ea3c](https://github.com/y2-intel/y2-py/commit/068ea3cce65a1711880c53b0c666b4c2a5084839))
* update mock server docs ([4a6f24a](https://github.com/y2-intel/y2-py/commit/4a6f24ac250d2add7385519b7f80ed6afdce9d68))

## 0.4.0 (2026-02-10)

Full Changelog: [v0.3.1...v0.4.0](https://github.com/y2-intel/y2-py/compare/v0.3.1...v0.4.0)

### Features

* **api:** manual updates ([7ddddd8](https://github.com/y2-intel/y2-py/commit/7ddddd89e38e78de561d0f966fcc616f5a63dd49))

## 0.3.1 (2026-02-10)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/y2-intel/y2-py/compare/v0.3.0...v0.3.1)

### Chores

* **internal:** bump dependencies ([dd8b46a](https://github.com/y2-intel/y2-py/commit/dd8b46a2ccbd81f9692e07e2e7fdc8b76c724f89))

## 0.3.0 (2026-01-30)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/y2-intel/y2-py/compare/v0.2.0...v0.3.0)

### Features

* **client:** add custom JSON encoder for extended type support ([e85356a](https://github.com/y2-intel/y2-py/commit/e85356a381475ffbe08fb959284ecb2d571f0aff))
* **client:** add support for binary request streaming ([a8f65b3](https://github.com/y2-intel/y2-py/commit/a8f65b35488abe14d21442ab57d99f7885949d21))


### Chores

* **ci:** upgrade `actions/github-script` ([897862a](https://github.com/y2-intel/y2-py/commit/897862a888389466e8b43b5c8b768f1c5537b196))
* **internal:** codegen related update ([38f3008](https://github.com/y2-intel/y2-py/commit/38f30086f2f78de68b56799d36b0aefed9ea557c))
* **internal:** update `actions/checkout` version ([61ea208](https://github.com/y2-intel/y2-py/commit/61ea2080efa36f79ebf6c2962b8e0f29183e8fde))

## 0.2.0 (2025-12-31)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/y2-intel/y2-py/compare/v0.1.0...v0.2.0)

### Features

* **api:** manual updates ([32aa037](https://github.com/y2-intel/y2-py/commit/32aa0375b37f757ecf4e55769f9883b28006d647))

## 0.1.0 (2025-12-28)

Full Changelog: [v0.0.3...v0.1.0](https://github.com/y2-intel/y2-py/compare/v0.0.3...v0.1.0)

### Features

* **api:** manual updates ([2a311cd](https://github.com/y2-intel/y2-py/commit/2a311cd4dd379409836ea539244f742128c5b4e4))

## 0.0.3 (2025-12-26)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/y2-intel/y2-py/compare/v0.0.2...v0.0.3)

### Chores

* update SDK settings ([86d94f7](https://github.com/y2-intel/y2-py/commit/86d94f730719ad9c2be47e1c1fde598fb88eebc2))

## 0.0.2 (2025-12-24)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/y2-intel/y2-py/compare/v0.0.1...v0.0.2)

### Chores

* update SDK settings ([199b21a](https://github.com/y2-intel/y2-py/commit/199b21aa7a34f9a5489fa593a764afa8c7097248))
* update SDK settings ([9d60021](https://github.com/y2-intel/y2-py/commit/9d600214561cf0b69254a5b20783bef26ee6f34f))
