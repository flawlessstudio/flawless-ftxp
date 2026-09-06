# Git + GitHub Full-Spectrum Reference Architecture — FT-X Master Execution Prompt

> **Status:** Canonical execution instruction candidate  
> **Repository:** `flawlessstudio/flawless-ftxp`  
> **Protocol:** FTXP v1.0  
> **Execution profile:** FT-X  
> **Purpose:** zero-loss consolidation of the Git + GitHub architecture, lifecycle, surface, navigation, interaction, governance, security, automation, failure/recovery, evidence, coverage and saturation workstream.

---

## 0. Execution contract

Execute this instruction as a single governed research-and-assurance program. Do not treat its sections as independent prompts and do not duplicate the same fact across multiple SSOTs.

The required operating sequence is:

```text
DISCOVER
→ VERIFY
→ CLASSIFY
→ CANONICALIZE
→ DEDUPLICATE
→ FACET
→ RELATE
→ MODEL CONTEXT
→ MODEL LIFECYCLE
→ RESOLVE EVIDENCE
→ FIND GAPS
→ CHALLENGE
→ REGRESS
→ SATURATE
→ APPLY
→ VALIDATE
→ FREEZE
```

A claim of completeness is permitted only under the explicit completeness and evidence-horizon rules in this document.

---

## 1. Mission

Build the canonical, materially exhaustive, non-redundant and operationally useful reference architecture for the complete Git + GitHub domain, then use it to audit and, when separately authorized for mutation, improve `flawlessstudio/flawless-ftxp`.

The target domain includes:

1. Git conceptual architecture.
2. Git object and reference model.
3. Git operational model.
4. Git lifecycle.
5. Git failure, recovery and maintenance model.
6. GitHub platform architecture.
7. GitHub product and feature architecture.
8. GitHub repository architecture.
9. GitHub repository lifecycle.
10. GitHub full-spectrum surface, navigation and interaction architecture.
11. GitHub identity, authentication, authorization, roles, permissions and policy architecture.
12. GitHub governance and security architecture.
13. GitHub automation, Actions and programmatic interface architecture.
14. GitHub Apps, integrations, webhooks and external-dependency architecture.
15. GitHub notifications, events, search and observability architecture.
16. GitHub plans, entitlements, billing, limits and deployment-model variation.
17. GitHub client/device variation.
18. GitHub failure, destructive-operation, rollback, recovery, maintenance and EOL architecture.
19. GitHub temporal, preview, deprecated and historical architecture.
20. Every additional materially relevant and non-redundant candidate discovered within the locked scope.

The objective is not maximum text volume. It is maximum **material coverage, correctness, traceability and usefulness at minimum necessary duplication and complexity**.

---

## 2. Final questions the architecture must answer

The final system MUST make it possible to answer unambiguously:

- What is Git and what are its canonical objects, references, states and operations?
- How does a Git repository move from creation through daily operation, integration, release, maintenance, recovery and retirement?
- What is GitHub and what layers does it add over Git?
- What products, entities, features, surfaces, settings, controls, routes, actions and states form GitHub?
- How do GitHub capabilities vary by role, permission, policy, plan, account type, repository state, object state, client and time?
- What are the UI, API, CLI, Git-transport and webhook representations of a capability?
- Which events, notifications and audit evidence are produced by each lifecycle transition?
- How do security controls, governance controls and policy inheritance affect repository behavior?
- How can failures propagate, be detected, contained, corrected and recovered?
- How can any frozen repository baseline be reconstructed exactly?
- Which elements of the global GitHub universe are applicable to `flawless-ftxp`?
- What is present, missing, redundant, incorrect, optional, conditional or not applicable in `flawless-ftxp`?
- What exact criteria must pass before the repository may be declared frozen?

---

## 3. Normative principles

### 3.1 Correctness before breadth

Priority order:

```text
correctness
→ conceptual distinction
→ material coverage
→ coherence
→ canonical terminology
→ operability
→ traceability
→ simplicity
→ compactness
→ additional breadth
```

### 3.2 MECE where natural; facets where orthogonal

Use mutually exclusive / collectively exhaustive primary categories where the domain supports them. Where dimensions naturally overlap, use orthogonal facets and typed relationships rather than forcing them into one hierarchy.

### 3.3 Keep modeling dimensions distinct

```text
HIERARCHY ≠ FACETS ≠ ATTRIBUTES ≠ STATES ≠ LIFECYCLE ≠ RELATIONSHIPS ≠ IMPLEMENTATIONS ≠ EXAMPLES
```

### 3.4 Git ≠ GitHub

- **Git:** distributed version-control system.
- **GitHub:** platform built around Git that adds hosting, collaboration, governance, automation, security, publication, APIs, integrations and other platform capabilities.

Do not attribute GitHub-only mechanisms to Git or vice versa.

### 3.5 Repository ≠ platform

Distinguish at minimum:

```text
Git repository
local repository
remote repository
GitHub repository
personal account
organization
enterprise
GitHub App
GitHub Actions
GitHub platform service
external integration
```

### 3.6 Current ≠ conditional ≠ preview ≠ legacy ≠ deprecated ≠ historical

Classify lifecycle/availability status explicitly whenever material.

### 3.7 Discover broadly; implement selectively

```text
DISCOVER EVERYTHING MATERIAL
≠
IMPLEMENT EVERYTHING DISCOVERED
```

The target repository receives only candidates that are applicable, value-producing, non-redundant and maintainable.

---

## 4. Evidence policy

When executing current-state research, prefer evidence in this order:

1. Official Git documentation.
2. Official GitHub documentation.
3. Official GitHub repositories/specifications.
4. Official GitHub API, CLI, Actions, Security and product documentation.
5. Official standards relevant to a feature.
6. High-authority technical sources when primary evidence is insufficient.
7. Secondary evidence only when necessary and clearly identified.

Every materially time-sensitive GitHub claim MUST distinguish:

```text
FACT
INFERENCE
RECOMMENDATION
CONVENTION
ASSUMPTION
```

Every observation that can vary over time SHOULD record:

```yaml
observed_at:
source:
product:
plan:
account_context:
role:
permission_context:
repository_state:
client:
feature_status:
```

### 4.1 Negative evidence rule

```text
NOT OBSERVED ≠ DOES NOT EXIST
```

Use explicit states such as:

```text
ABSENT_WITH_EVIDENCE
NOT_OBSERVED
UNKNOWN
INACCESSIBLE
NOT_APPLICABLE
UNVERIFIED
CONFLICTING_EVIDENCE
TEMPORALLY_UNCERTAIN
```

---

## 5. FTXP execution profile

```yaml
profile: FT-X
granularity: maximal-useful
evidence: required-for-material-current-claims
historical: selective
emerging: enabled-when-relevant
cross_domain: enabled
adversarial_review: required
independent_rediscovery: required
regression: full
saturation: required
```

Apply the canonical FTXP pipeline, gates G0–G12 and SAT-MAX rules without creating a competing methodology.

---

# PART I — GIT

## 6. Git canonical scope

### 6.1 Foundations

Map at minimum:

- repository;
- working tree;
- index / staging area;
- object database;
- refs;
- HEAD;
- configuration;
- hooks.

### 6.2 Object model

- blob;
- tree;
- commit;
- annotated tag.

### 6.3 Reference model

- branches;
- tags;
- symbolic refs;
- remote-tracking refs;
- namespaces where materially relevant.

### 6.4 Repository forms and operating modes

