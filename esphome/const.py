"""Constants used by esphome."""

MAJOR_VERSION = 1
MINOR_VERSION = 13
PATCH_VERSION = '0-dev'
__short_version__ = '{}.{}'.format(MAJOR_VERSION, MINOR_VERSION)
__version__ = '{}.{}'.format(__short_version__, PATCH_VERSION)
ESPHOME_CORE_VERSION = 'dev'

ESP_PLATFORM_ESP32 = 'ESP32'
ESP_PLATFORM_ESP8266 = 'ESP8266'
ESP_PLATFORMS = [ESP_PLATFORM_ESP32, ESP_PLATFORM_ESP8266]

APB_CLOCK_FREQ = 80000000

CONF_ESPHOME = 'esphome'
CONF_NAME = 'name'
CONF_PLATFORM = 'platform'
CONF_BOARD = 'board'
CONF_ESPHOME_CORE_VERSION = 'esphome_core_version'
CONF_USE_CUSTOM_CODE = 'use_custom_code'
CONF_ARDUINO_VERSION = 'arduino_version'
CONF_LOCAL = 'local'
CONF_REPOSITORY = 'repository'
CONF_COMMIT = 'commit'
CONF_SERVICES = 'services'
CONF_TAG = 'tag'
CONF_BRANCH = 'branch'
CONF_LOGGER = 'logger'
CONF_WIFI = 'wifi'
CONF_SSID = 'ssid'
CONF_IP_ADDRESS = 'ip_address'
CONF_BSSID = 'bssid'
CONF_PASSWORD = 'password'
CONF_MANUAL_IP = 'manual_ip'
CONF_STATIC_IP = 'static_ip'
CONF_GATEWAY = 'gateway'
CONF_SUBNET = 'subnet'
CONF_OTA = 'ota'
CONF_MQTT = 'mqtt'
CONF_BROKER = 'broker'
CONF_USERNAME = 'username'
CONF_MIN_LEVEL = 'min_level'
CONF_IDLE_LEVEL = 'idle_level'
CONF_MAX_LEVEL = 'max_level'
CONF_POWER_SUPPLY = 'power_supply'
CONF_ID = 'id'
CONF_MQTT_ID = 'mqtt_id'
CONF_SENSOR_ID = 'sensor_id'
CONF_TRIGGER_ID = 'trigger_id'
CONF_ACTION_ID = 'action_id'
CONF_CONDITION_ID = 'condition_id'
CONF_MAKE_ID = 'make_id'
CONF_AUTOMATION_ID = 'automation_id'
CONF_DELAY = 'delay'
CONF_PIN = 'pin'
CONF_NUMBER = 'number'
CONF_INVERTED = 'inverted'
CONF_I2C = 'i2c'
CONF_SDA = 'sda'
CONF_SCL = 'scl'
CONF_FREQUENCY = 'frequency'
CONF_PCA9685 = 'pca9685'
CONF_PCA9685_ID = 'pca9685_id'
CONF_OUTPUT = 'output'
CONF_CHANNEL = 'channel'
CONF_CHANNELS = 'channels'
CONF_LIGHT = 'light'
CONF_RED = 'red'
CONF_GREEN = 'green'
CONF_BLUE = 'blue'
CONF_SENSOR = 'sensor'
CONF_TEMPERATURE = 'temperature'
CONF_HUMIDITY = 'humidity'
CONF_MODEL = 'model'
CONF_BINARY_SENSOR = 'binary_sensor'
CONF_DEVICE_CLASS = 'device_class'
CONF_GPIO = 'gpio'
CONF_DHT = 'dht'
CONF_SAFE_MODE = 'safe_mode'
CONF_MODE = 'mode'
CONF_GAMMA_CORRECT = 'gamma_correct'
CONF_RETAIN = 'retain'
CONF_DISCOVERY = 'discovery'
CONF_DISCOVERY_PREFIX = 'discovery_prefix'
CONF_STATE_TOPIC = 'state_topic'
CONF_COMMAND_TOPIC = 'command_topic'
CONF_AVAILABILITY = 'availability'
CONF_TOPIC = 'topic'
CONF_PAYLOAD_AVAILABLE = 'payload_available'
CONF_PAYLOAD_NOT_AVAILABLE = 'payload_not_available'
CONF_DEFAULT_TRANSITION_LENGTH = 'default_transition_length'
CONF_TRANSITION_LENGTH = 'transition_length'
CONF_FLASH_LENGTH = 'flash_length'
CONF_BRIGHTNESS = 'brightness'
CONF_EFFECT = 'effect'
CONF_ABOVE = 'above'
CONF_BELOW = 'below'
CONF_ON = 'on'
CONF_IF = 'if'
CONF_WHILE = 'while'
CONF_WAIT_UNTIL = 'wait_until'
CONF_THEN = 'then'
CONF_BINARY = 'binary'
CONF_WHITE = 'white'
CONF_RGBW = 'rgbw'
CONF_MAX_POWER = 'max_power'
CONF_BIT_DEPTH = 'bit_depth'
CONF_BAUD_RATE = 'baud_rate'
CONF_LOG_TOPIC = 'log_topic'
CONF_TX_BUFFER_SIZE = 'tx_buffer_size'
CONF_LEVEL = 'level'
CONF_LOGS = 'logs'
CONF_PORT = 'port'
CONF_WILL_MESSAGE = 'will_message'
CONF_BIRTH_MESSAGE = 'birth_message'
CONF_SHUTDOWN_MESSAGE = 'shutdown_message'
CONF_PAYLOAD = 'payload'
CONF_QOS = 'qos'
CONF_DISCOVERY_RETAIN = 'discovery_retain'
CONF_TOPIC_PREFIX = 'topic_prefix'
CONF_PHASE_BALANCER = 'phase_balancer'
CONF_ADDRESS = 'address'
CONF_ENABLE_TIME = 'enable_time'
CONF_KEEP_ON_TIME = 'keep_on_time'
CONF_DNS1 = 'dns1'
CONF_DNS2 = 'dns2'
CONF_UNIT_OF_MEASUREMENT = 'unit_of_measurement'
CONF_ICON = 'icon'
CONF_ACCURACY_DECIMALS = 'accuracy_decimals'
CONF_EXPIRE_AFTER = 'expire_after'
CONF_FILTERS = 'filters'
CONF_OFFSET = 'offset'
CONF_MULTIPLY = 'multiply'
CONF_FILTER_OUT = 'filter_out'
CONF_SLIDING_WINDOW_MOVING_AVERAGE = 'sliding_window_moving_average'
CONF_EXPONENTIAL_MOVING_AVERAGE = 'exponential_moving_average'
CONF_WINDOW_SIZE = 'window_size'
CONF_SEND_EVERY = 'send_every'
CONF_ALPHA = 'alpha'
CONF_LAMBDA = 'lambda'
CONF_THROTTLE = 'throttle'
CONF_DELTA = 'delta'
CONF_OR = 'or'
CONF_CALIBRATE_LINEAR = 'calibrate_linear'
CONF_AND = 'and'
CONF_RANGE = 'range'
CONF_UNIQUE = 'unique'
CONF_HEARTBEAT = 'heartbeat'
CONF_DEBOUNCE = 'debounce'
CONF_UPDATE_INTERVAL = 'update_interval'
CONF_PULL_MODE = 'pull_mode'
CONF_COUNT_MODE = 'count_mode'
CONF_RISING_EDGE = 'rising_edge'
CONF_FALLING_EDGE = 'falling_edge'
CONF_INTERNAL_FILTER = 'internal_filter'
CONF_DALLAS_ID = 'dallas_id'
CONF_INDEX = 'index'
CONF_RESOLUTION = 'resolution'
CONF_ATTENUATION = 'attenuation'
CONF_PRESSURE = 'pressure'
CONF_TRIGGER_PIN = 'trigger_pin'
CONF_ECHO_PIN = 'echo_pin'
CONF_TIMEOUT = 'timeout'
CONF_CARRIER_DUTY_PERCENT = 'carrier_duty_percent'
CONF_NEC = 'nec'
CONF_COMMAND = 'command'
CONF_DATA = 'data'
CONF_NBITS = 'nbits'
CONF_JVC = 'jvc'
CONF_RC5 = 'rc5'
CONF_LG = 'lg'
CONF_SAMSUNG = 'samsung'
CONF_SONY = 'sony'
CONF_PANASONIC = 'panasonic'
CONF_REPEAT = 'repeat'
CONF_TIMES = 'times'
CONF_WAIT_TIME = 'wait_time'
CONF_OSCILLATION_OUTPUT = 'oscillation_output'
CONF_SPEED = 'speed'
CONF_OSCILLATION_STATE_TOPIC = 'oscillation_state_topic'
CONF_OSCILLATION_COMMAND_TOPIC = 'oscillation_command_topic'
CONF_OSCILLATING = 'oscillating'
CONF_SPEED_STATE_TOPIC = 'speed_state_topic'
CONF_SPEED_COMMAND_TOPIC = 'speed_command_topic'
CONF_LOW = 'low'
CONF_MEDIUM = 'medium'
CONF_HIGH = 'high'
CONF_NUM_ATTEMPTS = 'num_attempts'
CONF_CLIENT_ID = 'client_id'
CONF_RAW = 'raw'
CONF_CARRIER_FREQUENCY = 'carrier_frequency'
CONF_RATE = 'rate'
CONF_ADS1115_ID = 'ads1115_id'
CONF_MULTIPLEXER = 'multiplexer'
CONF_GAIN = 'gain'
CONF_SLEEP_DURATION = 'sleep_duration'
CONF_WAKEUP_PIN = 'wakeup_pin'
CONF_RUN_CYCLES = 'run_cycles'
CONF_RUN_DURATION = 'run_duration'
CONF_AP = 'ap'
CONF_CSS_URL = 'css_url'
CONF_JS_URL = 'js_url'
CONF_SSL_FINGERPRINTS = 'ssl_fingerprints'
CONF_PCF8574 = 'pcf8574'
CONF_MCP23017 = 'mcp23017'
CONF_PCF8575 = 'pcf8575'
CONF_SCAN = 'scan'
CONF_KEEPALIVE = 'keepalive'
CONF_INTEGRATION_TIME = 'integration_time'
CONF_RECEIVE_TIMEOUT = 'receive_timeout'
CONF_SCAN_INTERVAL = 'scan_interval'
CONF_MAC_ADDRESS = 'mac_address'
CONF_SETUP_MODE = 'setup_mode'
CONF_SETUP_PRIORITY = 'setup_priority'
CONF_IIR_FILTER = 'iir_filter'
CONF_MEASUREMENT_DURATION = 'measurement_duration'
CONF_LOW_VOLTAGE_REFERENCE = 'low_voltage_reference'
CONF_HIGH_VOLTAGE_REFERENCE = 'high_voltage_reference'
CONF_VOLTAGE_ATTENUATION = 'voltage_attenuation'
CONF_THRESHOLD = 'threshold'
CONF_OVERSAMPLING = 'oversampling'
CONF_GAS_RESISTANCE = 'gas_resistance'
CONF_NUM_LEDS = 'num_leds'
CONF_MAX_REFRESH_RATE = 'max_refresh_rate'
CONF_CHIPSET = 'chipset'
CONF_DATA_PIN = 'data_pin'
CONF_CLOCK_PIN = 'clock_pin'
CONF_RGB_ORDER = 'rgb_order'
CONF_ACCURACY = 'accuracy'
CONF_BOARD_FLASH_MODE = 'board_flash_mode'
CONF_ON_PRESS = 'on_press'
CONF_ON_RELEASE = 'on_release'
CONF_ON_STATE = 'on_state'
CONF_ON_CLICK = 'on_click'
CONF_ON_DOUBLE_CLICK = 'on_double_click'
CONF_ON_MULTI_CLICK = 'on_multi_click'
CONF_MIN_LENGTH = 'min_length'
CONF_MAX_LENGTH = 'max_length'
CONF_ON_VALUE = 'on_value'
CONF_ON_RAW_VALUE = 'on_raw_value'
CONF_ON_VALUE_RANGE = 'on_value_range'
CONF_ON_MESSAGE = 'on_message'
CONF_CS_PIN = 'cs_pin'
CONF_CLK_PIN = 'clk_pin'
CONF_MISO_PIN = 'miso_pin'
CONF_MOSI_PIN = 'mosi_pin'
CONF_TURN_ON_ACTION = 'turn_on_action'
CONF_TURN_OFF_ACTION = 'turn_off_action'
CONF_OPEN_ACTION = 'open_action'
CONF_CLOSE_ACTION = 'close_action'
CONF_STOP_ACTION = 'stop_action'
CONF_DOMAIN = 'domain'
CONF_OPTIMISTIC = 'optimistic'
CONF_ASSUMED_STATE = 'assumed_state'
CONF_ON_BOOT = 'on_boot'
CONF_ON_SHUTDOWN = 'on_shutdown'
CONF_PRIORITY = 'priority'
CONF_DUMP = 'dump'
CONF_BUFFER_SIZE = 'buffer_size'
CONF_TOLERANCE = 'tolerance'
CONF_FILTER = 'filter'
CONF_IDLE = 'idle'
CONF_NETWORKS = 'networks'
CONF_INTERNAL = 'internal'
CONF_BUILD_PATH = 'build_path'
CONF_PLATFORMIO_OPTIONS = 'platformio_options'
CONF_REBOOT_TIMEOUT = 'reboot_timeout'
CONF_INVERT = 'invert'
CONF_DELAYED_ON = 'delayed_on'
CONF_DELAYED_OFF = 'delayed_off'
CONF_UUID = 'uuid'
CONF_TYPE = 'type'
CONF_SPI_ID = 'spi_id'
CONF_HARDWARE_UART = 'hardware_uart'
CONF_UART_ID = 'uart_id'
CONF_UID = 'uid'
CONF_TX_PIN = 'tx_pin'
CONF_RX_PIN = 'rx_pin'
CONF_CO2 = 'co2'
CONF_SHUNT_RESISTANCE = 'shunt_resistance'
CONF_MAX_CURRENT = 'max_current'
CONF_MAX_VOLTAGE = 'max_voltage'
CONF_CURRENT = 'current'
CONF_POWER = 'power'
CONF_BUS_VOLTAGE = 'bus_voltage'
CONF_SHUNT_VOLTAGE = 'shunt_voltage'
CONF_CONDITION = 'condition'
CONF_ELSE = 'else'
CONF_EFFECTS = 'effects'
CONF_RANDOM = 'random'
CONF_EFFECT_ID = 'effect_id'
CONF_COLORS = 'colors'
CONF_STATE = 'state'
CONF_DURATION = 'duration'
CONF_WIDTH = 'width'
CONF_ILLUMINANCE = 'illuminance'
CONF_COLOR_TEMPERATURE = 'color_temperature'
CONF_BATTERY_LEVEL = 'battery_level'
CONF_MOISTURE = 'moisture'
CONF_CONDUCTIVITY = 'conductivity'
CONF_RC_SWITCH_RAW = 'rc_switch_raw'
CONF_RC_SWITCH_TYPE_A = 'rc_switch_type_a'
CONF_RC_SWITCH_TYPE_B = 'rc_switch_type_b'
CONF_RC_SWITCH_TYPE_C = 'rc_switch_type_c'
CONF_RC_SWITCH_TYPE_D = 'rc_switch_type_d'
CONF_CODE = 'code'
CONF_PROTOCOL = 'protocol'
CONF_PULSE_LENGTH = 'pulse_length'
CONF_SYNC = 'sync'
CONF_ZERO = 'zero'
CONF_ONE = 'one'
CONF_GROUP = 'group'
CONF_DEVICE = 'device'
CONF_FAMILY = 'family'
CONF_FILE = 'file'
CONF_GLYPHS = 'glyphs'
CONF_SIZE = 'size'
CONF_RESIZE = 'resize'
CONF_ROTATION = 'rotation'
CONF_DC_PIN = 'dc_pin'
CONF_RESET_PIN = 'reset_pin'
CONF_BUSY_PIN = 'busy_pin'
CONF_ESP8266_RESTORE_FROM_FLASH = 'esp8266_restore_from_flash'
CONF_FULL_UPDATE_EVERY = 'full_update_every'
CONF_DATA_PINS = 'data_pins'
CONF_ENABLE_PIN = 'enable_pin'
CONF_RS_PIN = 'rs_pin'
CONF_RW_PIN = 'rw_pin'
CONF_DIMENSIONS = 'dimensions'
CONF_NUM_CHIPS = 'num_chips'
CONF_INTENSITY = 'intensity'
CONF_EXTERNAL_VCC = 'external_vcc'
CONF_TIMEZONE = 'timezone'
CONF_SERVERS = 'servers'
CONF_HEATER = 'heater'
CONF_VOLTAGE = 'voltage'
CONF_CURRENT_RESISTOR = 'current_resistor'
CONF_VOLTAGE_DIVIDER = 'voltage_divider'
CONF_SEL_PIN = 'sel_pin'
CONF_CF_PIN = 'cf_pin'
CONF_CF1_PIN = 'cf1_pin'
CONF_CHANGE_MODE_EVERY = 'change_mode_every'
CONF_PAGE_ID = 'page_id'
CONF_COMPONENT_ID = 'component_id'
CONF_COLD_WHITE = 'cold_white'
CONF_PAGES = 'pages'
CONF_WARM_WHITE = 'warm_white'
CONF_COLD_WHITE_COLOR_TEMPERATURE = 'cold_white_color_temperature'
CONF_WARM_WHITE_COLOR_TEMPERATURE = 'warm_white_color_temperature'
CONF_HIDDEN = 'hidden'
CONF_ON_LOOP = 'on_loop'
CONF_ON_TIME = 'on_time'
CONF_SECONDS = 'seconds'
CONF_MINUTES = 'minutes'
CONF_HOURS = 'hours'
CONF_DAYS_OF_MONTH = 'days_of_month'
CONF_MONTHS = 'months'
CONF_DAYS_OF_WEEK = 'days_of_week'
CONF_CRON = 'cron'
CONF_POWER_SAVE_MODE = 'power_save_mode'
CONF_POWER_ON_VALUE = 'power_on_value'
CONF_PM_1_0 = 'pm_1_0'
CONF_PM_2_5 = 'pm_2_5'
CONF_PM_10_0 = 'pm_10_0'
CONF_FORMALDEHYDE = 'formaldehyde'
CONF_ON_TAG = 'on_tag'
CONF_ARGS = 'args'
CONF_FORMAT = 'format'
CONF_FOR = 'for'
CONF_COLOR_CORRECT = 'color_correct'
CONF_ON_JSON_MESSAGE = 'on_json_message'
CONF_ACCELERATION = 'acceleration'
CONF_DECELERATION = 'deceleration'
CONF_MAX_SPEED = 'max_speed'
CONF_TARGET = 'target'
CONF_POSITION = 'position'
CONF_STEP_PIN = 'step_pin'
CONF_DIR_PIN = 'dir_pin'
CONF_SLEEP_PIN = 'sleep_pin'
CONF_SEND_FIRST_AT = 'send_first_at'
CONF_TIME_ID = 'time_id'
CONF_RESTORE_STATE = 'restore_state'
CONF_TIMING = 'timing'
CONF_INVALID_COOLDOWN = 'invalid_cooldown'
CONF_MY9231_ID = 'my9231_id'
CONF_NUM_CHANNELS = 'num_channels'
CONF_UPDATE_ON_BOOT = 'update_on_boot'
CONF_INITIAL_VALUE = 'initial_value'
CONF_RESTORE_VALUE = 'restore_value'
CONF_PINS = 'pins'
CONF_SENSORS = 'sensors'
CONF_BINARY_SENSORS = 'binary_sensors'
CONF_OUTPUTS = 'outputs'
CONF_SWITCHES = 'switches'
CONF_TEXT_SENSORS = 'text_sensors'
CONF_INCLUDES = 'includes'
CONF_LIBRARIES = 'libraries'
CONF_PIN_A = 'pin_a'
CONF_PIN_B = 'pin_b'
CONF_PIN_C = 'pin_c'
CONF_PIN_D = 'pin_d'
CONF_SLEEP_WHEN_DONE = 'sleep_when_done'
CONF_STEP_MODE = 'step_mode'
CONF_COMPONENTS = 'components'
CONF_DATA_TEMPLATE = 'data_template'
CONF_VARIABLES = 'variables'
CONF_SERVICE = 'service'
CONF_ENTITY_ID = 'entity_id'
CONF_RESTORE_MODE = 'restore_mode'
CONF_INTERVAL = 'interval'
CONF_DIRECTION = 'direction'
CONF_VARIANT = 'variant'
CONF_METHOD = 'method'
CONF_FAST_CONNECT = 'fast_connect'
CONF_INTERLOCK = 'interlock'
CONF_ON_TURN_ON = 'on_turn_on'
CONF_ON_TURN_OFF = 'on_turn_off'
CONF_USE_ADDRESS = 'use_address'
CONF_FROM = 'from'
CONF_TO = 'to'
CONF_SEGMENTS = 'segments'
CONF_MIN_POWER = 'min_power'
CONF_MIN_VALUE = 'min_value'
CONF_MAX_VALUE = 'max_value'
CONF_RX_ONLY = 'rx_only'


ALLOWED_NAME_CHARS = u'abcdefghijklmnopqrstuvwxyz0123456789_'
ARDUINO_VERSION_ESP32_DEV = 'https://github.com/platformio/platform-espressif32.git#feature/stage'
ARDUINO_VERSION_ESP32_1_0_0 = 'espressif32@1.5.0'
ARDUINO_VERSION_ESP32_1_0_1 = 'espressif32@1.6.0'
ARDUINO_VERSION_ESP8266_DEV = 'https://github.com/platformio/platform-espressif8266.git#feature' \
                              '/stage'
ARDUINO_VERSION_ESP8266_2_5_0 = 'espressif8266@2.0.0'
ARDUINO_VERSION_ESP8266_2_3_0 = 'espressif8266@1.5.0'
