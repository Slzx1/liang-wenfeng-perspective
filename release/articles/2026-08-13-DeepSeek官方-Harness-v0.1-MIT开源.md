# Harness-v0.1-MIT开源

- URL: https://github.com/deepseek-ai/deepseek-harness
- 抓取日期: 2026-10-17
- 来源: DeepSeek官方
- 证据级别: 一手
- 说明: DeepSeek Harness官方仓库，MIT许可，Agent运行框架。

---

GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness: Everything is a Plugin. · GitHub

Skip to content

You signed in with another tab or window. 
Reload
 to refresh your session.

You signed out in another tab or window. 
Reload
 to refresh your session.

You switched accounts on another tab or window. 
Reload
 to refresh your session.

Dismiss alert

master
Branches
Tags
Go to file
Code
Open more actions menu
Latest commit

History
22,382 Commits
22,382 Commits
Folders and files
Name
Name
Last commit message
Last commit date
.agents
.agents

.claude
.claude

.github
.github

apps
apps

benchmarks
benchmarks

docs
docs

native
native

packages
packages

patches
patches

python
python

scripts
scripts

snapshots
snapshots

vendor
vendor

website
website

.editorconfig
.editorconfig

.gitattributes
.gitattributes

.gitignore
.gitignore

.gitlab-ci.yml
.gitlab-ci.yml

.jscpd.json
.jscpd.json

.oxlintrc.json
.oxlintrc.json

.oxlintrc.staged.json
.oxlintrc.staged.json

.rgignore
.rgignore

AGENTS.md
AGENTS.md

BENCHMARK.md
BENCHMARK.md

BRAND_GUIDELINES.i18n.yaml
BRAND_GUIDELINES.i18n.yaml

BRAND_GUIDELINES.md
BRAND_GUIDELINES.md

BRAND_GUIDELINES.zh.md
BRAND_GUIDELINES.zh.md

CLAUDE.md
CLAUDE.md

CONTRIBUTING.i18n.yaml
CONTRIBUTING.i18n.yaml

CONTRIBUTING.md
CONTRIBUTING.md

CONTRIBUTING.zh.md
CONTRIBUTING.zh.md

LICENSE
LICENSE

Makefile
Makefile

README.i18n.yaml
README.i18n.yaml

README.md
README.md

README.zh.md
README.zh.md

SAFETY.i18n.yaml
SAFETY.i18n.yaml

SAFETY.md
SAFETY.md

SAFETY.zh.md
SAFETY.zh.md

THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md

lefthook.yml
lefthook.yml

package.json
package.json

pnpm-lock.yaml
pnpm-lock.yaml

pnpm-workspace.yaml
pnpm-workspace.yaml

pytest.ini
pytest.ini

tsconfig.base.client.json
tsconfig.base.client.json

tsconfig.base.json
tsconfig.base.json

tsconfig.client.json
tsconfig.client.json

tsconfig.host.json
tsconfig.host.json

tsconfig.json
tsconfig.json

tsconfig.node.base.json
tsconfig.node.base.json

tsdown.config.ts
tsdown.config.ts

vitest.bench.config.ts
vitest.bench.config.ts

vitest.config.ts
vitest.config.ts

vitest.e2e.config.ts
vitest.e2e.config.ts

vitest.expected.config.ts
vitest.expected.config.ts

vitest.shared.ts
vitest.shared.ts

vitest.snapshot.config.ts
vitest.snapshot.config.ts

vitest.web-stress.config.ts
vitest.web-stress.config.ts

vitest.web.config.ts
vitest.web.config.ts

vitest.web.perf.config.ts
vitest.web.perf.config.ts

View all files
Repository files navigation
DeepSeek Harness

English | 
中文

DeepSeek Harness (
dsh
) is an open-source agent harness developed by 
DeepSeek AI
.

It is built on an 
everything-is-a-plugin
 architecture and powered by 
Cordis
, whose design is described in 
A Programming Paradigm for Spatiotemporal Composability
.

Documentation: 
https://deepseek-harness.github.io/deepseek-harness/

Developer preview

DeepSeek Harness is in 
developer preview
 and iterating rapidly. 
THERE WILL BE COMPATIBILITY-BREAKING CHANGES.

Review the 
safety notice
 before running the project.

Run

Run from 
npm

Install 
Node.js
, then run:

npx @deepseek-ai/dsh web

The command starts the Web UI at 
http://127.0.0.1:3080
 by default and opens it in the default browser for a local launch. An SSH launch only prints the host URL because the SSH client or editor owns the local forwarded address. Pass 
--no-open
 to run the server without opening a browser. See 
Web UI guide
.

Run from source

To run from a repository checkout:

git clone https://github.com/deepseek-ai/deepseek-harness.git

cd
 deepseek-harness
pnpm install
pnpm run build
pnpm dsh web

pnpm run build
 prepares the repository artifacts. 
pnpm dsh web
 uses those built artifacts without rebuilding.

Community and support

Submit feedback or bug reports through 
GitHub Discussions
.

Add the 
dsh-plugin
 topic to your plugin repository for discoverability.

Join 
DeepSeek Harness Discord community
.

Contributing

See 
CONTRIBUTING.md
.

Development

Start with the 
development guide
 and 
architecture documentation
.

pnpm run dev:web
 builds, serves, and rebuilds client bundles on source edits in one terminal, and 
make help
 lists the matching Make targets for Web and Desktop; the guide's application commands section owns the full table.

For agents, follow 
AGENTS.md
.

Citation

@misc
{
deepseek-harness2026
,

title
=
{
DeepSeek Harness: Everything is a Plugin
}
,

author
=
{
DeepSeek-AI
}
,

year
=
{
2026
}
,

publisher
=
{
GitHub
}
,

howpublished
=
{
\url{https://github.com/deepseek-ai/deepseek-harness}
}
,
}

License

MIT

Third-party dependencies and their licenses are disclosed in 
THIRD_PARTY_NOTICES.md
.

About
DeepSeek Harness: Everything is a Plugin.
deepseek.com/harness
Topics
ai-agents
cordis
dsh
dsh-plugin
Resources
Readme
MIT license
Contributing
Contributing
Activity
Custom properties
Stars
251.2k
 stars
Watchers
1.1k
 watching
Forks
30.2k
 forks
Report repository
Releases
Contributors
Languages

    You can’t perform that action at this time.