- non-bare;
- bare;
- local;
- remote;
- shallow;
- partial clone;
- sparse checkout;
- worktrees;
- submodules.

### 6.5 Core operations

Map semantics, preconditions, outputs, failure modes and recovery implications for materially relevant operations including:

```text
init
clone
status
add
commit
branch
switch / checkout
fetch
pull
merge
rebase
push
tag
revert
reset
restore
cherry-pick
stash
bisect
reflog
gc
maintenance
```

### 6.6 Commit graph and history

Map:

- DAG;
- ancestry;
- parents;
- merge bases;
- divergence;
- fast-forward;
- non-fast-forward;
- rewritten history;
- reachable/unreachable objects where relevant.

### 6.7 Synchronization

Map:

```text
local ↔ remote
tracking
upstream
fetch refspecs
push behavior
conflict handling
divergence
force / force-with-lease implications
```

### 6.8 Repository hygiene and integrity

Include:

- `.gitignore`;
- `.gitattributes`;
- line-ending strategy;
- text/binary handling;
- generated files;
- large-file considerations;
- commit/tag signing when justified;
- hook strategy;
- repository maintenance.

---

## 7. Git full lifecycle

Model end-to-end:

```text
REPOSITORY INTENT
→ INITIALIZATION
→ CONFIGURATION
→ CONTENT CREATION
→ STAGING
→ COMMIT
→ BRANCHING
→ LOCAL DEVELOPMENT
→ REMOTE SYNCHRONIZATION
→ INTEGRATION
→ CONFLICT RESOLUTION
→ HISTORY MANAGEMENT
→ VERSION IDENTIFICATION
→ DISTRIBUTION
→ MAINTENANCE
→ RECOVERY
→ DEPRECATION
→ ARCHIVAL / RETIREMENT
```

For each stage model:

- purpose;
- inputs;
- outputs;
- actor;
- preconditions;
- operations;
- states;
- transitions;
- invariants;
- failure modes;
- reversible/destructive characteristics;
- recovery paths.

Include happy path, alternative path, failure path and recovery path.

---

# PART II — GITHUB UNIVERSE

## 8. GitHub platform domains

Treat the following as first-pass product/domain candidates, not as a frozen universal list:

- GitHub.com;
- Repositories;
- Issues;
- Pull Requests;
- Discussions;
- Projects;
- Actions;
- Packages;
- Pages;
- Codespaces;
- Copilot and materially relevant AI/agentic repository capabilities;
- code/security products and repository security surfaces;
- Organizations;
- Enterprise;
- Apps;
- Marketplace;
- REST API;
- GraphQL API;
- Webhooks;
- GitHub CLI;
- GitHub Mobile;
- GitHub Desktop;
- Search;
- Notifications;
- account/profile/authentication settings;
- billing and entitlement surfaces;
- migration/import/export surfaces;
- audit/observability surfaces;
- support/status/help surfaces;
- Sponsors/Education/other platform domains only when material to the full-spectrum map.

New material domains discovered during execution MUST enter the Candidate Registry before inclusion.

---

## 9. Canonical entity universe

Start with, validate and expand an Entity Registry containing materially relevant entities such as:

```text
PLATFORM / IDENTITY
- user
- personal account
- organization
- enterprise
- team

REPOSITORY / GIT-HOSTED
- repository
- file
- directory
- commit
- branch
- tag
- release
- release asset

COLLABORATION
- issue
- sub-issue
- pull request
- review
- review thread
- comment
- discussion
- label
- milestone
- saved reply

AUTOMATION
- workflow
- workflow run
- job
- step
- runner
- runner group
- artifact
- cache
- environment
- deployment
- secret
- variable

SECURITY
- code-scanning alert
- secret-scanning alert
- dependency alert
- security advisory
- dependency
- security configuration
- protection policy

INTEGRATION / AUTHORIZATION
- GitHub App
- GitHub App installation
- OAuth App
- webhook
- token
- deploy key
- SSH/GPG credential

PUBLICATION / ENVIRONMENT
- package
- Pages site
- Codespace
- published artifact
```

Do not confuse an entity with a feature, surface, action, event or UI representation.

---

## 10. Universal node model

All canonical registries SHOULD derive from one metamodel:

```yaml
node:
  identity:
    id:
    canonical_name:
    aliases:
    description:
    concept_type:

  classification:
    platform:
    product:
    domain:
    feature_family:
    entity_type:

  structure:
    parent:
    children:
    contains:
    contained_by:

  interaction:
    surfaces:
    components:
    controls:
    actions:
    entry_points:
    exit_points:

  navigation:
    routes:
    route_patterns:
    deep_links:

  lifecycle:
    stages:
    states:
    transitions:
    preconditions:
    postconditions:

  access:
    actors:
    roles:
    permissions:
    scopes:
    authentication:
    authorization:

  availability:
    plans:
    entitlements:
    policies:
    feature_flags:
    clients:
    devices:
    deployment_models:

  programmatic:
    git_equivalent:
    cli_equivalent:
    rest_equivalent:
    graphql_equivalent:
    webhook_equivalent:

  behavior:
    inputs:
    outputs:
    side_effects:
    artifacts:
    events:
    notifications:

  assurance:
    security_impact:
    privacy_impact:
    reversibility:
    destructive:
    failure_modes:
    recovery:
    auditability:

  temporal:
    introduced:
    changed:
    deprecated:
    removed:
    preview_status:
    observed_at:

  evidence:
    sources:
    provenance:
    confidence:
    verification_status:

  governance:
    status:
    owner:
    exclusions:
    unresolved:
```

---

## 11. Concept versus occurrence

A canonical capability may appear in multiple UI/programmatic locations. Store one concept and N occurrences.

```text
CANONICAL CONCEPT
├─ occurrence A
├─ occurrence B
├─ occurrence C
└─ occurrence N
```

Occurrence model:

```yaml
occurrence:
  concept_id:
  surface:
  client:
  route:
  component:
  label:
  context:
  evidence:
```

Repeated visual representations MUST NOT become duplicate canonical concepts.

---

# PART III — FULL-SPECTRUM SURFACE, NAVIGATION & INTERACTION ARCHITECTURE

## 12. Scope of surface discovery

Map GitHub as a multidimensional dynamic system, not as a flat sitemap.

The discovery MUST cover and relate, where materially relevant:

```text
ENTITIES
PRODUCTS
FEATURES
SURFACES
INFORMATION ARCHITECTURE
NAVIGATION
MENUS
SUBMENUS
TABS
SIDEBARS
DASHBOARDS
FEEDS
SETTINGS
SECTIONS
SUBSECTIONS
CONTROLS
OPTIONS
FORMS
DIALOGS
MODALS
DRAWERS
WIZARDS
ACTIONS
ROUTES
DEEP LINKS
SEARCH
FILTERS
SORTS
COMMANDS
SHORTCUTS
STATES
STATE TRANSITIONS
JOURNEYS
LIFECYCLES
ACTORS
ROLES
PERMISSIONS
ACCOUNT SCOPES
POLICIES
PLANS
ENTITLEMENTS
CLIENTS
DEVICES
AUTOMATION
WORKFLOWS
APIS
CLI
GIT TRANSPORT
WEBHOOKS
EVENTS
NOTIFICATIONS
INTEGRATIONS
SECURITY
AUDIT
OBSERVABILITY
FAILURE MODES
ERROR SURFACES
RECOVERY PATHS
DESTRUCTIVE OPERATIONS
LIMITS / QUOTAS
RETENTION
MIGRATION
AVAILABILITY
PREVIEWS
DEPRECATIONS
HISTORICAL SURFACES
PROVENANCE
```

