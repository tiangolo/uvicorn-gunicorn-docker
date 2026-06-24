# Release Notes

## Latest Changes

### Features

* 👷 Avoid creating unnecessary `*.pyc` files with `PYTHONDONTWRITEBYTECODE=1` and ensure logs are printed immediately with `PYTHONUNBUFFERED=1`. PR [#192](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/192) by [@estebanx64](https://github.com/estebanx64).

### Refactors

* ♻️ Do not `EXPOSE` ports `80` and `443` by default as they can be customized. PR [#238](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/238) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆ Bump uvicorn from 0.47.0 to 0.49.0. PR [#301](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/301) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump gunicorn from 25.1.0 to 26.0.0. PR [#293](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/293) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump uvicorn from 0.41.0 to 0.47.0. PR [#294](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/294) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump uvicorn[standard] from 0.38.0 to 0.41.0. PR [#281](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/281) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump gunicorn from 23.0.0 to 25.1.0. PR [#280](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/280) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump uvicorn[standard] from 0.35.0 to 0.38.0. PR [#265](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/265) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.34.3 to 0.35.0. PR [#256](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/256) by [@dependabot[bot]](https://github.com/apps/dependabot).
* Bump uvicorn[standard] from 0.34.0 to 0.34.3. PR [#255](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/255) by [@dependabot[bot]](https://github.com/apps/dependabot).
* Bump uvicorn[standard] from 0.32.1 to 0.34.0. PR [#250](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/250) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.32.0 to 0.32.1. PR [#249](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/249) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.21.0 to 0.32.0. PR [#244](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/244) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Drop support for Python 3.7 and 3.8. PR [#246](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/246) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump gunicorn from 21.2.0 to 22.0.0. PR [#210](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/210) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump gunicorn from 21.2.0 to 22.0.0 in /docker-images. PR [#209](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/209) by [@dependabot[bot]](https://github.com/apps/dependabot).

### Docs

* 📝 Deprecate this Docker image, use Uvicorn with `--workers` ✨. PR [#225](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/225) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 👷 Simplify pull request workflow triggers. PR [#308](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/308) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update setup-python pin comment to 6.2.0. PR [#307](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/307) by [@tiangolo](https://github.com/tiangolo).
* 📝 Refactor release notes, move to its own file. PR [#306](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/306) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update issue-manager to 0.7.1. PR [#305](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/305) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update issue-manager to 0.7.0. PR [#304](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/304) by [@tiangolo](https://github.com/tiangolo).
* 🔒️ Add zizmor workflow security checks. PR [#303](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/303) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump the github-actions group across 1 directory with 3 updates. PR [#302](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/302) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Remove config files now in central GitHub repo. PR [#297](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/297) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update Dependabot. PR [#295](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/295) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump docker/build-push-action from 6 to 7. PR [#283](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/283) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/setup-buildx-action from 3 to 4. PR [#284](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/284) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 5.0.0 to 6.0.2. PR [#274](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/274) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump peter-evans/dockerhub-description from 4 to 5. PR [#267](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/267) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Upgrade actions/checkout from v5 to v6. PR [#271](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/271) by [@tiangolo](https://github.com/tiangolo).
* 👷 Upgrade `latest-changes` GitHub Action and pin `actions/checkout@v5`. PR [#270](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/270) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump actions/checkout from 4.2.2 to 5.0.0. PR [#259](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/259) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Drop support for Python 3.9. PR [#266](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/266) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump tiangolo/issue-manager from 0.5.1 to 0.6.0. PR [#264](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/264) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/labeler from 5 to 6. PR [#261](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/261) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 5 to 6. PR [#260](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/260) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update Dependabot config prefix. PR [#257](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/257) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update CI config for labeler. PR [#252](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/252) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add Labeler to CI. PR [#251](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/251) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump tiangolo/latest-changes from 0.3.1 to 0.3.2. PR [#248](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/248) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Remove old unused files. PR [#247](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/247) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump actions/checkout from 4.1.7 to 4.2.2. PR [#245](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/245) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR [#239](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/239) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#237](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/237) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update `latest-changes` GitHub Action. PR [#236](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/236) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump docker/build-push-action from 5 to 6. PR [#217](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/217) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump gunicorn from 22.0.0 to 23.0.0. PR [#222](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/222) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 4.1.0 to 4.1.7. PR [#216](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/216) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump docker/login-action from 1 to 3. PR [#211](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/211) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update issue-manager.yml GitHub Action permissions. PR [#219](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/219) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump peter-evans/dockerhub-description from 3 to 4. PR [#203](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/203) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump docker/build-push-action from 2 to 5. PR [#202](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/202) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump tiangolo/issue-manager from 0.4.0 to 0.5.0. PR [#201](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/201) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump docker/setup-buildx-action from 1 to 3. PR [#200](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/200) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/setup-python from 4 to 5. PR [#199](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/199) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Add GitHub templates for discussions and issues, and security policy. PR [#205](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/205) by [@alejsdev](https://github.com/alejsdev).
* 🔧 Update `latest-changes.yml`. PR [#198](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/198) by [@alejsdev](https://github.com/alejsdev).

## 0.8.0

### Features

* ✨ Add support for multi-arch builds, including support for `arm64` (e.g. Mac M1). PR [#195](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/195) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Update test badge in `README.md`. PR [#197](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/197) by [@alejsdev](https://github.com/alejsdev).

### Refactors

* 🔥 Remove Alpine support. PR [#193](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/193) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆️ Bump gunicorn from 20.1.0 to 21.2.0. PR [#185](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/185) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.20.0 to 0.21.0. PR [#174](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/174) by [@dependabot[bot]](https://github.com/apps/dependabot).

### Internal

* ⬆️ Bump actions/checkout from 3.3.0 to 4.1.0. PR [#189](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/189) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update mypy requirement from ^0.991 to ^1.1. PR [#173](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/173) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update black requirement from ^22.10 to ^23.1. PR [#171](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/171) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 3.1.0 to 3.3.0. PR [#170](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/170) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update latest changes token. PR [#178](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/178) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action to update Docker Hub description, fix. PR [#168](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/168) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action for Docker Hub description. PR [#167](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/167) by [@tiangolo](https://github.com/tiangolo).

## 0.7.0

The highlights of this release are:

* Support for Python 3.10 and 3.11.
* Deprecation of Python 3.6.
    * The last Python 3.6 image tag was pushed and is available in Docker Hub, but it won't be updated or maintained anymore.
    * The last image with a date tag is `python3.6-2022-11-25`.
* Upgraded versions of all the dependencies.

### Features

* ✨ Add support for Python 3.11. PR [#159](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/159) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Upgrade Uvicorn version. PR [#161](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/161) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add support for Python 3.10. PR [#99](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/99) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Upgrade Uvicorn to the last version supporting Python 3.6. PR [#155](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/155) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add Python 3.9 and Alpine Python 3.9. PR [#52](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/52) by [@graue70](https://github.com/graue70).
* ⬆️ Install uvicorn[standard] to include uvloop and Gunicorn support. PR [#54](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/54) by [@tiangolo](https://github.com/tiangolo).

### Breaking Changes

* 🔥 Deprecate and remove Python 3.6. PR [#160](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/160) by [@tiangolo](https://github.com/tiangolo).

### Docs

* ✏️ Fix typo, delete repeated line in README. PR [#147](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/147) by [@jiyeonseo](https://github.com/jiyeonseo).
* 📝 Add note to discourage Alpine with Python. PR [#96](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/96) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add warning for Kubernetes, when to use this image. PR [#95](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/95) by [@tiangolo](https://github.com/tiangolo).
* ✏️ Fix typo duplicate "Note" in Readme. PR [#92](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/92) by [@tiangolo](https://github.com/tiangolo).
* ✏️ Fix typo (type annotation) in tests. PR [#55](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/55) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆️ Update mypy requirement from ^0.971 to ^0.991. PR [#166](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/166) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update autoflake requirement from ^1.3.1 to ^2.0.0. PR [#165](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/165) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update black requirement from ^20.8b1 to ^22.10. PR [#164](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/164) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update docker requirement from ^5.0.3 to ^6.0.1. PR [#163](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/163) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Update Dependabot config. PR [#162](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/162) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add scheduled CI every Monday. PR [#158](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/158) by [@tiangolo](https://github.com/tiangolo).
* 👷 Do not run double CI for PRs, run on push only on master. PR [#157](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/157) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action alls-green. PR [#156](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/156) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update black requirement from ^19.10b0 to ^20.8b1. PR [#87](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/87) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update mypy requirement from ^0.770 to ^0.971. PR [#143](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/143) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update docker requirement from ^4.2.0 to ^5.0.3. PR [#97](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/97) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/setup-python from 1 to 4.1.0. PR [#142](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/142) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update isort requirement from ^4.3.21 to ^5.8.0. PR [#88](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/88) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump tiangolo/issue-manager from 0.2.0 to 0.4.0. PR [#85](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update pytest requirement from ^5.4.1 to ^7.0.1. PR [#123](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/123) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 2 to 3.1.0. PR [#145](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/145) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 📌 Add external dependencies and Dependabot to get automatic upgrade PRs. PR [#84](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/84) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update Latest Changes. PR [#83](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/83) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove unused Travis and old GitHub Actions configs. PR [#56](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/56) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action latest-changes, update issue-manager, add funding. PR [#53](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/53) by [@tiangolo](https://github.com/tiangolo).

## 0.6.0

* Add docs about installing and pinning dependencies. PR [#41](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/41).
* Add `slim` version. PR [#40](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/40).
* Remove leftover unneeded config for tests. PR [#39](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/39).
* Add extra configs, tests, and docs for:
    * `WORKER_CLASS`
    * `TIMEOUT`
    * `KEEP_ALIVE`
    * `GRACEFUL_TIMEOUT`
    * `ACCESS_LOG`
    * `ERROR_LOG`
    * `GUNICORN_CMD_ARGS`
    * `MAX_WORKERS`
    * PR [#38](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/38)
* Set up CI using GitHub actions, they provide more free instances, so builds finish faster (4 min vs 9 min). PR [#37](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/37).
* Add support for Python 3.8. PR [#36](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/36).
* Refactor tests to remove custom testing Dockerfiles, generate them during tests. PR [#35](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/35).
* Refactor and simplify build process to reduce code duplication. PR [#34](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/34).
* Disable `pip` cache during installation with `--no-cache-dir`. PR [#13](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/13) by [@pmav99](https://github.com/pmav99).
* Migrate local development from Pipenv to Poetry. PR [#31](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/31).
* Add tests and docs for custom `PRE_START_PATH` env var. PR [#30](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/30).
* Add support for custom `PRE_START_PATH` env var. PR [#12](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/12) by [@mgfinch](https://github.com/mgfinch).

## 0.5.0

* Refactor tests to use env vars and add image tags for each build date, like `tiangolo/uvicorn-gunicorn:python3.7-2019-10-15`. PR [#15](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/15).
* Update Gunicorn worker heartbeat directory to `/dev/shm` to improve performance. PR [#9](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/9) by [@wshayes](https://github.com/wshayes).
* Upgrade Travis. PR [#7](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/7).

## 0.4.0

* Add support for live auto-reload with an additional custom script `/start-reload.sh`, check the [updated documentation](https://github.com/tiangolo/uvicorn-gunicorn-docker#development-live-reload). PR <a href="https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/6" target="_blank">#6</a>.

## 0.3.0

* Set `WORKERS_PER_CORE` by default to `1`, as it shows to have the best performance on benchmarks.
* Make the default web concurrency, when `WEB_CONCURRENCY` is not set, to a minimum of 2 workers. This is to avoid bad performance and blocking applications (server application) on small machines (server machine/cloud/etc). This can be overridden using `WEB_CONCURRENCY`. This applies for example in the case where `WORKERS_PER_CORE` is set to `1` (the default) and the server has only 1 CPU core. PR <a href="https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/5" target="_blank">#5</a>.

## 0.2.0

* Make `/start.sh` run independently, reading and generating used default environment variables. And remove `/entrypoint.sh` as it doesn't modify anything in the system, only reads environment variables. PR <a href="https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/4" target="_blank">#4</a>.

## 0.1.2

* Whenever this image is built (and each of its tags/versions), trigger a build for the children images (<a href="https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker" target="_blank">FastAPI</a> and <a href="https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker" target="_blank">Starlette</a>).

## 0.1.0

* Add support for `/app/prestart.sh`.
