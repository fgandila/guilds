from pathlib import Path

HOME = Path().home()
DEFAULT_WORKSPACE = Path(__file__).parent

# ------------ For normal operation, modify below ------------ #
# Used net
DEFAULT_PROXY = "https://proxy-shadowfork-three.elrond.ro"                     # Proxy to be used for ALL operations
DEFAULT_API = "https://express-api-shadowfork-three.elrond.ro"                           # API to be used for ALL operations
GRAPHQL = 'https://graph.xexchange.com/graphql'                              # GraphQL service; only needed for the upgrader scripts
HISTORY_PROXY = ""                                                          # Proxy to be used for history operations; not used for the moment
# TODO: try to override the default issue token price with testnet definition to tidy code up
DEFAULT_ISSUE_TOKEN_PRICE = 50000000000000000                               # 0.05 EGLD - change only if different setup on nets

# Operation wallets
DEFAULT_ACCOUNTS = DEFAULT_WORKSPACE.absolute() / "defi-wallet.pem"       # Accounts to be used for user operations
DEFAULT_OWNER = DEFAULT_WORKSPACE.absolute() / "defi-wallet.pem"         # DEX owner address
DEFAULT_ADMIN = DEFAULT_WORKSPACE.absolute() / "defi-wallet.pem"         # DEX admin address
DEX_OWNER_ADDRESS = "erd1ss6u80ruas2phpmr82r42xnkd6rxy40g9jl69frppl4qez9w2jpsqj8x97"  # Only needed for shadowforks
DEX_ADMIN_ADDRESS = "erd1ss6u80ruas2phpmr82r42xnkd6rxy40g9jl69frppl4qez9w2jpsqj8x97"  # Only needed for shadowforks

# Used DEX deploy configuration
DEFAULT_CONFIG_SAVE_PATH = DEFAULT_WORKSPACE.absolute() / "deploy" / "configs-mainnet"   # Deploy configuration folder
DEPLOY_STRUCTURE_JSON = DEFAULT_CONFIG_SAVE_PATH / "deploy_structure.json"  # Deploy structure - change only if needed

FORCE_CONTINUE_PROMPT = False                                               # Force continue prompt for all operations

# DEX contract bytecode paths
EGLD_WRAP_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "egld-wrap.wasm"
LOCKED_ASSET_FACTORY_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "factory_upgrade.wasm"
SIMPLE_LOCK_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "simple-lock-legacy.wasm"
ROUTER_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "dex" / "router" / "output" / "router.wasm"
PROXY_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "proxy_dex_upgrade.wasm"
PROXY_V2_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "proxy_dex.wasm"
PAIR_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "pair.wasm"
FARM_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "dex" / "farm" / "output" / "farm.wasm"
FARM_LOCKED_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "dex" / "farm_with_lock" / "output" / "farm_with_lock.wasm"
FARM_COMMUNITY_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "dex" / "farm_with_community_rewards" / "output" / "farm_with_community_rewards.wasm"
PRICE_DISCOVERY_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "dex" / "price-discovery" / "output" / "price-discovery.wasm"
STAKING_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "farm-staking" / "farm-staking" / "output" / "farm-staking.wasm"
STAKING_V2_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "farm-staking.wasm"
STAKING_V3_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "farm-staking.wasm"
STAKING_PROXY_BYTECODE_PATH = Path().home() / "dev" / "dex" / "sc-dex-rs" / "farm-staking" / "farm-staking-proxy" / "output" / "farm-staking-proxy.wasm"
STAKING_PROXY_V2_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "farm-staking-proxy.wasm"
STAKING_PROXY_V3_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "farm-staking-proxy.wasm"
SIMPLE_LOCK_ENERGY_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "energy-factory.wasm"
UNSTAKER_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "token-unstake.wasm"
FEES_COLLECTOR_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "fees-collector.wasm"
ROUTER_V2_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "router.wasm"
PAIR_V2_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "pair.wasm"
PAIR_VIEW_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm" / "safe-price-view.wasm"
FARM_DEPLOYER_BYTECODE_PATH = Path().home() / "projects" / "dex" / "dex-v2" / "dexv2-rs" / "proxy-deployer.wasm"
FARM_V2_BYTECODE_PATH = DEFAULT_WORKSPACE.home() / "projects" / "dex" / "dex-v2" / "sc-dex-rs" / "output-docker" / "farm-with-locked-rewards" / "farm-with-locked-rewards.wasm"
FARM_V3_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "farm-with-locked-rewards.wasm"
GOVERNANCE_BYTECODE_PATH = Path().home() / "projects" / "dex" / "dex-v2" / "sc-dex-rs" / "energy-integration" / "governance-v2" / "output" / "governance-v2.wasm"
POSITION_CREATOR_BYTECODE_PATH = Path().home() / "MultiversX/mx-exchange-tools-sc/auto-pos-creator/output" / "auto-pos-creator.wasm"
ESCROW_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "lkmex-transfer.wasm"
LK_WRAP_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "locked-token-wrapper.wasm"
DUMMY_PROXY_BYTECODE_PATH = DEFAULT_WORKSPACE.absolute() / "wasm-v3" / "dummy-proxy.wasm"