---

## 13. Information architecture and navigation

Classify navigation by type:

```text
GLOBAL
ACCOUNT
ORGANIZATION
ENTERPRISE
REPOSITORY
OBJECT-SPECIFIC
PRODUCT-SPECIFIC
UTILITY
CONTEXTUAL
BREADCRUMB
TAB-BASED
SIDEBAR-BASED
DROPDOWN-BASED
OVERFLOW
COMMAND-PALETTE
SEARCH-DRIVEN
DEEP-LINK
PROGRAMMATIC
RESPONSIVE
```

Represent navigation as a directed graph, not only a tree:

```text
NODE
→ NAVIGATES_TO
→ NODE
```

Each navigation edge SHOULD capture:

```yaml
source:
destination:
trigger:
component:
action:
required_context:
permissions:
conditional:
```

Detect orphan/deep surfaces, multiple entry points, cycles and context-specific routes.

---

## 14. Menus, tabs, settings and controls

Recursive menu expansion:

```text
MENU
→ GROUP
→ ITEM
→ SUBMENU
→ GROUP
→ ITEM
→ CONTROL
→ OPTION
→ ACTION
→ DIALOG
→ CONFIRMATION
→ STATE TRANSITION
→ DESTINATION
```

Apply equivalent recursion to tabs, sidebars, settings sections and control groups.

### 14.1 Settings scopes

Map at minimum when present:

```text
PERSONAL ACCOUNT SETTINGS
ORGANIZATION SETTINGS
ENTERPRISE SETTINGS
REPOSITORY SETTINGS
SECURITY SETTINGS
DEVELOPER SETTINGS
APPLICATION / INTEGRATION SETTINGS
BILLING / PLAN SETTINGS
NOTIFICATION SETTINGS
ACCESS SETTINGS
AUTOMATION SETTINGS
```

For every setting/control capture:

```yaml
id:
surface:
section:
label:
type:
value_type:
allowed_values:
default_value:
required_role:
required_permission:
required_plan:
policy_dependencies:
state_dependencies:
effect:
side_effects:
security_impact:
reversible:
resettable:
confirmation_required:
destructive:
api_equivalent:
evidence:
```

Candidate control representations include toggles, checkboxes, radio groups, selectors, text/number inputs, buttons, links, upload controls, token-generation controls, role/permission selectors and policy selectors.

---

## 15. Route architecture

Keep route namespaces separate:

```text
WEB UI
REST API
GRAPHQL
GIT TRANSPORT
RAW / DOWNLOAD
CALLBACK / WEBHOOK / INTEGRATION
```

Route record:

```yaml
namespace:
method_if_applicable:
pattern:
parameters:
query_parameters:
entity:
operation:
scope:
authentication:
permissions:
product:
plan:
state_requirements:
result:
canonical:
deprecated:
evidence:
```

Never conflate a web UI URL, REST endpoint, GraphQL operation and Git transport endpoint.

---

## 16. Action architecture

Discover canonical actions rather than relying on a closed verb list. Candidate families include:

```text
CREATE / READ / LIST / SEARCH / FILTER / SORT / UPDATE / DELETE / RESTORE / CONFIGURE
ENABLE / DISABLE / ACTIVATE / DEACTIVATE
ASSIGN / UNASSIGN / LABEL / UNLABEL
SUBSCRIBE / UNSUBSCRIBE / WATCH / UNWATCH / MUTE
OPEN / CLOSE / REOPEN / LOCK / UNLOCK
REVIEW / COMMENT / APPROVE / REQUEST_CHANGES / DISMISS
MERGE / REBASE / SQUASH / REVERT
RUN / RERUN / CANCEL / RETRY / APPROVE_RUN
DEPLOY / PUBLISH / UNPUBLISH
ARCHIVE / UNARCHIVE / TRANSFER / FORK / STAR
INSTALL / AUTHORIZE / REVOKE / UNINSTALL
IMPORT / EXPORT / DOWNLOAD / UPLOAD
```

For every action capture actor, target, preconditions, permission, control/entry point, state transition, side effects, events, notifications, audit evidence, failure and recovery.

---

## 17. Entry-point and result architecture

For every material feature determine how it can be reached:

```text
global navigation
repository navigation
context menu
direct URL
notification
search result
command palette
settings
API
CLI
webhook
external integration
email/deep link
```

Also model every material result:

```text
ACTION
→ navigation
| state change
| artifact creation
| event
| notification
| workflow
| permission/configuration change
| destructive change
| external call
| no-op
| error
```

---

## 18. UI representation facet

Classify visual/interaction representation independently from semantic identity. Candidate representation types:

```text
page
dashboard
feed
list
table
board
tree
graph
timeline
diff
editor
viewer
tab
sidebar
toolbar
breadcrumb
button
link
dropdown
menu
context menu
command
form
field
selector
toggle
modal
drawer
popover
tooltip
banner
toast
alert
badge
label
status indicator
wizard
onboarding flow
confirmation flow
```

Do not turn representation types into the primary domain taxonomy.

---

## 19. Search and discovery architecture

Map separately where available:

```text
GLOBAL SEARCH
CODE SEARCH
REPOSITORY SEARCH
ISSUE SEARCH
PR SEARCH
DISCUSSION SEARCH
PROJECT SEARCH
USER / ORGANIZATION SEARCH
MARKETPLACE SEARCH
COMMAND PALETTE
FILTERING
SORTING
SAVED / PERSISTENT VIEWS
```

Capture scope, syntax/qualifiers, filters, sort options, result types, permission effects and navigation behavior.

---

## 20. Accessibility, locale and responsive variation

Treat accessibility and representation variation as orthogonal facets.

Relevant candidates include:

- keyboard navigation and shortcuts;
- focus behavior and accessible interaction;
- screen-reader-relevant semantics where they affect functionality;
- theme/contrast/motion settings;
- responsive behavior;
- locale/language;
- regional date/time/number presentation;
- translated UI/documentation.

Distinguish:

```text
CLIENT ≠ DEVICE ≠ VIEWPORT ≠ LOCALE
```

A responsive GitHub.com view is not automatically equivalent to GitHub Mobile.

---

# PART IV — CONTEXT AND ACCESS

## 21. Context matrix

Absence in one context MUST NOT be interpreted as global absence.

Evaluate material candidates across applicable dimensions:

```text
ENTITY
× PRODUCT
× FEATURE
× SURFACE
× ACTION
× STATE
× LIFECYCLE STAGE
× ACTOR
× ROLE
× PERMISSION
× ACCOUNT TYPE / SCOPE
× PLAN / ENTITLEMENT
× POLICY
× CLIENT
× DEVICE / VIEWPORT
× REPOSITORY TYPE
× FEATURE AVAILABILITY
× TEMPORAL STATUS
```

Do not blindly materialize the Cartesian product. Use it as a coverage/gap-detection model.

---

## 22. Identity, authentication and authorization

Keep these layers distinct:

```text
IDENTITY
→ AUTHENTICATION
→ CREDENTIAL
→ ROLE
→ PERMISSION
→ RESOURCE
→ OPERATION
→ SCOPE
→ POLICY
```

Candidate authentication/credential mechanisms to validate include passwords, 2FA, passkeys, recovery mechanisms, SSH keys, signing keys, PATs, OAuth and GitHub App tokens, SSO/enterprise identity mechanisms, Actions tokens and OIDC-derived credentials.

### 22.1 Permission lattice

```yaml
authorization_rule:
  actor_type:
  role:
  permission:
  operation:
  resource:
  scope:
  inherited_from:
  overridden_by:
  policy_constraints:
  plan_constraints:
```

### 22.2 Policy inheritance

Model effective policy across applicable hierarchy, e.g.:

```text
ENTERPRISE
↓
ORGANIZATION
↓
REPOSITORY
↓
RESOURCE
```

Record inheritance, override, restriction, allowance, block, bypass and exception where supported.

Distinguish configured value from effective value.

---

## 23. Plan, entitlement, deployment model and billing

Keep distinct:

```text
PLAN ≠ ENTITLEMENT ≠ USAGE ≠ BILLING
```

Capture product/tier and deployment-model variation only from current evidence. Candidate contexts can include GitHub Free/Pro/Team/Enterprise Cloud, GitHub Enterprise Server versions, Copilot tiers, security entitlements, preview/beta status and organization/enterprise policy.

Billing/commercial surfaces, when material to availability, may include subscription, metered usage, seats/licenses, budgets/spending controls, invoices and usage reporting.

---

## 24. Quotas, limits and retention

For material capabilities record applicable limits:

```yaml
limit:
  capability:
  dimension:
  value:
  scope:
  plan:
  reset_window:
  enforcement:
  error_behavior:
  evidence:
  observed_at:
```

Candidate dimensions include API rate limits, storage, Actions execution, artifacts/caches, Codespaces, Packages and retention limits.

Model retention separately:

```text
retention policy
expiration
automatic deletion
manual deletion
archive
recoverability
historical persistence
```

---

# PART V — PROGRAMMATIC, AUTOMATION AND INTEGRATION PLANES

## 25. UI / CLI / API / Git / webhook parity

Classify each capability according to its available interaction channels:

```text
UI_ONLY
CLI_ONLY
API_ONLY
UI+API
UI+CLI
CLI+API
UI+CLI+API
GIT_TRANSPORT
WEBHOOK_EVENT_ONLY
NO_PROGRAMMATIC_EQUIVALENT_KNOWN
```

Where APIs exist, distinguish REST and GraphQL. Track Git transport independently.

Capability parity matrix SHOULD compare materially relevant clients/channels, such as:

```text
Web
Mobile
Desktop
CLI
REST
GraphQL
Git
Codespaces
IDE integrations
```

Use statuses:

```text
SUPPORTED
PARTIAL
READ_ONLY
WRITE_ONLY
CONDITIONAL
UNAVAILABLE
UNKNOWN
NOT_APPLICABLE
```

---

## 26. GitHub Actions and automation architecture

For every automation model:

```yaml
trigger:
event:
scope:
actor:
permissions:
inputs:
workflow:
jobs:
outputs:
artifacts:
secrets:
side_effects:
failure_behavior:
retry_strategy:
idempotence:
security_exposure:
```

Distinguish validation, release, maintenance, security and repository-management automation.

---

## 27. Event architecture

Maintain an Event Registry:

```yaml
event:
  id:
  source:
  actor:
  entity:
  trigger:
  payload:
  subscribers:
  webhook:
  notification:
  workflow_trigger:
  audit_event:
  state_transition:
```

Connect events to actions and state changes:

```text
EVENT
→ TRIGGER
→ ACTION
→ STATE TRANSITION
→ SIDE EFFECT
→ NEW EVENT
```

---

## 28. Notification architecture

Model causality:

```text
SOURCE EVENT
→ REASON
→ SUBSCRIPTION RULE
→ RECIPIENT
→ CHANNEL
→ DELIVERY
→ USER STATE
→ ACTION
```

Capture repository/thread/account notification settings, watching/subscription semantics, mute/ignore behavior, mentions, assignments, reviews, workflow/security/account notifications and materially relevant external notification channels.

Track grouping/threading, suppression, read state, saved/done states, unsubscribe/mute controls and delivery failures when material.

---

## 29. Apps and integrations

Keep separate:

```text
GitHub App registration
GitHub App installation
GitHub App authorization
GitHub App permissions
installation repository scope
user access token
installation token
webhook subscription
OAuth App
OAuth authorization/scopes
Marketplace
external service
```

For external dependencies capture dependency, criticality, security boundary, availability impact and failure propagation.

---

# PART VI — SECURITY, TRUST AND OBSERVABILITY

## 30. Security architecture

Map security as a transverse system:

```text
AUTHENTICATION SECURITY
CREDENTIAL SECURITY
REPOSITORY PROTECTION
BRANCH / TAG / RULESET PROTECTION
SECRET SECURITY
CODE SCANNING
DEPENDENCY SECURITY
SUPPLY-CHAIN SECURITY
ACTIONS SECURITY
APP SECURITY
ORGANIZATION SECURITY
ENTERPRISE SECURITY
AUDIT
INCIDENT RESPONSE
```

For each material control record availability, scope, enablement, inheritance, role, alerts/detection, blocking, bypass/exception, remediation, dismissal, auditability and recovery.

---

## 31. Trust boundaries

Model trust/data/credential crossings between materially relevant zones, for example:

```text
USER DEVICE
↔ GIT CLIENT
↔ GITHUB PLATFORM
↔ GITHUB ACTIONS RUNNER
↔ GITHUB APP
↔ EXTERNAL SERVICE
↔ CLOUD / DEPLOYMENT TARGET
```

Capture credentials crossing, data crossing, permissions, trust assumptions, attack surface and audit trail.

---

## 32. Credential and secret lifecycles

Credential lifecycle:

```text
CREATE / ISSUE
→ STORE
→ USE
→ ROTATE
→ EXPIRE
→ REVOKE
→ DELETE
```

Secret model SHOULD capture source, storage scope, consumers, permissions, exposure surface, masking, rotation, revocation, leak detection and recovery.

---

## 33. Audit and observability

Differentiate:

```text
operational observability
security observability
administrative audit
user/repository activity history
```

Candidate evidence surfaces include commit history, issue/PR timelines, checks/statuses, workflow/job logs, deployments, security alerts, audit/security logs, repository insights/traffic, dependency graph and usage/billing telemetry when materially relevant.

---

# PART VII — LIFECYCLES, STATES, FAILURE AND RECOVERY

## 34. GitHub repository full lifecycle

Model:

```text
IDEA / REQUIREMENT
→ REPOSITORY CREATION
→ INITIAL CONFIGURATION
→ BOOTSTRAP
→ BASELINE CONTENT
→ BRANCH / CHANGE PREPARATION
→ IMPLEMENTATION
→ LOCAL VALIDATION
→ COMMIT
→ PUSH
→ PULL REQUEST
→ AUTOMATED CHECKS
→ REVIEW
→ APPROVAL
→ MERGE
→ POST-MERGE VALIDATION
→ VERSION DECISION
→ VERSION BUMP
→ CHANGELOG
→ TAG
→ RELEASE
→ DISTRIBUTION / PUBLICATION
→ MONITORING
→ MAINTENANCE
→ PATCH / MINOR / MAJOR CHANGE
→ DEPRECATION
→ ROLLBACK / REVERT / RECOVERY
→ SUPERSESSION
→ ARCHIVAL / EOL
```

For every stage record purpose, inputs, outputs, actor, permissions, preconditions, actions, artifacts, validations, security, failures, recovery and transition criteria.

---

## 35. State-machine registry

Every material lifecycle entity SHOULD have an explicit state machine where state is meaningful.