# ------------ Generic configuration below; Modify only in case of framework changes ------------ #
TOKENS_CONTRACT_ADDRESS = "erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzllls8a5w6u"
SF_CONTROL_ADDRESS = "erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqplllst77y4l"
ZERO_CONTRACT_ADDRESS = "erd1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq6gq4hu"

# Upgrader scripts output directory
UPGRADER_OUTPUT_FOLDER = DEFAULT_CONFIG_SAVE_PATH / "upgrader_outputs"

DEFAULT_GAS_BASE_LIMIT_ISSUE = 60000000
DEFAULT_TOKEN_PREFIX = "TDEX"     # limit yourself to max 6 chars to allow automatic ticker build
DEFAULT_TOKEN_SUPPLY_EXP = 27       # supply to be minted in exponents of 10
DEFAULT_TOKEN_DECIMALS = 18         # decimals on minted tokens in exponents of 10
DEFAULT_MINT_VALUE = 1  # EGLD      # TODO: don't go sub-unitary cause headaches occur. just don't be cheap for now...

CROSS_SHARD_DELAY = 60
INTRA_SHARD_DELAY = 10

EGLD_WRAPS = "egld_wraps"
LOCKED_ASSETS = "locked_assets"
PROXIES = "proxies"
PROXIES_V2 = "proxies_v2"
SIMPLE_LOCKS = "simple_locks"
SIMPLE_LOCKS_ENERGY = "simple_locks_energy"
UNSTAKERS = "unstakers"
ROUTER = "router"
ROUTER_V2 = "router_v2"
PAIRS = "pairs"
PAIRS_V2 = "pairs_v2"
PAIRS_VIEW = "pairs_view"
PROXY_DEPLOYERS = "proxy_deployers"
FARMS_V2 = "farms_boosted"
FARMS_COMMUNITY = "farms_community"
FARMS_UNLOCKED = "farms_unlocked"
FARMS_LOCKED = "farms_locked"
PRICE_DISCOVERIES = "price_discoveries"
STAKINGS = "stakings"
STAKINGS_V2 = "stakings_v2"
STAKINGS_BOOSTED = "stakings_boosted"
METASTAKINGS = "metastakings"
METASTAKINGS_V2 = "metastakings_v2"
METASTAKINGS_BOOSTED = "metastakings_boosted"
FEES_COLLECTORS = "fees_collectors"
GOVERNANCES = "governances"
POSITION_CREATOR = "position_creator"
ESCROWS = "escrows"
LK_WRAPS = "lk_wraps"
DUMMY_PROXY = "dummy"


def get_default_tokens_file():
    return DEFAULT_CONFIG_SAVE_PATH / "tokens.json"


def get_default_log_file():
    return DEFAULT_WORKSPACE / "logs" / "trace.log"