```yaml
state_machine:
  entity:
  initial_states:
  states:
  terminal_states:
  transitions:
    - from:
      action:
      to:
      actor:
      preconditions:
      guards:
      side_effects:
      reversible:
```

Candidate entities include repository, issue, pull request, discussion, review, workflow/run/job, deployment, environment, release, security alert, GitHub App installation, Codespace and package.

---

## 36. Version / tag / release / baseline architecture

Keep distinct:

```text
Git commit identity
≠ Git tag
≠ semantic version
≠ GitHub Release
≠ repository baseline
≠ FTXP protocol version
```

For `flawless-ftxp`, explicitly resolve the relationship among protocol version, repository `VERSION`, release tag, GitHub Release and frozen commit SHA.

---

## 37. Data and artifact lifecycle

For material stored artifacts model:

```text
CREATE
→ STORE
→ VERSION
→ READ
→ MODIFY
→ TRANSFER
→ EXPORT
→ ARCHIVE
→ RETAIN
→ DELETE
→ RECOVER
```

Apply selectively to repositories, commits, issues/PRs, releases, packages, workflow artifacts/caches, Codespaces, logs, alerts, audit records and credentials.

---

## 38. Import, export and migration

Separate:

```text
IMPORT
EXPORT
TRANSFER
MIGRATE
MIRROR
CLONE
FORK
ARCHIVE
RESTORE
```

Do not conflate Git clone/fetch, repository transfer, organization/enterprise migration, API export and artifact download.

---

## 39. Failure model

Discover and classify material failures, including candidates such as:

- invalid/accidental commit;
- wrong branch;
- rejected push;
- divergence;
- merge/rebase conflict or failure;
- force-push risk;
- CI/check failure;
- review rejection;
- permission/policy denial;
- secret exposure;
- dependency/security finding;
- compromised third-party Action/integration;
- malformed workflow;
- release/tag mistake;
- bad merge;
- deleted branch;
- lost commit;
- credential compromise;
- webhook/integration outage;
- service degradation.

For each:

```text
DETECTION
→ CONTAINMENT
→ CORRECTION
→ RECOVERY
→ VALIDATION
→ PREVENTION
```

---

## 40. Failure propagation and error surfaces

Represent propagation:

```text
FAILURE A
→ degrades/breaks CAPABILITY B
→ blocks TRANSITION C
→ generates ERROR/ALERT D
→ triggers RECOVERY E
```

Classify error surfaces such as Git errors, CLI errors, API/HTTP errors, UI validation errors, banners/toasts/inline errors, workflow/check failures, security alerts and permission denials.

Record cause, diagnostic evidence, remediation and retryability.

---

## 41. Recovery and reconstructability

Demonstrate recovery paths for materially relevant cases, including previous commit/branch state, reverted merge, deleted branch where recoverable, erroneous release/tag, failed workflow, invalid configuration, compromised credential and frozen historical baselines.

A frozen baseline MUST be reconstructable unambiguously from version-control and release metadata.

---

## 42. Destructive / danger-zone architecture

Every destructive operation must identify:

```text
trigger
permission
confirmation
blast radius
reversibility / irreversibility
audit evidence
recovery
safer alternative
```

Candidate operations include delete, transfer, archive, remove access, revoke/uninstall, disable security control, delete branch/tag/release/artifact/environment and credential revocation.

---

## 43. Maintenance, service availability and EOL

Distinguish feature availability from service availability.

Model when material:

```text
active maintenance
security maintenance
dependency maintenance
stale branch/artifact cleanup
deprecation
supersession
archive
end-of-life
```

Service-state concepts such as normal/degraded/outage/maintenance may be modeled where they affect lifecycle behavior.

---

# PART VIII — TEMPORAL, EVIDENCE AND UNKNOWN SPACE

## 44. Feature temporal status

Candidate lifecycle:

```text
UNKNOWN
→ ANNOUNCED
→ PREVIEW
→ GENERALLY_AVAILABLE
→ CHANGED
→ DEPRECATED
→ RETIRED
```

Not every feature traverses every state.

Canonical status vocabulary SHOULD distinguish at least:

```text
CURRENT_CANONICAL
CURRENT_CONDITIONAL
PREVIEW
LEGACY_SUPPORTED
DEPRECATED
REMOVED
HISTORICAL
```

---

## 45. Evidence horizon

Every run MUST declare its evidence horizon:

```yaml
evidence_horizon:
  execution_date:
  github_dot_com:
  enterprise_cloud:
  enterprise_server_versions:
  clients:
  plans:
  roles_observed:
  account_contexts:
  sources_available:
  inaccessible_contexts:
```

This bounds completeness claims and makes them falsifiable.

---

## 46. Unknown-space registry

Track uncertainty explicitly:

```text
KNOWN_KNOWN
KNOWN_UNKNOWN
INACCESSIBLE
CONTEXT_NOT_AVAILABLE
UNVERIFIED
CONFLICTING_EVIDENCE
TEMPORALLY_UNCERTAIN
```

No evidence is not evidence of absence.

---

## 47. Contradiction registry

When Docs, UI, API, CLI or observed behavior conflict:

```yaml
contradiction:
  claim_a:
  evidence_a:
  claim_b:
  evidence_b:
  affected_scope:
  resolution:
  status:
```

Resolve by evidence and context, never intuition.

---

# PART IX — DISCOVERY, TAXONOMY AND SATURATION

## 48. Discovery-source matrix

Use independent discovery surfaces where accessible and relevant:

1. Git documentation.
2. GitHub Docs information architecture.
3. Live GitHub.com surfaces.
4. Personal-account settings.
5. Repository settings.
6. Organization settings.
7. Enterprise surfaces when available.
8. REST API endpoint catalog.
9. GraphQL schema/documentation.
10. Webhook event catalog.
11. GitHub CLI command tree.
12. GitHub Mobile.
13. GitHub Desktop.
14. Codespaces.
15. Copilot/AI capabilities.
16. Actions.
17. Code/security products.
18. Packages/Pages/Projects/Issues/PRs/Discussions.
19. Apps/Marketplace.
20. Search/Notifications.
21. Changelog/release notes/feature previews.
22. Permission and role variation.
23. Plan/entitlement variation.
24. State and client variation.
25. Adversarial independent rediscovery.

No individual source is accepted as the entire GitHub universe.

---

## 49. Discovery directions

Translate exhaustive exploration into explicit passes:

```text
TOP-DOWN
Platform → product → feature → surface → component → control

BOTTOM-UP
Control/action → capability → feature → product → platform

HORIZONTAL
Sibling features / equivalent surfaces

VERTICAL
Parent / child decomposition

LIFECYCLE
Before → during → after

CROSS-CUTTING
Security / permissions / policies / plans / clients / states

PROGRAMMATIC
UI ↔ CLI ↔ REST ↔ GraphQL ↔ Git ↔ webhook

TEMPORAL
Current ↔ preview ↔ legacy ↔ deprecated ↔ historical

ADVERSARIAL
Search explicitly for omissions, contradictions and boundary failures
```

---

## 50. Fractal expansion rule

For every material node recursively determine:

```text
What is it?
What contains it?
What does it contain?
What states does it have?
What actions affect it?
Who can act?
Under what permissions/policies?
Under what plans/entitlements?
On what clients/devices?
Through what routes?
Through what APIs/CLI/Git transport?
What events does it emit?
What notifications follow?
What automation interacts with it?
What security impact exists?
What audit evidence remains?
How can it fail?
How is it recovered?
What lifecycle stage uses it?
What adjacent nodes exist?
→ RECURSE on materially new candidates
```

Stop recursion when further decomposition adds representation detail, aliases or examples without new material capability/structure.

---

## 51. Candidate discovery passes

At minimum perform independent passes for:

```text
canonical Git concepts
canonical GitHub concepts
repository lifecycle
governance
security
automation
releases/versioning
notifications/events
programmatic interfaces
recovery/rollback
maintenance/EOL
integrations
plans/policies/permissions
clients/devices
historical/deprecated candidates
adversarial discovery
independent rediscovery
```

Every candidate enters Candidate Registry before becoming canonical.

```text
DISCOVERED ≠ VALIDATED ≠ CANONICAL ≠ INCLUDED
```

---

## 52. Terminology and canonicalization

For each term resolve:

```text
canonical term
synonym
alias
colloquial form
UI wording
CLI wording
API wording
legacy label
deprecated/historical term
related-but-distinct concept
```

Do not confuse:

```text
feature
surface
page
menu
setting
control
action
route
API endpoint
CLI command
event
notification
policy
permission
state
artifact
```

---

## 53. Deduplication

Apply:

```text
D1 Exact
D2 Lexical
D3 Referential
D4 Semantic
D5 Functional
D6 Structural
```

Allowed outcomes:

```text
KEEP
MERGE
ALIAS
RELATE
SPLIT
EXCLUDE
UNRESOLVED
```

Do not create distinct canonical categories only because the same capability appears in different UI/product locations.

---

## 54. Primary taxonomies and facets

Produce separate primary taxonomies where natural, including:

- Git conceptual/object/operational architecture;
- Git lifecycle;
- GitHub platform/product architecture;
- repository architecture;
- governance;
- security;
- automation;
- collaboration;
- integrations;
- version/release lifecycle;
- recovery lifecycle.

### 54.1 Surface facets

Candidate orthogonal facets include:

```text
Identity / concept type
Abstraction level
Function
Lifecycle stage
Actor
Interaction model
Change-control role
Governance
Permission
Security
Automation
Artifact type
State
Temporal role
Scope
Integration mode
Evidence/provenance
Reversibility
Persistence
Standardization
Quality impact
Failure domain
Recovery mechanism
Representation/UI component
Client/device
Plan/entitlement
Policy inheritance
Availability/temporal status
```

Activate only facets that add material discriminatory value.

---

## 55. Typed relationship model

Use specific relations when justified, including candidates such as:

```text
IS_A
INSTANCE_OF
PART_OF
CONTAINS
USES
REQUIRES
ENABLES
PRODUCES
TRANSFORMS
IMPLEMENTS
PRECEDES
FOLLOWS
SUPERSEDES
DEPRECATED_BY
DERIVED_FROM
ALTERNATIVE_TO
COMPLEMENTS
OVERLAPS_WITH
CONTRASTS_WITH
NAVIGATES_TO
EXPOSES
CONTAINS_CONTROL
PERFORMS_ACTION
TRANSITIONS_TO
AVAILABLE_TO
REQUIRES_PERMISSION
REQUIRES_PLAN
REQUIRES_STATE
GOVERNED_BY
OVERRIDDEN_BY
INHERITS_FROM
EMITS
NOTIFIES
TRIGGERS_WORKFLOW
CALLS
HAS_API_EQUIVALENT
HAS_CLI_EQUIVALENT
AUDITED_BY
RECOVERED_BY
DISPLAYED_IN
CONFIGURED_IN
INSTALLED_ON
AUTHORIZED_BY
SCOPED_TO
SYNCHRONIZES_WITH
```

Use generic `RELATED_TO` only as a last resort.

---

## 56. Referential and bidirectional integrity

Every identifier reference MUST resolve to a canonical record.

Validate inverse/paired semantics where applicable, e.g.:

```text
A CONTAINS B
↔
B PART_OF A
```

State transitions, permissions, routes, events and recovery references MUST NOT be orphaned.

Where useful, capture cardinality:

```text
1:1
1:N
N:1
N:N
```

---

## 57. Canonical identifier system

Use stable semantic identifiers independent of mutable UI labels. Example pattern only:

```text
GH-ENTITY-REPOSITORY
GH-FEATURE-PULL-REQUESTS
GH-ACTION-MERGE-PR
GH-SURFACE-REPO-SETTINGS
GH-EVENT-PR-MERGED
```

Maintain an Alias Registry for UI/API/CLI/legacy wording.

---

# PART X — COVERAGE, ADVERSARIAL REVIEW AND ASSURANCE

## 58. Coverage model

Do not reduce coverage to one synthetic score. Track independently:

```text
Concept Coverage
Product/Feature Coverage
Surface Coverage
Navigation Coverage
Settings/Control Coverage
Action Coverage
Route Coverage
Role/Permission Coverage
Policy Coverage
Plan/Entitlement Coverage
Client Coverage
State Coverage
Lifecycle Coverage
API/CLI/Webhook Coverage
Event/Notification Coverage
Security Coverage
Audit Coverage
Failure Coverage
Recovery Coverage
Evidence Coverage
```

Coverage states:

```text
COVERED
PARTIALLY_COVERED
NOT_APPLICABLE
INACCESSIBLE
UNVERIFIED
GAP
```

---

## 59. Gap severity

```text
BLOCKER — prevents structural/integrity claim
MAJOR   — missing material family, lifecycle, security boundary or recovery path
MINOR   — missing detail that does not alter architecture
INFO    — non-blocking observation
```

Every gap record includes ID, description, evidence, severity, impact, remediation and blocking status.

---

## 60. Adversarial personas and boundary testing

Challenge the architecture from materially distinct perspectives, such as:

```text
anonymous visitor
contributor
maintainer
repository admin
organization owner
security/admin role
enterprise administrator
GitHub App
Actions workflow
external integration
mobile user
CLI-only user
API-only client
threat/attacker perspective
```

Test boundaries including:

```text
Git ↔ GitHub
repository ↔ organization
organization ↔ enterprise
UI ↔ API/CLI
user ↔ GitHub App
workflow ↔ runner
secret ↔ consumer
release ↔ package
notification ↔ event
GitHub ↔ external provider
```

Perform a dedicated rare/edge-path pass for transfer, archive/unarchive, branch/tag/release deletion, workflow disable/cancel, permission downgrade, App uninstall, credential revocation, failed webhook/integration, security alert dismissal/reopen, migration and recovery scenarios that current evidence supports.

---

## 61. Security bypass analysis

For every material governance/security control ask:

```text
What does it protect?
Who can configure it?
Can it be bypassed?
Who can bypass it?
Is the bypass audited?
Is it a legitimate exception path?
What is the blast radius?
What recovery exists?
```

---

## 62. SAT-MAX

Material novelty includes a newly discovered:

- domain/family/class;
- necessary conceptual distinction;
- structural relationship that changes interpretation;
- lifecycle stage;
- permission/policy dimension;
- security/trust boundary;
- failure class;
- recovery mechanism;
- materially different interaction surface/context;
- evidence that invalidates a prior decision.

Aliases, microvariants, cosmetic UI rearrangement, extra examples, rewordings or confirmatory evidence are not material by themselves.

Final rediscovery sequence SHOULD include:

```text
concept rediscovery
navigation rediscovery
surface/settings/control rediscovery
action/route rediscovery
role/permission/policy rediscovery
plan/client/state rediscovery
API/CLI/webhook rediscovery
event/notification rediscovery
security/integration rediscovery
failure/recovery rediscovery
temporal/historical rediscovery
independent adversarial pass
```

SAT-MAX passes only after **two consecutive zero-material-novelty passes**, with at least one independent/adversarial pass, blockers = 0 and unresolved material gaps = 0.

---

## 63. Definition of material completeness

Do not claim metaphysical or future-proof universal completeness.

Canonical meaning of “100%” for this workstream:

> **100% means demonstrated material coverage of all canonical candidates identifiable within the defined scope, context matrix, evidence horizon and accessible surfaces, with zero known material gaps and SAT-MAX satisfied.**

---

# PART XI — CANONICAL REGISTRIES AND DERIVED VIEWS

## 64. Canonical registries

Maintain, when material, separate canonical registries for:

```text
Candidate Registry
Concept / Terminology Registry
Entity Registry
Product Registry
Feature Registry
Surface Registry
Occurrence Registry
Navigation Registry
Menu Registry
Tab / Sidebar Registry
Settings Registry
Control Registry
Action Registry
Route Registry
State / Transition Registry
Role Registry
Permission Registry
Policy Registry
Plan / Entitlement Registry
Client / Device Registry
Event Registry
Webhook Registry
Notification Registry
Integration Registry
Security Control Registry
Audit / Observability Registry
Limit / Retention Registry
Failure Registry
Error Surface Registry
Recovery Registry
Journey Registry
Lifecycle Registry
Evidence Registry
Contradiction Registry
Unknown-Space Registry
Exclusion Registry
Unresolved Registry
```

Avoid physical files for registries that can be coherently merged without loss; logical separation does not require one-file-per-concept.

---

## 65. Derived views

The canonical registries are the SSOT. Produce views from them rather than duplicating truth:

```text
Taxonomies
Sitemap / information architecture
Navigation graph
Settings tree
Permission/policy matrix
Lifecycle diagrams
Security view
API/CLI parity view
Client parity view
Notification/event view
Failure/recovery view
Repository blueprint
Conformance matrix
```

---

# PART XII — APPLY TO `flawless-ftxp`

## 66. Applicability engine

Filter the global reference architecture into repository-relevant capabilities:

```text
GIT + GITHUB UNIVERSE SSOT
↓ applicability filter
REPOSITORY-RELEVANT CAPABILITIES
↓ target profile
flawless-ftxp
```

Each candidate receives one status:

```text
REQUIRED
RECOMMENDED
OPTIONAL
CONDITIONAL
NOT_APPLICABLE
EXCLUDED
```

Include reason, benefit, cost, risk and dependency.

---

## 67. Current-versus-reference audit

Classify every applicable item in `flawless-ftxp` as:

```text
PRESENT_CORRECT
PRESENT_PARTIAL
PRESENT_REDUNDANT
PRESENT_INCORRECT
MISSING_REQUIRED
MISSING_RECOMMENDED
OPTIONAL
NOT_APPLICABLE
```

Produce gap families:

```text
GIT_GAPS
GITHUB_GAPS
REPOSITORY_ARCHITECTURE_GAPS
LIFECYCLE_GAPS
SECURITY_GAPS
GOVERNANCE_GAPS
AUTOMATION_GAPS
RELEASE_GAPS
RECOVERY_GAPS
DOCUMENTATION_GAPS
VALIDATION_GAPS
```

---

## 68. Minimum sufficient repository architecture

Before adding any feature/artifact ask:

```text
Is there a material gap?
Does this solve it?
Is it the minimum sufficient solution?
Does it duplicate another SSOT/layer?
Can it be derived instead?
Does maintenance burden remain justified?
```

Exclude candidates that fail this test.

---

## 69. Change impact and classification

Before mutation build an impact graph:

```text
CHANGE
→ affected files/settings
→ affected concepts/registries
→ affected validations
→ affected version
→ affected documentation
→ affected release/baseline
```

Classify change:

```text
EDITORIAL
CORRECTIVE
ADDITIVE
STRUCTURAL
BEHAVIORAL
BREAKING
SECURITY
DEPRECATION
REMOVAL
```

Map classification to version impact, reopening trigger, validation scope and review requirement.

---

## 70. Mutation rule

When repository mutation is authorized:

```text
DISCOVER
→ VERIFY
→ CLASSIFY
→ JUSTIFY
→ PLAN
→ CHANGE
→ VALIDATE
→ REGRESS
```

Never delete an artifact merely because a cleaner architecture is imaginable; demonstrate redundancy, incorrectness or supersession first.

Group changes into atomic, logical commits.

---

# PART XIII — ASSURANCE AND FREEZE

## 71. FTXP quality gates

Preserve G0–G12:

```text
G0 Scope
G1 Terminology
G2 Candidate Coverage
G3 Canonicalization
G4 Deduplication
G5 Hierarchy
G6 Facet Orthogonality
G7 Relationships
G8 Evidence
G9 Gap Analysis
G10 Adversarial Review
G11 SAT-MAX
G12 Regression
```

---

## 72. Repository assurance gates

Maintain RQ0–RQ13 and add the lifecycle-specific gates:

### RQ14 — Git Lifecycle Integrity

PASS only when init/configuration, branch, commit, remote, integration, conflict handling, tag/version, recovery, maintenance and archive lifecycle are sufficiently represented and validated.

### RQ15 — GitHub Repository Lifecycle Integrity

PASS only when the actual repository process can demonstrate:

```text
change request
→ branch
→ change
→ commit
→ push
→ PR
→ CI
→ review/approval
→ merge
→ post-merge validation
→ version
→ tag
→ release
→ maintenance
→ recovery
```

### RQ16 — Recovery & Reconstructability

PASS only when every frozen baseline can be unambiguously reconstructed from version-control/release evidence.

### RQ17 — Governance & Security Integrity

PASS only when material changes cannot unintentionally bypass the defined controls and legitimate bypass/exception paths are understood and auditable.

---

## 73. Conformance model

```yaml
conformance:
  requirement_id:
  applicability:
  expected:
  observed:
  evidence:
  status:
```

Statuses:

```text
PASS
PASS_WITH_FINDING
FAIL
NOT_APPLICABLE
BLOCKED
UNVERIFIED
```

---

## 74. Reference test suite

Use representative cases rather than pretending to simulate all GitHub contexts. Include where applicable:

```text
empty repository
public repository
private repository
fork
archived repository
protected/ruleset-governed main
PR lifecycle
Actions workflow
release lifecycle
security finding
GitHub App/integration
permission-denied path
failed workflow
revert/recovery
historical-baseline reconstruction
```

---

## 75. Freeze manifest

A final freeze SHOULD emit an unambiguous manifest:

```yaml
freeze:
  repository:
  default_branch:
  commit_sha:
  protocol_version:
  repository_version:
  tag:
  release:
  validation_run:
  evidence_horizon:
  gates:
  blockers:
  unresolved_majors:
  saturation:
  timestamp:
```

---

## 76. Freeze criteria

Do not declare repository freeze unless:

```text
FTXP applicable G0–G12 = PASS
AND repository applicable RQ0–RQ17 = PASS
AND SAT-MAX = PASS
AND repository regression = PASS
AND Git lifecycle = PASS
AND GitHub repository lifecycle = PASS
AND reconstructability = PASS
AND governance/security = PASS
AND blockers = 0
AND unresolved MAJOR = 0
```

---

## 77. Stop condition

Stop expansion when successive independent passes discover no new material domains, entity families, feature families, surfaces, actions, facets, lifecycle stages, security boundaries, permission dimensions, failure classes or recovery mechanisms; no materially independent evidence source is likely to alter the model; all applicable gates pass; and the two-pass SAT-MAX condition is satisfied.

Do not continue merely because more words can be generated.

---

# PART XIV — OUTPUT PACKAGE

## 78. Canonical execution outputs

Produce outputs in a logically ordered package. The following is a canonical logical inventory; physical consolidation is allowed when it avoids duplication without reducing traceability.

```text
00 Execution Header
01 Executive Map
02 Scope & Boundaries
03 Evidence Horizon
04 Terminology Registry
05 Git Canonical Architecture
06 Git Object / Ref Model
07 Git Operational Model
08 Git Full Lifecycle
09 Git Failure & Recovery Model
10 GitHub Canonical Architecture
11 GitHub Product Registry
12 GitHub Entity Registry
13 GitHub Feature Registry
14 GitHub Platform Taxonomy
15 GitHub Facet Registry
16 GitHub Relationship Model
17 Global Information Architecture
18 Global Navigation Map
19 Menu / Submenu Registry
20 Tab / Sidebar Registry
21 Surface Registry
22 Occurrence Registry
23 Settings Taxonomy
24 Control Registry / Matrix
25 Action Registry
26 Route Registry
27 Search / Command Architecture
28 Journey Registry
29 State / Transition Registry
30 GitHub Repository Architecture
31 GitHub Repository Full Lifecycle
32 Identity & Authentication Architecture
33 Role / Permission Matrix
34 Policy / Inheritance Architecture
35 Plan / Entitlement / Deployment Matrix
36 Client / Device Capability Matrix
37 API / CLI / Git / Webhook Parity Matrix
38 Automation / Actions Architecture
39 Event Registry
40 Webhook Registry
41 Notification Architecture
42 Apps & Integrations Architecture
43 Security Architecture
44 Trust Boundary Model
45 Credential / Secret Lifecycle
46 Audit & Observability Architecture
47 Limit / Retention Architecture
48 Data / Artifact Lifecycle
49 Migration / Transfer Architecture
50 Failure Registry
51 Error Surface Registry
52 Failure Propagation Graph
53 Recovery Registry
54 Destructive Operations Matrix
55 Maintenance / EOL Model
56 Historical / Preview / Deprecated Registry
57 Evidence Ledger
58 Unknown-Space Registry
59 Contradiction Registry
60 Coverage Accounting
61 Gap Register
62 Adversarial Audit
63 SAT-MAX Report
64 Regression Report
65 Repository Applicability Matrix
66 Current `flawless-ftxp` Inventory
67 Reference-vs-Current Matrix
68 Remediation Plan
69 Conformance Report
70 Repository Assurance Report
71 Target Architecture
72 Implementation Plan
73 Release Readiness Report
74 Freeze Readiness Report
75 Freeze Manifest
```

---

## 79. Pre-mutation execution plan

Before modifying the target repository, enumerate each proposed change with:

```text
ID
FILE / SETTING / POLICY
CURRENT STATE
TARGET STATE
WHY
SOURCE / EVIDENCE
RISK
DEPENDENCIES
VALIDATION
ROLLBACK
VERSION IMPACT
REOPENING TRIGGER
COMMIT GROUP
```

---

# PART XV — MASTER PIPELINE

## 80. Full end-to-end pipeline

```text
BASELINE RECOVERY
→ EVIDENCE HORIZON
→ SCOPE LOCK
→ SOURCE DISCOVERY
→ DOMAIN DISCOVERY
→ ENTITY DISCOVERY
→ PRODUCT DISCOVERY
→ FEATURE DISCOVERY
→ SURFACE DISCOVERY
→ NAVIGATION DISCOVERY
→ CONTROL DISCOVERY
→ ACTION DISCOVERY
→ ROUTE DISCOVERY
→ STATE DISCOVERY
→ ROLE / PERMISSION DISCOVERY
→ POLICY / PLAN / ENTITLEMENT DISCOVERY
→ CLIENT / DEVICE DISCOVERY
→ API / CLI / GIT / WEBHOOK DISCOVERY
→ EVENT DISCOVERY
→ NOTIFICATION DISCOVERY
→ AUTOMATION DISCOVERY
→ SECURITY / TRUST DISCOVERY
→ FAILURE / ERROR DISCOVERY
→ RECOVERY DISCOVERY
→ RETENTION / MIGRATION / LIMIT DISCOVERY
→ HISTORICAL / TEMPORAL DISCOVERY
→ CANDIDATE REGISTRY
→ NORMALIZATION
→ CANONICALIZATION
→ CONCEPT TYPING
→ DEDUPLICATION
→ PRIMARY TAXONOMIES
→ FACETING
→ RELATIONSHIP MODELING
→ STATE MACHINES
→ LIFECYCLE MODELING
→ CONTEXT MATRIX
→ PARITY MATRICES
→ EVIDENCE RESOLUTION
→ CONTRADICTION RESOLUTION
→ COVERAGE ACCOUNTING
→ GAP ANALYSIS
→ TOP-DOWN REDISCOVERY
→ BOTTOM-UP REDISCOVERY
→ HORIZONTAL REDISCOVERY
→ CROSS-CUTTING REDISCOVERY
→ ADVERSARIAL REDISCOVERY
→ SAT-MAX PASS 1
→ INDEPENDENT REDISCOVERY
→ SAT-MAX PASS 2
→ REGRESSION
→ REFERENCE ARCHITECTURE BASELINE
→ APPLICABILITY FILTER
→ flawless-ftxp AUDIT
→ REMEDIATION PLAN
→ AUTHORIZED IMPLEMENTATION
→ VALIDATION
→ E2E GIT/GITHUB LIFECYCLE TEST
→ RELEASE READINESS
→ FREEZE MANIFEST
→ FREEZE
```

---

## 81. Change-detection after freeze

Do not continuously rebuild the entire model. After a frozen baseline, process change as deltas triggered by materially relevant evidence such as GitHub changelog/documentation/API/CLI/security changes, new product capabilities, observed contradictions or new repository requirements.

```text
CURRENT BASELINE
→ DELTA DISCOVERY
→ MATERIALITY CLASSIFICATION
→ TARGETED REOPENING IF REQUIRED
→ REGRESSION
→ NEW BASELINE
```

---

## 82. Definition of done

The work is DONE only when the required model, context, lifecycle, evidence and assurance dimensions pass their applicable gates. Producing a large document is not a completion criterion.

Required logical result:

```text
Canonical Model ............... PASS
Candidate Coverage ............ PASS
Deduplication ................. PASS
Facet Orthogonality ........... PASS
Relationship Integrity ........ PASS
Context Coverage .............. PASS
Lifecycle Coverage ............ PASS
Security / Trust Coverage ..... PASS
Failure Coverage .............. PASS
Recovery Coverage ............. PASS
Evidence Coverage ............. PASS
Adversarial Review ............ PASS
Regression .................... PASS
SAT-MAX ....................... PASS
```

---

## 83. Canonical closure statement

The strongest defensible completion claim is:

> **The Git + GitHub Full-Spectrum Reference Architecture is materially complete within its declared scope and evidence horizon, all known material candidates are canonicalized and accounted for, all applicable assurance gates pass, no BLOCKER or unresolved MAJOR remains, and SAT-MAX has been satisfied by two consecutive zero-material-novelty passes including an independent adversarial pass.**

No stronger universal/future-proof completeness claim may be made without evidence that supports it.
